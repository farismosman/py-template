import unittest
from math import sqrt, pi

from src.circle import Circle

class TestCircle(unittest.TestCase):
	def test_circle_should_have_radius(self):
		circle = Circle(5)

		self.assertEqual(circle.radius, 5)

	def test_should_calculate_circle_area(self):
		radius = 1./sqrt(pi)
		circle = Circle(radius)

		area = circle.area()

		self.assertAlmostEqual(area, 1)

if __name__ == '__main__':
	unittest.main()
		