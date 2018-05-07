from flask import Flask, abort, url_for

app = Flask(__name__)

@app.route('/parse')
def parseAmostragem():
    return "Extraindo dados..."

app.run()