from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    marks = {
        "John": 85,
        "Jix": 92,
        "Alice": 78,
        "Bob": 88,
    }
    return render_template("index.html", marks=marks)

if __name__ == "__main__":
    app.run(debug=True)