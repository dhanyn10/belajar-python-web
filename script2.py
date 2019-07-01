from flask import Flask

app = Flask(__name__)

#for index page
@app.route("/")
def home():
    return "index for main content here"

#for about page
@app.route("/about")
def about():
    return "about content here"

if __name__ == "__main__":
    app.run(debug=True)