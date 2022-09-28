#!/usr/bin/python3
""" Module that defines the class Student
"""

class student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ defines a student by
        first name, last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Public method that retrieves a dictionary
        representation of a Student """

        return(self.__dict__)
