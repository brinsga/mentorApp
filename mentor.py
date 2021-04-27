# Understands How Similar Mentors are to Mentees
class Mentor:

    def __init__(self, name, language, interests, country):
        self.name = name
        self.language = language
        self.interests = interests
        self.country = country
    
    def language_similarity(self, language):
        if self.language == language:
            return 1
        return 0

    def location_similarity(self, location):
        if self.country == location:
            return 1
        return 0

        

    