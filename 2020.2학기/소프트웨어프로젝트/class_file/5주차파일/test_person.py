from unittest import TestCase
from person import Person

class TestPerson(TestCase):
    def test_last_name(self):
        bob = Person('Bob Smith')
        self.assertEqual(bob.last_name(),'Smith')
    def test_give_raise(self):
        sue = Person("Sue James", job='dev', pay = 100000)
        print(sue.give_raise(0.1))