from flask import Flask, render_template, request
from mbta_helper import get_nearest_stop
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/find", methods=["POST"])
def find():
    place = request.form.get("place", "").strip()
    if not place:
        return render_template("index.html", error="Please enter a place name.")

    result = get_nearest_stop(place)

    if result.get("error"):
        return render_template("index.html", error=result["error"], place=place)

    return render_template("result.html", place=place, result=result,
                           mapbox_token=os.getenv("MAPBOX_TOKEN", ""))

if __name__ == "__main__":
    app.run(debug=True)
