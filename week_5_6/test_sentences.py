from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(2):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    tense = ["past", "present", "future"]
    for _ in range(4):
        if tense == "past":
            word = get_verb(2,"past")
            assert word in past_verbs

    present_1 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        if tense == "present":
            word = get_verb(4)
            assert word in present_1
    
    present_0 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        if tense == "present":
            word = get_verb(1)
            assert word in present_0
    
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(4):
        if tense == "future":
            word = get_verb(4)
            assert word in future_verbs

def test_get_preposition():
    latest_words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in latest_words

def test_get_prepositional_phrase():
    word = get_prepositional_phrase(1)
    assert word in word

pytest.main(["-v", "--tb=line", "-rN", __file__])
