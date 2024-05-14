from flask import Blueprint, render_template, redirect, request

faqs = Blueprint('faqs', __name__, template_folder="templates")

@faqs.route('/faqs', methods=['GET', 'POST'])
def Faqs():
    return render_template('faqs/faqs.html')