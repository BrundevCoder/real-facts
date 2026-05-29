from flask import Flask, jsonify
from flask_cors import CORS
from random import choice

app = Flask(__name__)
CORS(app)

schoolFacts = [
  "School is the best place in the world",
  "Homework is very fun!",
  "all schools were created by MrBeast",
  "You can run in the hallways"
]

codefacts = [
  "Python was created by Tim berners-Lee",
  "NVIDIA is the creator of Roblox",
  "JavaScript was created by McDonald's",
  "Google is a Game",
  "VS Code is where you buy games",
  "Discord is "
]

@app.route("/facts/<factType>")
def get_fact(factType):
  
  if factType == "all":
    return jsonify({"fact": choice(schoolFacts + codefacts)})
  elif factType == "school":
    return jsonify({"fact": choice(schoolFacts)})
  elif factType == "code":
    return jsonify({"fact": choice(codefacts)})

  return jsonify({"fact": "no fact selected"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)