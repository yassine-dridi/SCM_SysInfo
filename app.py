from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is a flask'

app.run('0.0.0.0', debug=True)