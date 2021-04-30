import pytest
import sys
sys.path.append(".")
from mentor import Mentor
from constants import Language, Country, Interest
from mentorMatch import MentorMatch

mentorA = Mentor("Jack", "English", "Computer Science", "United States")
mentorB = Mentor("B", "English", "Computer Science, Data Science", "Germany")
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
    assert 0.67 == mentorB.interests_similarity(menteeA.interests)

def test_overAllSimilarityScoreIs():
    assert 0.5 == mentorA.overall_similarity(mentee)

def test_emptyMenteeEdgeCaseTesting():
    menteeB = Mentor("", "", "", "")
    assert 0.0 == mentorA.overall_similarity(menteeB)

def test_findBestMentorMatchShouldReturnWhenThereAreNoAvailableMentors():
    match = MentorMatch
    assert None == match.bestMatch(mentee)
    





