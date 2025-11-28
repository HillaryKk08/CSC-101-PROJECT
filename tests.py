import unittest
import data
import StudentDemographic
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
        self.assertEqual(actual, expected)
        # passed


if __name__ == '__main__':
    unittest.main()
