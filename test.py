import unittest
from main import LT
from tkinter import *
from tkinter import messagebox
from validate_email import validate_email
import rsaidnumber
from datetime import datetime
import uuid
from playsound import playsound


class MyTestCase(unittest.TestCase):
    def test_submit(self):
        obj = LT()


if __name__ == '__main__':
    unittest.main()
