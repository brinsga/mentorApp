import pytest
import sys
sys.path.append(".")
from mentor import Mentor
from constants import Language, Country, Interest

mentorA = Mentor("Jack", "English", "Computer Science", "United States")

def test_mentorAMenteeBSpeaksEngHasSimilarityScoreOne():
    assert 1 == mentorA.language_similarity("English")

def test_mentorLocationUSMenteeLocationUKShouldReturnZero():
    assert 0 == mentorA.location_similarity("United Kingdom")

def test_wrongEnumForCountryPolandRaisesError():
    with pytest.raises(ValueError):
        mentorB = Mentor("B", "English", "Computer Science", "Poland")





