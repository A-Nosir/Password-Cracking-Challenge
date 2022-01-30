from flask import Flask, request, abort, render_template
from werkzeug.exceptions import HTTPException

from scripts.challenges import *;

app = Flask(__name__)

@app.route("/")
def index():
    f = open('./templates/challenges.json')
    challengesjson = json.load(f)
    f.close()
    return render_template('index.html', challenges=challengesjson)

@app.route("/challenge/<int:challenge_id>")
def challenge(challenge_id):
    f = open('./templates/challenges.json')
    challengesjson = json.load(f)
    f.close()
    return render_template('challengeTemplate.html', challenge=challengesjson[str(challenge_id)])

@app.route("/challenge/<int:challenge_id>/download")
def challenge_download(challenge_id):
    if validate_challenge_id(challenge_id) and download_request_valid(request):
        cnum = request.args['cnum'];
        challenge_data = get_challenge_data(challenge_id, cnum)
        if (challenge_data != None):
            return download_set(challenge_id, challenge_data)
        else:
            abort(500)
    else:
        abort(404)

@app.route("/challenge/<int:challenge_id>/login")
def challenge_login(challenge_id):
    if validate_challenge_id(challenge_id) and login_request_valid(request):

        cnum = request.args['cnum']
        username = request.args['username']
        password = request.args['password']
        
        return json.dumps({
            "passed" : validate_login_attempt(challenge_id, cnum, username, password)
        })
    else:
        abort(404)

@app.errorhandler(HTTPException)
def errorHandler(e):
    return str(e)

if (__name__ == "__main__"):
    app.run(debug = True)