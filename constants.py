
from enum import Enum

class Language(Enum):
    ENGLISH = "English"
    FRENCH = "French"
    GERMAN = "German"
    CHINESE = "Chinese"

class Country(Enum):
    US = "United States"
    UK = "United Kingdom"
    GERMANY = "Germany"
    INDIA = "India"

class Interest(Enum):
    CS = "Computer Science"
    DS = "Data Science"
    ML = "Machine Learning"
    NETWORKENG = "Network Engineering"
    SECURITY = "CyberSecurity"