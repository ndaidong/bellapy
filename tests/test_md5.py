import unittest
from bella import Bella as bella

class TestMD5(unittest.TestCase):

  def test_default(self):
    rid = bella.md5('hello world')
    self.assertEqual(len(rid), 32, 'It must generate 32 characters')

  def test_nothing(self):
    rid = bella.md5()
    self.assertEqual(len(rid), 0, 'It must generate an empty string')

if __name__ == '__main__':
  unittest.main()