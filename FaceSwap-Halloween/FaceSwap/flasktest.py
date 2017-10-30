from flask import Flask
app = Flask(__name__)
app.run(host='192.168.1.21')

@app.route("/")
def hello():
	return "Hello World!"
if __name__ == "__main__":
	app.run()