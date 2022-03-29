class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; ' \
               f'Длительность: {"%.3f" %self.duration} ч.; ' \
               f'Дистанция: {"%.3f" % self.distance} км; ' \
               f'Ср. скорость: {"%.3f" %self.speed} км/ч; ' \
               f'Потрачено ккал: {"%.3f" %self.calories}.'
        pass


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage('RUN',
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        pass


# noinspection TaskProblemsInspection
class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self, coffee_calorie_1=18, coffee_calorie_2=20):
        return (coffee_calorie_1 * self.get_mean_speed() - coffee_calorie_2) * self.weight / self.M_IN_KM * (self.duration * 60)
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage('Running',
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        pass


# noinspection TaskProblemsInspection
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        return (0.035 * self.weight + (self.get_mean_speed() ** 2 // self.height) * 0.029 * self.weight) * self.duration * 60
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage('SportsWalking',
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        pass


# noinspection TaskProblemsInspection
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        pass

    def get_spent_calories(self):
        return (self.get_mean_speed() + 1.1) * 2 * self.weight

    def show_training_info(self) -> InfoMessage:
        return InfoMessage('Swimming',
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    if workout_type == 'SWM':
        return Swimming(data[0], data[1], data[2], data[3], data[4])
    elif workout_type == 'RUN':
        return Running(data[0], data[1], data[2])
    elif workout_type == 'WLK':
        return SportsWalking(data[0], data[1], data[2], data[3])
    pass


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
