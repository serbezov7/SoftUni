from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Gosho")
        self.student1 = Student("Ivan", {"English": ["note1", "note2"]})

    def test_init(self):
        self.assertEqual("Gosho", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_notes_update_on_existing_course(self):
        result = self.student1.enroll("English", ["note3"])
        self.assertEqual("note3", self.student1.courses["English"][-1])
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_creating_notes_on_non_existing_course(self):
        result = self.student.enroll("Deutsch", ["note1", "note2"], "Y")
        self.assertEqual("note2", self.student.courses["Deutsch"][-1])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_creating_notes_on_non_existing_course2(self):
        result = self.student.enroll("Deutsch", ["note1", "note2"])
        self.assertEqual("note2", self.student.courses["Deutsch"][-1])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_adding_course_with_different_course_notes(self):
        result = self.student.enroll("Deutsch", ["note1", "note2"], "No")
        self.assertEqual([], self.student.courses["Deutsch"])
        self.assertEqual(result, "Course has been added.")

    def test_adding_notes_on_existing_course(self):
        result = self.student1.add_notes("English", "note3")
        self.assertEqual("note3", self.student1.courses["English"][-1])
        self.assertEqual(result, "Notes have been updated")

    def test_adding_notes_on_non_existing_course(self):
        with self.assertRaises(Exception) as error:
            self.student1.add_notes("Deutsch", "note3")
        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_leaving_course_with_existing_course_name(self):
        result = self.student1.leave_course("English")
        self.assertEqual({}, self.student1.courses)
        self.assertEqual(result, "Course has been removed")

    def test_raises_when_course_not_exists(self):
        with self.assertRaises(Exception) as error:
            self.student1.leave_course("Deutsch")
        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()
