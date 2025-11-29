from typing import Dict, Optional
import json
import interviewQuestions

class studentPopulations:
    def __init__(self):
        self.data = {}

    def add_population_data(self,year:int, ethnicity:str, percentage:float):
        #this checks if the year already exists else it makes one
        if year not in self.data:
            self.data[year] = {}
        # removes spaces, and makes lower case all upper
        ethnicity = ethnicity.strip().upper()
        # Store the percentage
        self.data[year][ethnicity] = percentage

    def get_year(self,year:int):
        if year in self.data:
            return self.data[year]
        else:
            return None

    def statement(self,year:int, ethnicity:str):
        info = self.get_year(year)
        key= ethnicity.strip().upper()
        if key in info:
            value = info[key]
            return f"{ethnicity.title()} students we {value}% of Cal Poly's student population in {year}"
        else:
            return f"No data for {ethnicity} in {year}"

    #Class for the question : (grade, answers, rating)

class InterviewQuestions:
    def __init__(self):
        self.questions = interviewQuestions.questions_data

    def get_questions(self):
        #displays all the questions
        text = ("Question 1: Rate 1-7 how much representation you feel is reflected from Cal Poly faculty & staff "
              "\n Question 2: Rate 1-7 your comfortability in a classroom setting based on the demographics of your classmates"
              "\n Question 3: Rate 1-7 how supported you feel as a Black student in Cal Poly for resources."
              "\n Question 4: Rate 1-7 how much you agree with the following statement: 'I see students like me walking about campus'"
              "\n Question 5: Rate 1-7 how much you agree with the following statement: 'I feel safe as a Black student at Cal Poly'"
              "\n Question 6: Rate 1-7, 1 being least, 7 being most, how often you face discrimination: hate speech, open prejudices, etc. at Cal Poly")
        return text


    def add_question(self, question:str,  grade:str,rating:int):
            #create a key for question if it doesn't exist
            if question not in self.questions:
                self.questions[question] = {}
            #creates a grade key, and fills it with rating from 1 to 10
            if grade not in self.questions[question]:
                self.questions[question][grade] = {}
                for i in range(1,8):
                    self.questions[question][grade][i] = 0
            #checks if rating is between 1 and 7 and if is, the vote count for that rating increases by 1
            if rating >= 1 and rating <= 7:
                self.questions[question][grade][rating] += 1

    #calculates the average rating for a question across all grades
    def average_rating(self, question: str):
        if question not in self.questions:
            return None
        total_score = 0 #keeps track of all the scores
        total_votes = 0 #keeps track of how many votes a rating has
        for grade in self.questions[question]: # for instance: Freshman, Sophomore, etc.
            for rating in self.questions[question][grade]: # each rating, 1 through 7
                count = self.questions[question][grade][rating] # count becomes how many in each rating
                total_score += rating*count
                total_votes += count
        if total_votes == 0:
            return None
        return total_score/total_votes
