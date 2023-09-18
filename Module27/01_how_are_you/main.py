import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который выводит ответ на поставленный вопрос
    """

    @functools.wraps(func)
    def answer(*args, **kwargs) -> Any:
        question = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func()
        return result

    return answer


@how_are_you
def test() -> Any:
    print('<Тут что-то происходит...>')


test()

# зачтено
