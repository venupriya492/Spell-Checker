from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""
    original_text = ""
    if request.method == "POST":
        original_text = request.form["text"]
        blob = TextBlob(original_text)
        corrected_text = str(blob.correct())
    return render_template("index.html", original=original_text, corrected=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)
