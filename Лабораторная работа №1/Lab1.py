class Motocycle:
    def __init__(self, color: str, count_passengers, serial_numb: str):
        if not isinstance(color, str):
            raise TypeError('Название цвета должно быть типа str')
        self.color = color
        if count_passengers > 3:
            raise TypeError('Вместимость не более 3 человек!')
        self.count_passengers = count_passengers
        if not isinstance(serial_numb, str):
            raise TypeError('Номер должен совершать буквы и цифры')
        self.serial_numb = serial_numb

    def broken(self):
        print('Мотоцикл не двигается')
        self.health = 0


class Cats:
    def __init__(self, breed: str, age: int, vaccination):
        if not isinstance(breed, str):
            raise TypeError('Название породы должно быть типа str')
        self.breed = breed
        if age > 20:
            raise ValueError('Возраст не более 20 лет')
        self.age = age
        if not vaccination > 3:
            raise ValueError('У кота не менее 3 прививок')
        self.vaccination = vaccination


class Houses:
    def __init__(self, number_of_floors: int, entrance: int):
        if not isinstance(number_of_floors, int):
            raise TypeError('Лучше записать количество этажей цифровым значением')
        if number_of_floors <= 0:
            raise ValueError('Не может быть дом без этажей')
        self.height = number_of_floors
        if entrance <= 0:
            raise ValueError('У дома должен быть вход!!!')
        self.entrance = entrance


if __name__ == "__main__":
    Jupiter = Motocycle('Красный', 2, 'KZ587234')
    Kawasaki = Motocycle('Черный', 2, 'KZ9834718')
    Cat = Cats('Британская', 5, 4)
    house_1 = Houses(9, 2)
    house_2 = Houses(1, 1)
    import doctest

    doctest.testmod()
    pass