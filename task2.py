from helper import Helper


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Меньшее из двух чисел заменить их полусуммой, большее - их удвоенным произведением')
        x = helper.set_real_number('x')
        y = helper.set_real_number('y', x)
        print('----------------------------------------------------------')
        checked_values = self.__check_values(x, y)
        print(f'Введенные x, y после проверки: \nx = {checked_values[0]}, \ny = {checked_values[1]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __check_values(x: float, y: float) -> list[float]:
        new_x = 0.0
        new_y = 0.0
        if x < y:
            new_x = round((x + y) / 2, 2)
            new_y = round((x * y) * 2, 2)
        else:
            new_y = round((x + y) / 2, 2)
            new_x = round((x * y) * 2, 2)
        return [new_x, new_y]
