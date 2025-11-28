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
        print(" Question 1: Rate 1-7 how much representation you feel is reflected from Cal Poly faculty & staff "
              "\n Question 2: Rate 1-7 your comfortability in a classroom setting based on the demographics of your classmates"
              "\n Question 3: Rate 1-7 how supported you feel as a Black student in Cal Poly for resources."
              "\n Question 4: Rate 1-7 how much you agree with the following statement: 'I see students like me walking about campus'"
              "\n Question 5: Rate 1-7 how much you agree with the following statement: 'I feel safe as a Black student at Cal Poly'"
              "\n Question 6: Rate 1-7, 1 being least, 7 being most, how often you face discrimination: hate speech, open prejudices, etc. at Cal Poly")

    def get_average_by_grade(self, question:str, num:int)->float:
        count = 0
        for i in range(7):
            count += interviewQuestions.questions_data[question][num][i]
        average = count / 7
        return average

    def add_question(self, question:str,  grade:str,rating:int):
            #create a key for question if it doesn't exist
            if question not in self.data:
                self.data[question] = {}
            #creates a grade key, and fills it with rating from 1 to 10
            if grade not in self.data[question]:
                self.data[question][grade] = {}
                for i in range(1,11):
                    self.data[question][grade][i] = 0
            #checks if rating is between 1 and 10 and if is, the vote count for that rating increases by 1
            if rating >= 1 and rating <= 10:
                self.data[question][grade][rating] += 1

        #calculates the average rating for a question across all grades
    def average_rating(self,question:str):
            if question not in self.data:
                return None
            total_score = 0 #keeps track of all score
            total_votes = 0#keeps track of all votes
            #goes through all grade and add rating up
            for grade in self.data[question]:
                for rating in self.data[question][grade]:
                    count=self.data[question][grade][rating]
                    total_votes+=count
                    total_score+=rating * count #rating x number of votes

            #calculates average
            if total_votes == 0:
                return None
            else:
                return total_score/total_votes
