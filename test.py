from flask import Flask
import requests


def api():
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id": "1178275040"}

    headers = {
        "x-rapidapi-key": "bc2dc6829emsha35bcaaebc4b1c9p15c439jsnf47640b4fca9",
        "x-rapidapi-host": "hotels4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api")
def api_endpoint():
    return api()


if __name__ == "__main__":
    app.run(debug=True)
