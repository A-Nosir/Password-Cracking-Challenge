from flask import send_file
import json
import io

from scripts import challenge_1
from scripts import challenge_2
#from scripts import challenge_3
from scripts import challenge_4
from scripts import challenge_5

def validate_challenge_id(challenge_id):
	return 1 <= challenge_id <= 5

def download_request_valid(request):
	if "cnum" not in request.args:
		return False
	else:
		cnum = request.args["cnum"]
		return cnum.isnumeric() and (99 < int(cnum) < 1000)

def login_request_valid(request):
	if "username" not in request.args or "password" not in request.args:
		return False
	else:
		return download_request_valid(request)

def download_set(challenge_id, data):

	data_string = "[\n"
	for dict in data:
		data_string += json.dumps(dict) + "\n"
	data_string += "]"

	download_file = io.BytesIO()
	download_file.write(data_string.encode())
	download_file.seek(0)
	
	return send_file(
		download_file,
		as_attachment = True,
		attachment_filename = 'challenge' + str(challenge_id) + '.txt',
		mimetype = 'text/txt'
	)

def get_challenge_data(challenge_id, cnum):
	if (challenge_id == 1):
		return challenge_1.get_challenge_set(cnum)
	if (challenge_id == 2):    
		return challenge_2.get_challenge_set(cnum)
	if (challenge_id == 4):
		return challenge_4.get_challenge_set(cnum)
	if (challenge_id == 5):
		return challenge_5.get_challenge_set(cnum)
	return None

def validate_login_attempt(challenge_id, cnum, username, password):
	if (challenge_id == 1):
		return challenge_1.validate_attempt(cnum, username, password)
	if (challenge_id == 2):
		return challenge_2.validate_attempt(cnum, username, password)
	if (challenge_id == 4):
		return challenge_4.validate_attempt(cnum, username, password)
	if (challenge_id == 5):
		return challenge_5.validate_attempt(cnum, username, password)
	return False