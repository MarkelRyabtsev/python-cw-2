from helper import Helper


class Task1:

    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны действительные числа x, y. Если x, y отрицательны, то каждое значение заменить его модулем; '
              '\nесли отрицательное только одно из них, то оба значения увеличить на 0.5; '
              '\nесли оба значения не отрицательны и ни одно из них не принадлежит отрезку [0.5, 2.0], '
              '\nто оба значения уменьшить в 10 раз; в остальных случаях x, y оставить без изменения')
        x = helper.set_real_number('x')
        y = helper.set_real_number('y')
        print('----------------------------------------------------------')
        checked_values = self.__check_values(x, y)
        print(f'Введенные x, y после проверки: \nx = {checked_values[0]}, \ny = {checked_values[1]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __check_values(x: float, y: float) -> list[float]:
        if x < 0.0 and y < 0.0:
            x = abs(x)
            y = abs(y)
        elif x < 0.0 or y < 0.0:
            x += 0.5
            y += 0.5
        elif (x > 0.0 and y > 0.0) and (0.5 < x < 2.0 and 0.5 < y < 2.0):
            x /= 10.0
            y /= 10.0
        return [x, y]
