from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "index home content here"

if __name__ == "__main__":
    app.run(debug=True)