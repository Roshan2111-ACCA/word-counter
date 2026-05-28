# ✍️ Word Counter

A clean, simple web app that analyses any text instantly — built with Python and Flask.

🔗 **[Live Demo](https://word-counter.onrender.com)**

---

## What it does

Paste or type any text and get:

- 📝 **Word count**
- 🔤 **Character count** (with and without spaces)
- 🏆 **Most common word**

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| Frontend | HTML + CSS |
| Hosting | Render (free tier) |
| Version Control | GitHub |

## Run locally

```bash
# 1. Clone the repo
git clone https://github.com/Roshan2111-ACCA/word-counter.git
cd word-counter

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py

# 4. Open in browser
# http://localhost:5000
```

## Project Structure

```
word-counter/
├── app.py               # Flask server
├── word_counter.py      # Core logic (count words, chars, etc.)
├── requirements.txt     # Dependencies
├── render.yaml          # Render deployment config
└── templates/
    └── index.html       # Web UI
```

## Functions

- `count_words(text)` — returns the number of words
- `count_chars(text, include_spaces=True)` — returns character count
- `most_common_word(text)` — returns the most frequent word

---

Made by [Roshan Mishra](https://github.com/Roshan2111-ACCA)
