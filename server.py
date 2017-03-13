from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import subprocess

app = Flask(__name__)
Bootstrap(app)

## def index():
##	output = subprocess.check_output("date", shell=True)
##	uptime = subprocess.check_output("uptime", shell=True)
##	return render_template('index.html',display_date=output,display_uptime=uptime)

@app.route('/')
@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.route('/EX4200A_linkup')
def EX4200A_linkup():
	output = subprocess.check_output("uptime", shell=True)
	return render_template('EX4200A_linkup.html',display_status=output)

@app.route('/EX4200A_linkdown')
def EX4200A_linkdown():
	output = subprocess.check_output("date", shell=True)
	return render_template('EX4200A_linkdown.html',display_status=output)

@app.route('/EX4200B_linkup')
def EX4200B_linkup():
	output = subprocess.check_output("uptime", shell=True)
	return render_template('EX4200B_linkup.html',display_status=output)

@app.route('/EX4200B_linkdown')
def EX4200B_linkdown():
	output = subprocess.check_output("date", shell=True)
	return render_template('EX4200B_linkdown.html',display_status=output)

@app.route('/EX_status')
def EX_status():
	output = subprocess.check_output("date", shell=True)
	return render_template('EX_status.html',display_status=output)

if __name__ == '__main__':
	app.run(debug=True)
	

