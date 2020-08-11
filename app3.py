from flask import Flask, url_for, request, render_template

app=Flask(__name__)
@app.route('/<V1>')
def hello(V1):
	return render_template('Homepage.html', name=V1)
if __name__=='__main__':
	app.run()
