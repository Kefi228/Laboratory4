class Car:
    name: str
    weight: float

    def __init__(self, name: str, weight: float) -> None:
        """Создание и подготовка к работе объекта "Автомобиль"

                  :param name: имя машины
                  :param weight: вес

                  Примеры:
                  >>> car = Car("Wolkswagen", 1.5) #инициализация экземпляра класса
              """
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        """Данный метод выводит данные о машине для пользователя.

                        Примеры:
                        >>> car = Car("Wolkswagen", 1.5)
                        >>> car.__str__()
                        """
        return f"Машина {self.name}. Вес {self.weight}."

    def __repr__(self) -> str:
        """Данный метод выводит данные о машине для разработчика.

                                Примеры:
                                >>> car = Car("Wolkswagen", 1.5)
                                >>> car.__repr__()
                                """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r})"

    def editName(self, newName: str) -> None:
        """Данный метод изменяет имя машины.

                 Примеры:
                 >>> car = Car("Wolkswagen", 1.5)
                 >>> car.editName("Toyota")
                 """
        self.name = newName

    def start(self) -> None:
        """Данный метод заводит машину.

                        Примеры:
                        >>> car = Car("Wolkswagen", 1.5)
                        >>> car.start()
                        """
        ...


class PassengerCar(Car):
    passenger: int

    def __init__(self, name: str, weight: float, passenger: int) -> None:
        """Создание и подготовка к работе объекта "Легковой автомобиль"

                          :param name: имя машины
                          :param weight: вес
                          :param passenger: количество пассажиров
                          Примеры:
                          >>> car = PassengerCar("Wolkswagen", 1.5, 5) #инициализация экземпляра класса
                      """
        super().__init__(name=name, weight=weight)
        self.passenger = passenger
        super().__str__()
        super().start()

    def __repr__(self) -> str:
        """Данный метод выводит данные о машине для разработчика, включая количество пассажиров.

                                       Примеры:
                                       >>> car = PassengerCar("Wolkswagen", 1.5, 5)
                                       >>> car.__repr__()
                                       """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, passenger={self.passenger!r})"

    def editName(self, name: str, weight: float) -> str:
        """Данный метод изменяет имя машины, добавляя её вес в название.

                         Примеры:
                         >>> car = PassengerCar("Wolkswagen", 1.5, 5)
                         >>> car.editName("Toyota", 2)
                         """
        self.name = name + str(weight)
        return self.name


class Truck(Car):
    cargo: str

    def __init__(self, name: str, weight: float, cargo: str) -> None:
        """Создание и подготовка к работе объекта "Грузовой автомобиль"

                                  :param name: имя машины
                                  :param weight: вес
                                  :param cargo: тип груза
                                  Примеры:
                                  >>> car = Truck("Wolkswagen", 1.5, "Песок") #инициализация экземпляра класса
                              """
        super().__init__(name=name, weight=weight)
        self.cargo = cargo
        super().__str__()

    def __repr__(self) -> str:
        """Данный метод выводит данные о машине для разработчика, включая тип груза.

                                               Примеры:
                                               >>> car = Truck("Wolkswagen", 1.5, "Песок")
                                               >>> car.__repr__()
                                               """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, cargo={self.cargo!r})"


if __name__ == "__main__":
    # Write your solution here
    pass
