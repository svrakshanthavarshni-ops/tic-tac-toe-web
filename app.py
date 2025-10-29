from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play/<mode>/<int:size>")
def play(mode, size):
    # Get difficulty from URL (default = easy)
    difficulty = request.args.get("difficulty", "easy")
    return render_template("play.html", mode=mode, size=size, difficulty=difficulty)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
