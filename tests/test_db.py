import unittest

from db import DB


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.db.initialize()