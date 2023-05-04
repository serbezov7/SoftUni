from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hero_name", 99, 100, 30)
        self.enemy = Hero("hero_name1", 10, 10, 10)

    def test_proper_init(self):
        self.assertEqual("hero_name", self.hero.username)
        self.assertEqual(99, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_raises_battle_with_yourself(self):
        enemy_hero = Hero("hero_name", 100, 100, 100)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_raises_when_hero_needs_to_rest(self):
        enemy_hero = Hero("hero_name1", 100, 100, 100)
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_raises_when_enemy_needs_rest(self):
        enemy_hero = Hero("hero_name1", 100, 0, 100)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight hero_name1. He needs to rest", str(error.exception))

    def test_correct_player_damage(self):
        self.assertEqual(2970, self.hero.damage * self.hero.level)

    def test_correct_enemy_damage(self):
        self.assertEqual(100, self.enemy.damage * self.enemy.level)

    def test_draw_case_after_battle(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_when_hero_wins(self):
        self.enemy.damage = 1
        self.hero.battle(self.enemy)

        self.assertEqual(self.hero.level, 100)
        self.assertEqual(self.hero.health, 95)
        self.assertEqual(self.hero.damage, 35)

    def test_hero_wins_return_proper_string(self):
        self.enemy.damage = 1
        self.assertEqual("You win", self.hero.battle(self.enemy))

    def test_when_enemy_wins(self):
        self.hero.damage = 1
        self.hero.level = 1
        self.hero.battle(self.enemy)

        self.assertEqual(self.enemy.level, 11)
        self.assertEqual(self.enemy.health, 14)
        self.assertEqual(self.enemy.damage, 15)

    def test_enemy_wins_return_proper_string(self):
        self.hero.damage = 1
        self.hero.level = 1
        self.assertEqual("You lose", self.hero.battle(self.enemy))

    def test_str_returns_proper_string(self):
        self.assertEqual("Hero hero_name: 99 lvl\nHealth: 100\nDamage: 30\n", str(self.hero))




if __name__ == "__main__":
    main()