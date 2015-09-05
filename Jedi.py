from flask import Flask
import json

app = Flask(__name__)

@app.route("/jedi")
def say_hi():
    return "Welcome to the Jedi Council!"

@app.route("/firstname")
def first():
    firstn ={"firstname":['Arnold']}
    return json.dumps(firstn)

@app.route("/lastname")
def last():
    lastn ={"lastname":['Scwartzenagger']}
    return json.dumps(lastn)

@app.route("/jedi/<firstname>/<lastname>")
def hi_jedi(firstname, lastname):
    jediname = firstname[:3] + lastname[:2]
    html ="""
        <h1>
            Hello Jedi Master {}
        </h1>
        <p>
        </p>
        <img src="https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ytimg.com%2Fvi%2FXkFs0GpaV7I%2F0.jpg&f=1">
    """
    return html.format(jediname)


if __name__ == "__main__":
    app.run(host="0.0.0.0",
        port=8080)

