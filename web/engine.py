from random import randint
import random


class TableMixin:
    def get_complete_dict(self) -> list:
        complete_list = []

        for psy in self.list_psychics:
            complete_list.append({
                'name': psy.name,
                'guess': psy.predict_number,
                'success': round((psy.success / len(psy.predict_number) * 100), 2)
            })

        return complete_list


class User:
    __slots__ = ['user_number']

    def __init__(self, user_number: list = []) -> None:
        self.user_number = user_number

    def get_user_number(self, number):
        self.user_number.append(number)


class Psychic:

    __slots__ = ['name', 'predict_number', 'success']

    def __init__(self, predict_number: list = [], success: int = 0, name: str = 'NoName') -> None:
        self.name = name
        self.predict_number = predict_number
        self.success = success

    def try_predict_number(self):
        number = randint(10, 99)
        self.predict_number.append(number)

    def add_success(self):
        self.success += 1

    def result_predict(self, user_number: int) -> None:
        if self.predict_number[-1] == user_number:
            self.add_success()


class PsychicList(TableMixin):

    names_list = [
        'Мария',
        'Света',
        'Лиза',
        'Женя',
        'Володя',
        'Павел',
        'Сергей',
        'Дмитрий',
        'Анатолий',
        'Андрей',
        'Влад',
        'Коля',
        'Олег',
        'Катя',
        'Алексей',
        'Михаил',
        'Денис'
    ]

    def __init__(self) -> None:
        self.list_psychics: list(Psychic) = []

    def create_list_psychics(self, count_psy: int) -> None:
        for i in range(count_psy):
            psy = Psychic()
            psy.name = random.choice(self.names_list)
            self.list_psychics.append(psy)

    def add_psychics_to_list(self, obj: Psychic) -> None:
        self.list_psychics.append(obj)
