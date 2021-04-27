import pytest
import sys
sys.path.append(".")
from mentor import Mentor

mentorA = Mentor("Jack", "English", "Computer Science", "United States")
print(mentorA)

def test_mentorAMenteeBSpeaksEngHasSimilarityScoreOne():
    mentorA = Mentor("Jack", "English", "Computer Science", "United States")
    assert 1 == mentorA.language_similarity("English")