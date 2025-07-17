from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        with open("data.txt", "w") as f:
            f.write(f"Name: {request.form['name']}\n")
            f.write(f"Email: {request.form['email']}\n")

        return render_template("contact.html")
    
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)