from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = "john"
    token= 50000
    if "name" in request.args:
        name =  request.args["name"]
    if "token" in request.args:
        token = request.args["token"]
    return render_template("index.html", name=name, token=token)



if __name__ == '__main__':
    app.run(debug=True)