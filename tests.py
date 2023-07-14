import unittest
import sys, os

sys.path.append(os.getcwd())

import main


class TestSuperStackPush(unittest.TestCase):

    def test_SS_push(self):
        "Теструем что пушит без проблем и не падает с ошибкой"
        ss = main.SuperStack()
        self.assertEqual(ss.push(12), None)
        self.assertEqual(ss.push("123"), None)
        self.assertEqual(ss.push(["123", 412]), None)
        self.assertEqual(ss.push({"sd": 1245}), None)
        self.assertEqual(ss.push(("touple", "touple")), None)

    def test_SS_peek(self):
        "Проверка корректных значений"
        ss = main.SuperStack()

        self.assertEqual(ss.peek(), None)
        ss.push(1)
        ss.push(2)
        ss.push(3)
        self.assertEqual(ss.peek(), 3)
        ss.push([12, 12])
        self.assertEqual(ss.peek(), [12, 12])
        ss.push("qweq")
        self.assertEqual(ss.peek(), "qweq")
        ss.push([])
        self.assertEqual(ss.peek(), [])

    def test_SS_pop(self):
        "Проверка корректных значений"
        ss = main.SuperStack()

        self.assertEqual(ss.pop(), None)
        self.assertEqual(ss.pop(), None)
        ss.push(12)
        self.assertEqual(ss.pop(), 12)
        self.assertEqual(ss.peek(), None)
        ss.push(11)
        ss.push(["12", 13])
        ss.push(13)
        self.assertEqual(ss.pop(), 13)
        self.assertEqual(ss.peek(), ["12", 13])
        self.assertEqual(ss.pop(), ["12", 13])
        self.assertEqual(ss.pop(), 11)
        self.assertEqual(ss.pop(), None)
        self.assertEqual(ss.pop(), None)
        self.assertEqual(ss.peek(), None)
