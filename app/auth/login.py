from flask import Blueprint, render_template, redirect, request

login = Blueprint('login', __name__, template_folder="templates")

@login.route('/auth/login', methods=['GET', 'POST'])
def Login():
    return render_template('auth/login.html')