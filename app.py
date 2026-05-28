from flask import Flask, render_template, request
from word_counter import count_words, count_chars, most_common_word

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    text = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        if text.strip():
            results = {
                "words": count_words(text),
                "chars_with_spaces": count_chars(text, include_spaces=True),
                "chars_without_spaces": count_chars(text, include_spaces=False),
                "most_common": most_common_word(text),
            }
    return render_template("index.html", results=results, text=text)


if __name__ == "__main__":
    app.run(debug=True)
