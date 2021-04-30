import sys
sys.path.append(".")
from constants import Language, Country, Interest

LANGUAGE_IMPORTANCE_SCORE = 0.20
LOCATION_IMPORTANCE_SCORE = 0.20
INTERESTS_IMPORTANCE_SCORE = 0.60

# Understands Mentor Similarity Metric
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
        print(values)
        result = set()
        for value in values:
            value = value.strip()
            if value!= "":
                result.add(enumType(value))
        print(result)
        return result

    def language_similarity(self, language):
        total, matched = 0, 0
        for value in language:
            if value in self.language:
                matched+=1
            total+=1

        if total != 0:
            return round(matched/total, 2)
        return 0.0

    def location_similarity(self, location):
        if self.country == location:
            return 1.0
        return 0.0

    def interests_similarity(self, interests):
        total, matched = 0, 0
        for value in interests:
            if value in self.interests:
                matched+=1
            total+=1

        if total != 0:
            return round(matched/total, 2)
        return 0.0

    def overall_similarity(self, mentee):
        language_sim = self.language_similarity(mentee.language)
        location_sim = self.location_similarity(mentee.country)
        interests_sim = self.interests_similarity(mentee.interests)


        total_sim = (LANGUAGE_IMPORTANCE_SCORE*language_sim) + (LOCATION_IMPORTANCE_SCORE*location_sim)+ (INTERESTS_IMPORTANCE_SCORE*interests_sim)

        return total_sim 







    