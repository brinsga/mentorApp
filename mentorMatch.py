import sys
sys.path.append(".")
from mentor import Mentor

MATCH_THRESHOLD = 0.3

#Understands the mentor mentee matches 
class MentorMatch():

    def __init__(self):
        self.mentors = []
        self.mentees = []

    def bestMentor(self, toMatch):
        best = None
        curr_best = 0.0
        for mentor in self.mentors:
            if not mentor.isMatched():
                value = mentor.overall_similarity(toMatch)
                if value >= MATCH_THRESHOLD and value > curr_best:
                    curr_best = value
                    best = mentor
        return best

    def addMentor(self, person):
        self.mentors.append(person)

    def addMentees(self, person):
        self.mentees.append(person)