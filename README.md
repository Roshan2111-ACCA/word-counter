# word-counter

A tiny Python utility for counting words and characters in a string.

## Fuctions

- `count_words(text)` — returns the number of words
- `count_chars(text, include_spaces=True)` — returns character count
- `most_common_word(text)` — returns the most frequent word

## Usage

```python
from word_counter import count_words, count_chars, most_common_word

text = "the quick brown fox jumps over the lazy dog"
print(count_words(text))        # 9
print(count_chars(text))        # 43
print(most_common_word(text))   # "the"
```
