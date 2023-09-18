import functools
from typing import Callable

app = {}


def callback(route: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            return func(*args, **kwargs)

        return wrapper

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачтено
