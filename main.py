from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    vardai = ['Jonas', 'Antanas', 'Justinas', 'Gustavas']
    return render_template("index.html", sarasas=vardai)

if __name__ == "__main__":
    app.run(debug=True)
