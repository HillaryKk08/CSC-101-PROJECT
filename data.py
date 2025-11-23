from typing import Dict, Optional
import json

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
            return "No data for {ethnicity} in {year}"

    #Class for tge the question : (grage, answers, rating)
class InterviewQuestions:
        def __init__(self):
        #self.data will hold all responses, organized by question and grade level.
            self.data = {}

        def add_question(self, question:str,  grade:str,rating:int):
            #create a key for question if it doesnt exist
            if question not in self.data:
                self.data[question] = {}
            #creates a grade kee, and fills it with rating from 1 to 10
            if grade not in self.data[question]:
                self.data[question][grade] = {}
                for i in range(1,11):
                    self.data[question][grade][i] = 0
            #checks if rating is between 1 to 10 and if it the vote count for that rating increases by 1
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
