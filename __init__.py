from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

from config import app_config

def create_app(config_name):
	app = Flask(__name__,instance_relative_config=True,template_folder="../app/templates")
	app.config.from_object(app_config[config_name])
	app.config.SECRET_KEY = 'cibicool'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql: // cr_admin@localhost/cr_db'
	db = SQLAlchemy(app)

	db.init_app(app)

	@app.route('/',methods=['GET','POST'])
	def hello_world():
		if request.method == 'POST':
			name=request.form["name"]
        		passw=request.form['psswd']
			if name=="cibi" and passw == "cibicool": 
				return render_template("dashboard.html",err="i")
			else:
				return render_template("dashboard.html",err="if")
		else:
			return render_template("dashboard.html",err="i")

	@app.route('/form',methods=['GET','POST'])
	def form():
		if request.method == 'POST' :
			student=db.db.student
			roll=request.form["roll_no"]
        		nam=request.form['name']
			total=request.form['total_mark']
			student.insert({"roll_no":roll,"name":nam,"total_mark":total})
			return redirect(url_for('hello_world'))
		else:
			return render_template("form.html")

	return app

