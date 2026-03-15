from home_snack import *
from unittest import TestCase

class TestClass (TestCase):

	def test_length_of_a_list_is_equal(self):

		expected = length_of_list([2, 6, 4, 9, 6])
		actual = 5

		self.assertEqual(expected, actual)

	def test_sum_of_elements_at_even_positions(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = sum_of_elements_at_even_positions(numbers)
		actual = 16

		self.assertEqual(expected, actual)

	def test_sum_of_elements_at_odd_positions(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = sum_of_elements_at_odd_positions(numbers)
		actual = 20

		self.assertEqual(expected, actual)

	def test_the_everage_of_elements_in_a_list(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = average_of_elements(numbers)
		actual = 4.5

		self.assertEqual(expected, actual)

	def test_product_of_elements_in_every_third_positions(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = product_of_elements_in_every_third_positions(numbers)
		actual = 10

		self.assertEqual(expected, actual)

	def test_for_largest_number(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = largest_element(numbers)
		actual = 9

		self.assertEqual(expected, actual)

	def test_for_smallest_number(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = smallest_element(numbers)
		actual = 1

		self.assertEqual(expected, actual)

	def test_for_string_length_in_a_list(self):

		words = {"Ene", "Tablet", "At", "bubble", "hannah"}

		expected = string_length_in_a_list(words)
		expected_formatted = (expected[0], sorted(expected[1]))

		actual = (5, ["Ene", "Tablet", "hannah"])

		self.assertEqual(expected_formatted, actual)

	def test_output_is_1_to_15(self):

		expected = list_of_integers()
		actual = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		self.assertEqual(expected, actual)

	def test_for_sum_of_elements_at_multiples_of_three(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = sum_of_elements_at_multiples_of_three(numbers)
		actual = 7
		self.assertEqual(expected, actual)
		
	def test_for_sum_of_elements_in_first_middle_and_last_position(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4]

		expected = sum_of_elements_in_first_middle_and_last_position(numbers)

		actual = 10
		self.assertEqual(expected, actual)

	def test_for_sum_of_elements_in_first_middle_and_last_position_for_odd_length(self):

		numbers = [4, 9, 5, 1, 3, 2, 8, 4, 3]

		expected = sum_of_elements_in_first_middle_and_last_position(numbers)

		actual = 10
		self.assertEqual(expected, actual)


				
