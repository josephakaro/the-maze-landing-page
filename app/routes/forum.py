from flask import Blueprint, render_template, redirect, request

forum = Blueprint('forum', __name__, template_folder="templates")

@forum.route('/community/forum', methods=['GET', 'POST'])
def Forum():
    return render_template('community/forum.html')