from flask import *


app = Flask(__name__)
@app.route("/")
def index():
    print request.headers
    return ""

app.run(host='0.0.0.0', port=9998, debug=True)
