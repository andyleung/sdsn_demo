from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import subprocess
import time

app = Flask(__name__)
Bootstrap(app)

## def index():
##	output = subprocess.check_output("date", shell=True)
##	uptime = subprocess.check_output("uptime", shell=True)
##	return render_template('index.html',display_date=output,display_uptime=uptime)

@app.route('/')
@app.route('/sdsn')
def demo():
	return render_template('demo.html')

@app.route('/EX4200A_linkup')
def EX4200A_linkup():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic up -n vmnic2"
	output = subprocess.check_output(exsi_cli, shell=True)
	time.sleep(5)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -5 | tail -1 | awk \'{print $4}\'"
	vmnic2_output = subprocess.check_output(exsi_cli, shell=True)
	return render_template('EX4200A_linkup.html',display_status=vmnic2_output)

@app.route('/EX4200A_linkdown')
def EX4200A_linkdown():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic down -n vmnic2"
	output = subprocess.check_output(exsi_cli, shell=True)
	time.sleep(5)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -5 | tail -1 | awk \'{print $4}\'"
	vmnic2_output = subprocess.check_output(exsi_cli, shell=True)
	return render_template('EX4200A_linkdown.html',display_status=vmnic2_output)

@app.route('/EX4200B_linkup')
def EX4200B_linkup():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic up -n vmnic3"
	output = subprocess.check_output(exsi_cli, shell=True)
	time.sleep(5)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -6 | tail -1 | awk \'{print $4}\'"
	vmnic3_output = subprocess.check_output(exsi_cli, shell=True)
	return render_template('EX4200B_linkup.html',display_status=vmnic3_output)

@app.route('/EX4200B_linkdown')
def EX4200B_linkdown():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic down -n vmnic3"
	output = subprocess.check_output(exsi_cli, shell=True)
	time.sleep(5)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -6 | tail -1 | awk \'{print $4}\'"
	vmnic3_output = subprocess.check_output(exsi_cli, shell=True)
	return render_template('EX4200B_linkdown.html',display_status=vmnic3_output)

@app.route('/EX_status')
def EX_status():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -5 | tail -1 | awk \'{print $4}\'"
	vmnic2_output = subprocess.check_output(exsi_cli, shell=True)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -6 | tail -1 | awk \'{print $4}\'"
	vmnic3_output = subprocess.check_output(exsi_cli, shell=True)
	return render_template('EX_status.html',vmnic2=vmnic2_output,vmnic3=vmnic3_output)

@app.route('/status')
def status():
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -5 | tail -1 | awk \'{print $4}\'"
	vmnic2_output = subprocess.check_output(exsi_cli, shell=True)
        exsi_cli = "/usr/bin/sshpass -p \'8wry7Hxr\' ssh root@esxi-dell-1.kdc.jnpr.net esxcli network nic list | head -6 | tail -1 | awk \'{print $4}\'"
	vmnic3_output = subprocess.check_output(exsi_cli, shell=True)
	return jsonify({ 'name':'EX4200', 'status':vmnic2_output},{'name':'EX4300', 'status':vmnic3_output})

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
	

