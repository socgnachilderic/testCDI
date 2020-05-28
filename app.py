from flask import Flask, render_template


app = Flask(__name__)


# aaaa
def generate_list():
    return [f"liste {i}" for i in range(1, 5)]


@app.route("/")
def home():
    return render_template("index.html", lists=generate_list())


if __name__ == '__main__':
    app.run(debug=True)
