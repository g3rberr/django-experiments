from datetime import datetime


def timedeco(func: function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now() - start
            print(f'Выполнилось за {end}')
            return result
        return wrapper

@timedeco
def sum_numbers(x:int, y:int) -> int:
    return x + y


print(sum_numbers(x=3, y=4))