from flask import Blueprint, render_template, redirect, request

contact = Blueprint('contact', __name__, template_folder="templates")

@contact.route('/contact', methods=['GET', 'POST'])
def Contact():
    return render_template('contact/contact.html')