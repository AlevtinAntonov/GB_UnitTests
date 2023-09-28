# Задание 1. Проект Vehicle. Написать следующие тесты с использованием JUnit5:
#  - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор
#  instanceof).
#  - Проверить, что объект Car создается с 4-мя колесами.
#  - Проверить, что объект Motorcycle создается с 2-мя колесами.
#  - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
#  - Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
#  - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина
# останавливается (speed = 0).
#  - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл
# останавливается (speed = 0).

import unittest

from vehicle import *


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Audi', 'Q5', 2021)
        self.motorcycle = Motorcycle('BMW', 'S 1000 XR (K69)', 2020)

    def tearDown(self) -> None:
        self.car = None
        self.motorcycle = None

    def test_car_is_instance_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_has_four_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

    def test_motorcycle_has_two_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_car_speed_by_mode_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed_by_mode_test_drive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park_mode_after_test_drive(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
