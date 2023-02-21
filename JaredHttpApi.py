from flask import Flask
import random

app = Flask(__name__)

member_names = [
  "Jared",
  "Allan",
  "Andrew"
]

@app.route('/')
def display_member_name():
    index = random.randint(0, len(member_names) - 1)
    return "Member: " + member_names[index];

app.run(host = "0.0.0.0")