from flask import Flask, request
from Feynman import Feynman 
from flashcards import Flashcards
#using json files:

#app is taking the name of __name__, which is any name
app = Flask(__name__)

#remember that @app.route is a decorator that makes the function hello_world() run inside the function @app.route()
@app.route("/")
def hello_world():
    return "Hi"

#rest api.
@app.route("/penpal")
def second_page():
    # transcript = request.args.get("transcript")
    # instead of doing this, since aly is not happy, I will be taking in the body of the request, which is a json
    json = request.get_json()
    transcript = json["transcript"]
    return Feynman(transcript)

@app.route("/flashcards")
def third_page():
    # transcript = request.args.get("transcript")

    #extracts the json from the body of the POST
    transcript = request.get_json()
    return Flashcards(transcript)

if __name__ == '__main__':
    app.run(debug=True)

