from flask import Flask
app = Flask(__name__)

# la racine du serveur flask est à l'endroit du fichier python
@app.route('/')
# le répertoire test doit exister
@app.route('/test')
def hello_world():
    return 'Hello, World!'

'''
if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)
'''