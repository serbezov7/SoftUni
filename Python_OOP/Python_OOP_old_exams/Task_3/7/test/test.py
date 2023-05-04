from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("MyTeam")
        self.other = Team("OtherTeam")

    def test_init(self):
        self.assertEqual("MyTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "My Team1"
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_adding_new_member(self):
        result = self.team.add_member(Gosho=23, Ivan=22)
        self.assertEqual(result, "Successfully added: Gosho, Ivan")
        self.assertEqual(len(self.team.members), 2)
        # self.assertEqual(self.team.members, {"Gosho": 23, "Ivan": 22})

    def test_adding_member_twice(self):
        self.team.add_member(Gosho=23, Ivan=22)
        result = self.team.add_member(Gosho=20)
        self.assertEqual(result, "Successfully added: ")
        # self.assertEqual(self.team.members, {"Gosho": 23, "Ivan": 22})

    def test_successfully_remove_name(self):
        self.team.add_member(Gosho=23, Pesho=22)
        result = self.team.remove_member("Gosho")
        self.assertEqual(result, "Member Gosho removed")
        self.assertEqual(1, len(self.team.members))
        # self.assertEqual(self.team.members, {"Pesho": 22})

    def test_unsuccessfully_remove_name(self):
        self.team.add_member(Gosho=23)
        result = self.team.remove_member("Ivan")
        self.assertEqual(result, "Member with name Ivan does not exist")
        self.assertEqual(1, len(self.team.members))
        # self.assertEqual(self.team.members, {"Gosho": 23})

    def test_gt_method_works_correct(self):
        self.team.add_member(Gosho=23, Ivan=22)
        self.other.add_member(Ivo=32)
        result = self.team.__gt__(self.other)

        self.assertEqual(True, result)

    def test_gt_method_returns_false(self):
        self.other.add_member(Gosho=23, Ivan=22)
        self.team.add_member(Ivo=32)

        result = self.team.__gt__(self.other)

        self.assertEqual(False, result)

    def test_len_method(self):
        self.team.add_member(Gosho=23, Ivan=22)
        result = self.team.__len__()

        self.assertEqual(2, result)

    def test_add_method_works_correct(self):
        self.other.add_member(Gosho=23, Ivan=22)
        self.team.add_member(Ivo=32)

        new_team = self.team.__add__(self.other)

        self.assertEqual("MyTeamOtherTeam", new_team.name)
        self.assertEqual(3, len(new_team.members))
        # self.assertEqual(new_team.members, {"Gosho": 23, "Ivan": 22, "Ivo": 32})

    def test_str_returns_proper_string(self):
        self.team.add_member(Gosho=23, Ivan=22)
        self.assertEqual("Team name: MyTeam\nMember: Gosho - 23-years old\nMember: Ivan - 22-years old", str(self.team))


if __name__ == "__main__":
    main()
