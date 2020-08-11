from flask import Flask, render_template,url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return (render_template('Homepage.html'))

@app.route('/Alex')
def index():
	return (render_template('Homepage.html'))

if __name__ == '__main__':
	app.run(debug=True)
