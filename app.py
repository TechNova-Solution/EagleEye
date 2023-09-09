from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, I am EagleEye a fraud detection!"