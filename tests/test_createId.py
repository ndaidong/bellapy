import unittest
from bella import createId

class TestCreateId(unittest.TestCase):

  def test_generator(self):
    rid1 = createId()
    self.assertEqual(len(rid1), 16, 'It must generate 16 characters')
    rid2 = createId()
    self.assertEqual(len(rid2), 16, 'It must generate 16 characters')

    self.assertNotEqual(rid1, rid2, 'Generated string must be different')

  def test_generator_with_leng(self):
    rid1 = createId(32)
    self.assertEqual(len(rid1), 32, 'It must generate 32 characters')
    rid2 = createId(32)
    self.assertEqual(len(rid2), 32, 'It must generate 32 characters')

    self.assertNotEqual(rid1, rid2, 'Generated string must be different')

if __name__ == '__main__':
  unittest.main()