import unittest
from unittest import TestCase
from unittest.mock import patch
from callApi import get_total_pokemon_count

class TestPokeApi(TestCase):
    # Test case to check count of total pokemon
    def test_get_total_pokemon_count(self):
        # This test case assumes that you know the total count of pokemon, which may change
        # Depending on the real-time data from the PokeAPI.
        self.assertEqual(get_total_pokemon_count(), 1302)  # Adjust this number accordingly

    # Mock the API call here and test get_total_pokemon_count
    # This test case will run even if internet is not there
    @patch('callApi.get_all_pokemon')
    def test_get_total_pokemon_count_mock(self, mock_get_all_pokemon):
        # Here we are mocking the response of the API
        mock_get_all_pokemon.return_value = {'count': 10}
        self.assertEqual(get_total_pokemon_count(), 10)

if __name__ == '__main__':
    unittest.main()
