import pytest
import sys
sys.path.append(".")
from mentor import Mentor
from constants import Language, Country, Interest

mentorA = Mentor("Jack", "English", "Computer Science", "United States")
mentee = Mentor("MenteeA", "English", "Computer Science, Data Science", "United Kingdom")
menteeA = Mentor("MenteeA", "English", "Computer Science, Data Science, Machine Learning", "United Kingdom")


def test_mentorAMenteeBSpeaksEngHasSimilarityScoreOne():
    assert 1.0 == mentorA.language_similarity(mentee.language)

def test_mentorLocationUSMenteeLocationUKShouldReturnZero():
    assert 0.0 == mentorA.location_similarity(mentee.country)

def test_wrongEnumForCountryPolandRaisesError():
    with pytest.raises(ValueError):
        mentorB = Mentor("B", "English", "Computer Science", "Poland")

def test_MenteeCSDSMLMentorCSMLShouldReturnInterestSimilarityZeroPointSixSeven():

    mentorB = Mentor("B", "English", "Computer Science, Data Science", "Germany")
    assert 0.67 == mentorB.interests_similarity(menteeA.interests)

def test_overAllSimilarityScoreIs():
    assert 0.5 == mentorA.overall_similarity(mentee)




    






