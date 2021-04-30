import sys
sys.path.append(".")
from mentor import Mentor

MATCH_THRESHOLD = 0.3

#Understands the mentor mentee matches 
class MentorMatch():

    def __init__(self):
        self.mentors = []
        self.mentees = []

    def bestMatch(self, toMatch, users):
        best = None
        curr_best = 0.0
        for user in users:
            if not user.isMatched():
                value = user.overall_similarity(toMatch)
                if value >= MATCH_THRESHOLD and value > curr_best:
                    curr_best = value
                    best = user
        return best

    def bestMentor(self, toMatch):
        best = self.bestMatch(toMatch, self.mentors)
        toMatch.updateMatch(best)
        return best

    def bestMentee(self, toMatch):
        best = self.bestMatch(toMatch, self.mentees)
        toMatch.updateMatch(best)
        return best

    def addMentor(self, person):
        self.mentors.append(person)

    def addMentee(self, person):
        self.mentees.append(person)

    def unmatchedPeopleCount(self, users):
        count = 0
        for user in users:
            if not user.isMatched():
                count+=1
        return count 

    def numberOfUnmatchedMentees(self):
        return self.unmatchedPeopleCount(self.mentees)

    def numberOfUnmatchedMentors(self):
        return self.unmatchedPeopleCount(self.mentors)
