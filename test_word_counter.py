from word_counter import count_words, count_chars, most_common_word


def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_empty():
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_count_chars_with_spaces():
    assert count_chars("hello") == 5


def test_count_chars_no_spaces():
    assert count_chars("hi there", include_spaces=False) == 7


def test_most_common_word():
    assert most_common_word("the cat and the dog") == "the"


def test_most_common_word_empty():
    assert most_common_word("   ") is None
