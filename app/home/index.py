from flask import Blueprint, render_template


index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
def Index():
	return render_template('home/index.html')