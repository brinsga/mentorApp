import sys
sys.path.append(".")
from constants import Language, Country, Interest

# Understands How Similar Mentors are to Mentees
class Mentor:

    def __init__(self, name, language, interests, country):
        try:
            self.name = name
            self.language = Language(language)
            self.interests = Interest(interests)
            self.country = Country(country)
        except AttributeError as e:
            print(e)
    
    def language_similarity(self, language):
        if self.language == Language(language):
            return 1
        return 0

    def location_similarity(self, location):
        if self.country == Country(location):
            return 1
        return 0



    