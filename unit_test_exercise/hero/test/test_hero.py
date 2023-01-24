from unittest import TestCase, main
from hero.project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Hero', 10, 10.0, 10.0)
        self.enemy = Hero('Enemy', 5, 5.0, 5.0)

    def test_initializing(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(10.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_raise_exception_fight_himself_in_battle(self):
        with self.assertRaises(Exception)as ex:
            self.enemy.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raise_exception_with_health_zero_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError)as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_raise_exception_with_enemy_health_zero_or_less(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError)as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_correct_decrease_health_after_battle(self):
        self.hero.battle(self.enemy)
        self.assertEqual(-15.0, self.hero.health)
        self.assertEqual(-95.0, self.enemy.health)

    def test_return_draw_after_battle(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual('Draw', result)

    def test_hero_win_after_battle(self):
        self.hero.health = 100.0
        result = self.hero.battle(self.enemy)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(80.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)
        self.assertEqual('You win', result)

    def test_enemy_win_after_battle(self):
        self.enemy.health = 150.0
        result = self.hero.battle(self.enemy)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(55.0, self.enemy.health)
        self.assertEqual(10.0, self.enemy.damage)
        self.assertEqual('You lose', result)

    def test_correct_str_represent(self):
        result = str(self.hero)
        self.assertEqual("Hero Hero: 10 lvl\nHealth: 10.0\nDamage: 10.0\n", result)


if __name__ == '__main__':
    main()