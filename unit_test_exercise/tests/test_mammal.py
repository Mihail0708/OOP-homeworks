from unittest import TestCase, main
from projects.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Dog", "Domestic", "Bark")

    def test_initializing(self):
        self.assertEqual('Dog', self.mammal.name)
        self.assertEqual('Domestic', self.mammal.type)
        self.assertEqual('Bark', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_return_make_sound(self):
        self.assertEqual('Dog makes Bark', self.mammal.make_sound())

    def test_return_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_return_info(self):
        self.assertEqual('Dog is of type Domestic', self.mammal.info())


if __name__ == '__main__':
    main()