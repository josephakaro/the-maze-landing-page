from flask import Blueprint, render_template, redirect, request

login = Blueprint('login', __name__, template_folder="templates")

Users = {
    1:{
        "Email": "josephmmakaro@gmail.com",
        "Password": "Jubatech@2%"
    },
    2:{
        "Email": "ukothjosephakaro@gmail.com",
        "Password": "Jubatech@2"
    },
    }

@login.route('/auth/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        for i in Users:   
            if email == Users[i].Email and password == Users[i].Password:
                return "Success!"
            else:
                return "Access Denied!"
            user + 1
    return render_template('auth/login.html')