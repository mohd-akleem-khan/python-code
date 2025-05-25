import unittest
from name import formatted_name
class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		fname=formatted_name('Manoj','Kumar')
		self.assertEqual(fname,'Manoj Kumar')
	def test_first_middle_last_name(self):
		foname=formatted_name('amit','yadav','kumar')
		self.assertEqual(foname,'Amit Kumar Yadav')
if __name__=='__main__':
	unittest.main()
