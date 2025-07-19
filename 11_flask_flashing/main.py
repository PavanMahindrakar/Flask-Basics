from flask import Flask, request, jsonify, render_template,flash

app = Flask(__name__)

app.secret_key = "sdv233bf26dfb2f3db2f"

@app.route('/')
def index():
    return render_template("index.html")    

@app.route('/logout')
def logout():
    flash("You have been logged out successfully!")
    return render_template("index.html")


if __name__ == '__main__':
    print("Visit http://localhost:5000/ in your browser to see the flash message functionality.")
    app.run(debug=True)