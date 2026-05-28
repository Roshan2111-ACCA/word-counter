"""A simple word counter utility."""


def count_words(text):
    """Count the number of words in a string."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def count_chars(text, include_spaces=True):
    """Count characters in a string."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def most_common_word(text):
    """Return the most common word in the text."""
    if not text.strip():
        return None
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return max(counts, key=counts.get)
