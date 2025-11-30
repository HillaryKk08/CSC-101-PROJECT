import unittest
import data
import StudentDemographic
from StudentDemographic import DemoPopulation
import interviewQuestions


class MyTestCase(unittest.TestCase):
    def test_get_questions(self):
        obj = data.InterviewQuestions()
        actual = obj.get_questions()
        expected = ("Question 1: Rate 1-7 how much representation you feel is reflected from Cal Poly faculty & staff "
              "\n Question 2: Rate 1-7 your comfortability in a classroom setting based on the demographics of your classmates"
              "\n Question 3: Rate 1-7 how supported you feel as a Black student in Cal Poly for resources."
              "\n Question 4: Rate 1-7 how much you agree with the following statement: 'I see students like me walking about campus'"
              "\n Question 5: Rate 1-7 how much you agree with the following statement: 'I feel safe as a Black student at Cal Poly'"
              "\n Question 6: Rate 1-7, 1 being least, 7 being most, how often you face discrimination: hate speech, open prejudices, etc. at Cal Poly")
        print("\nACTUAL (test_get_questions):\n", actual)
        self.assertEqual(actual, expected)
        # passed
    def test_avergage(self):
        obj = data.InterviewQuestions()
        actual = obj.average_rating("Question 1")
        expected = 2.225
        print("\nACTUAL (test_average):", actual)
        self.assertEqual(actual, expected)
        #passed
    def test_add_question(self):
        obj = data.InterviewQuestions()
        obj.add_question("Question 8", "Freshman", 3)
        expected=1
        actual =  obj.questions["Question 8"]["Freshman"][3]
        print("\nACTUAL (test_add_question):", actual)
        self.assertEqual(actual,expected)
        #passed

    def test_add_population(self):
        obj = StudentDemographic.DemoPopulation()
        obj.add_population_data(2024, "AFRICAN AMERICAN", 0.93)
        expected = 0.93
        actual = obj.data[2024]["AFRICAN AMERICAN"]
        print("\nACTUAL (test_add_population):", actual)
        self.assertEqual(actual, expected)

    def test_invalid_ethnicity(self):
        pop = StudentDemographic.DemoPopulation()
        print("\nACTUAL (test_invalid_ethnicity): Expecting KeyError")
        with self.assertRaises(KeyError):
            pop.add_population_data(2022, "MARTIAN", 0.5)

if __name__ == '__main__':
    unittest.main()
