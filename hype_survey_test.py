import unittest
from unittest.mock import patch

from hype_survey import hype_survey


class HypeSurveyTest(unittest.TestCase): 

    def test_single_survey(self): 
        user_input = ['Cardi', '01/01/2003', '16', '3', '28', 'gmail', 'recursion', 'False']
        expected = [{0: 'Cardi', 1: '01/01/2003', 2: '16', 3: '3', 4: '28', 5: 'gmail', 6: 'recursion'}]
        with patch('builtins.input', side_effect=user_input): 
            answers = hype_survey.collect_responses()
        self.assertEqual(answers, expected)

    def test_multiple_surveys(self): 
        user_input = ['Beyonce', '01/01/2004', '15', '2', '30', 'facebook', 'loops', 'True',
                      'Cardi', '01/01/2003', '16', '3', '28', 'gmail', 'recursion', 'False']
        expected = [{0: 'Beyonce', 1: '01/01/2004', 2: '15', 3: '2', 4: '30', 5: 'facebook', 6: 'loops'},
                    {0: 'Cardi', 1: '01/01/2003', 2: '16', 3: '3', 4: '28', 5: 'gmail', 6: 'recursion'}]
        with patch('builtins.input', side_effect=user_input): 
            answers = hype_survey.collect_responses()
        self.assertEqual(answers, expected)


if __name__ == '__main__': 
    unittest.main()

