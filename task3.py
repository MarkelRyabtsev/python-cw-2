from helper import Helper


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('По заданному номеру месяца вывести название следующего месяца. Использовать оператор case')
        month_number = helper.set_natural_number('Введите номер месяца', range(1, 12))
        print('----------------------------------------------------------')
        print(f'Следующий месяц после введенного : {self.__get_next_month_name(month_number)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_next_month_name(month_number: int) -> str:
        next_month_number = 1 if month_number == 12 else month_number + 1
        if next_month_number == 1:
            return 'Январь'
        elif next_month_number == 2:
            return 'Февраль'
        elif next_month_number == 3:
            return 'Март'
        elif next_month_number == 4:
            return 'Апрель'
        elif next_month_number == 5:
            return 'Май'
        elif next_month_number == 6:
            return 'Июнь'
        elif next_month_number == 7:
            return 'Июль'
        elif next_month_number == 8:
            return 'Август'
        elif next_month_number == 9:
            return 'Сентябрь'
        elif next_month_number == 10:
            return 'Октябрь'
        elif next_month_number == 11:
            return 'Ноябрь'
        elif next_month_number == 12:
            return 'Декабрь'
        else:
            return 'Ошибка!'
