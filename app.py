from flask import Flask, render_template, request

app = Flask(__name__)

songs = {
    "pop": [
        "Shape of You",
        "Blinding Lights",
        "Butta Bomma",
        "Samajavaragamana",
        "Kesariya",
        "Tum Se Hi"
    ],

    "rock": [
        "Believer",
        "Thunder",
        "Saahore Baahubali",
        "Bulleya"
    ],

    "romantic": [
        "Perfect",
        "Priyathama Priyathama",
        "Tum Hi Ho",
        "Raabta"
    ],

    "party": [
        "Stay",
        "Oo Antava",
        "Ramuloo Ramulaa",
        "Kala Chashma"
    ],

    "sad": [
        "Someone You Loved",
        "Adiga Adiga",
        "Channa Mereya"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = []

    if request.method == "POST":
        genre = request.form["genre"].lower()

        if genre in songs:
            result = songs[genre]

    return render_template("index.html", songs=result)


if __name__ == "__main__":
    app.run(debug=True)