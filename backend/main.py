from flask import Flask, jsonify
from flask_cors import CORS
from random import choice

app = Flask(__name__)
CORS(app)

schoolFacts = [
  "School is the best place in the world",
  "Homework is very fun!",
  "all schools were created by MrBeast",
  "You can run in the hallways",
  "We love tests/exams!"
]

techFacts = [
  "Python was created by Tim berners-Lee",
  "NVIDIA is the creator of Roblox",
  "JavaScript was created by McDonald's",
  "Google is a Game",
  "VS Code is where you buy games",
  "Discord is where you code",
  "WhatsApp was created by HackClub"
]

worldFacts = [
  "USA is in Europe",
  "Europe is a country",
  "Portugal is a continent",
  "Brazil is in Asia",
  "The Eiffel Tower is in Germany",
  "You can Buy a country",
  "The Moon costs like... $1 in sale"
]

@app.route("/facts/<factType>")
def get_fact(factType):
  
  if factType == "all":
    return jsonify({"fact": choice(schoolFacts + techFacts + worldFacts)})
  elif factType == "school":
    return jsonify({"fact": choice(schoolFacts)})
  elif factType == "tech":
    return jsonify({"fact": choice(techFacts)})
  elif factType == "world":
    return jsonify({"fact": choice(worldFacts)})

  return jsonify({"fact": "Fact Does Not Exist yet"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)