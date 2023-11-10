# -*- coding: utf-8 -*-

"""
Program: unit_test.py
Author: Kai Mwirotsi-Shaw
Last date modified: 11/10/2023

This file tests the student class
"""

import unittest
import student as s

class Sudent_Test_Case(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Lazlo', 'Bill', "Mathematics", 3.8)
    def tearDown(self):
        del self.student
    def test_object_created_required_attributes(self):
        student = s.Student('Lazlo', 'Bill', "Mathematics")
        assert student.last_name == 'Lazlo'
        assert student.first_name == 'Bill'
        assert student.major == 'Mathematics'
    def test_object_created_all_attributes(self):
        student = s.Student('Lazlo', 'Bill', "Mathematics", 3.8)
        assert student.last_name == 'Lazlo'
        assert student.first_name == 'Bill'
        assert student.major == 'Mathematics'
        assert student.gpa == 3.8
    def test_student_str(self):
        self.setUp()
        print(str(self.student))
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s.Student(23, 'Bill', "Mathematics", 3.8)
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s.Student("Lazlo", 39, "Mathematics", 3.8)
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = s.Student("Lazlo", 'Bill', 90, 3.8)
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s.Student("Lazlo", 'Bill', "Mathematics", "hello")
        
if __name__ == '__main__':
    unittest.main()
    student1 = s.Student('Samantha', 'Arnold', "p.e", 4.0)
    student2 = s.Student('Bob', 'Bugel', "Music", 3.9)
    print(str(student1))
    print(str(student2))