# -*- coding: utf-8 -*-

"""
Program: unit_test.py
Author: Kai Mwirotsi-Shaw
Last date modified: 11/10/2023

This file contains the student class that has student details
"""

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        accepted_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-.")
        if not accepted_characters.issuperset(str(lname)):
            print("Please ensure you've entered a valid last name")
            raise ValueError
        if not accepted_characters.issuperset(str(fname)):
            print("Please ensure you've entered a valid first name")
            raise ValueError
        if not accepted_characters.issuperset(str(major)):
            print("Please ensure you've entered your major correctly")
            raise ValueError
        
        self.last_name = lname
        self.first_name = fname
        self.major = major
            
        if isinstance(gpa,float)  != True:
            raise ValueError
        if gpa < 0 or gpa > 4:
            print("Please enter a valid gpa")
            raise ValueError
        else:
            self.gpa = float(gpa)
    
    def set_last_name(self, lname):
         self.last_name = lname

    def set_first_name(self, fname):
         self.first_name = fname
        
    def set_major(self, major):
         self.major = major
        
    def set_gpa(self, gpa):
         self.gpa = gpa

    def get_last_name(self):
         return self.last_name

    def get_first_name(self):
         return self.first_name
     
    def get_major(self):
         return self.major
     
    def get_gpa(self):
        return self.gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)