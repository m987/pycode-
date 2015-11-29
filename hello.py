from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/kot')
def kot():
	return 'KOT!!!'

@app.route('/potega/<int:a>')
def potega(a):
	return str(a*a)

if __name__ == '__main__':
    app.run()