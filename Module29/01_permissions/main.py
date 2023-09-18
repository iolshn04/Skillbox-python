import functools
from typing import Callable


def check_permission(permission: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    func.__name__)
                )

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# зачтено
