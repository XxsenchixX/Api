from flask import Flask,request
from Api import reverse,upper,rec,circle
import json

api = Flask(__name__)

@api.route("/reverse")
def get_reverse():
	string=request.args.get("string")
	data=reverse(string)
	text=data.get_text()
	return json.dumps({'result':text})

@api.route("/upper")
def get_upper():
	string=request.args.get("string")
	data=upper(string)
	text=data.get_text()
	return json.dumps({'result':text})

@api.route("/rec")
def get_rec():
	l=int(request.args.get("l"))
	w=int(request.args.get("w"))
	data=rec(l,w)
	answer=data.get_answer()
	return json.dumps({'result':answer})

@api.route("/circle")
def get_answers():
	r=int(request.args.get("r"))
	data=circle(r)
	area=data.get_area()
	per=data.get_per()
	return json.dumps({'area':area,'perimeter':per})

if __name__ == "__main__":
	api.run(host="127.0.0.1",port=5000)