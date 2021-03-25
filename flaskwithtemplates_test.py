from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

@app.route("/")
@app.route("/test")
def home():
    """Serve homepage template."""
    return render_template("index2.html")