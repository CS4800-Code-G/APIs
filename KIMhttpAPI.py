from flask import Flask
#from flask_cors import CORS
#import pymongo



app = Flask(__name__)


@app.route('/home')
def home():
    return "Main Home Page. Welcome!"

@app.route('/')
def hello():
    return 'Hello, World!'





app.run(host = "0.0.0.0")