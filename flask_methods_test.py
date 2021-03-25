from flask import Flask, render_template

# https://hackersandslackers.com/flask-routes/
app = Flask(__name__, template_folder="templates")

# methods enable which python can manage
@app.route("/", methods=['GET', 'POST', 'PUT'])
# name is given here

# accès par http://127.0.0.1:5000
# la page index3.html dans templates sera utilisée comme page index 
def home(name='Jean david FM'):
    """Serve homepage template."""
    return render_template("index3.html", name=name)  #name is passed as argument