import sys
sys.path.append(".")
from constants import Language, Country, Interest

# Understands How Similar Mentors are to Mentees
class Mentor:

    def __init__(self, name, language, interests, country):
        try:
            self.name = name
            self.language = self.convertToEnum(language, Language)
            self.interests = self.convertToEnum(interests, Interest)
            self.country = self.convertToEnum(country, Country)
        except AttributeError as e:
            print(e)

    def convertToEnum(self, values, enumType):
        values = values.split(",")
        result = set()
        for value in values:
            value = value.strip()
            result.add(enumType(value))
        return result

    def language_similarity(self, language):
        values = language.split(",")
        total, matched = 0, 0
        for value in values:
            value = value.strip()
            if Language(value) in self.language:
                matched+=1
            total+=1
        return round(matched/total, 2)

    def location_similarity(self, location):
        if self.country == Country(location):
            return 1.0
        return 0.0

    def interests_similarity(self, interests):
        values = interests.split(",")
        total, matched = 0, 0
        for value in values:
            value = value.strip()
            if Interest(value) in self.interests:
                matched+=1
            total+=1
        return round(matched/total, 2)




    