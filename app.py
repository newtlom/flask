from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
	return "Home"


@app.route('/')
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
#로컬이라 포트만, 시작할때 app.py이름을찾기때문에.
