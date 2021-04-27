import pytest
import sys
sys.path.append(".")
from mentor import Mentor

mentorA = Mentor("Jack", "English", "Computer Science", "United States")

def test_mentorAMenteeBSpeaksEngHasSimilarityScoreOne():
    assert 1 == mentorA.language_similarity("English")

def test_mentorLocationUSMenteeLocationUKShouldReturnZero():
    assert 0 == mentorA.location_similarity("United Kingdom")

