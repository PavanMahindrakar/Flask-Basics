from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {
        "name": "john",
        "token": 50000
    }

    values = [1, data ]
    return jsonify(values)

if __name__ == '__main__':
    print("Visit http://localhost:5000/api/data in your browser or use curl to test the endpoint.")
    app.run(debug=True)