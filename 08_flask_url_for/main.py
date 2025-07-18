from flask import Flask, render_template    

# app = Flask(__name__, static_url_path='/public') #this sets the static URL path
app = Flask(__name__, static_folder='assets', static_url_path='/public')  # this sets the static folder and URL path

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)