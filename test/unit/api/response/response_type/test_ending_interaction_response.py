import unittest
from unittest.mock import patch, call

from src.api.response.response_tag import ResponseTag
from src.api.response.response_type.ending_interaction_response import EndingInteractionResponse


class TestEndingInteractionResponse(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.ending_interaction_response = EndingInteractionResponse().with_output(self._SOME_REUBERT_OUTPUT)

    @patch('builtins.print')
    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self, print_mock):
        expected_response_format = "\n" + ResponseTag.GOODBYE_TAG.__str__().format(self._SOME_REUBERT_OUTPUT) + "\n"

        self.ending_interaction_response.print()

        print_mock.assert_has_calls([call(expected_response_format)], any_order=False)
