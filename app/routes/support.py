from flask import Blueprint, render_template, redirect, request

support = Blueprint('support', __name__, template_folder="templates")

@support.route('/community/support', methods=['GET', 'POST'])
def Support():
    return render_template('community/support.html')