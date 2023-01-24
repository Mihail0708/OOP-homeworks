from unittest import TestCase, main
from student.project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Name")
        self.student_with_courses = Student("Other Name", {"key": ["notes"]})

    def test_initializing(self):
        self.assertEqual('Name', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_if_course_name_in_courses(self):
        result = self.student_with_courses.enroll("key", ["other"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'key': ['notes', 'other']}, self.student_with_courses.courses)

    def test_enroll_if_add_course_notes_yes(self):
        result = self.student.enroll("key", ["notes"], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'key': ['notes']}, self.student.courses)

    def test_enroll_if_add_course_notes_empty_str(self):
        result = self.student.enroll("key", ["notes"], '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'key': ['notes']}, self.student.courses)

    def test_enroll_if_add_course_notes_no(self):
        result = self.student.enroll("key", ["notes"], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'key': []}, self.student.courses)

    def test_add_notes_if_course_name_in_courses(self):
        result = self.student_with_courses.add_notes('key', 'other')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'key': ['notes', 'other']}, self.student_with_courses.courses)

    def test_add_notes_raise_exception_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('key', 'other')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_in_courses(self):
        result = self.student_with_courses.leave_course("key")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_course_raise_exception_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("key")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
