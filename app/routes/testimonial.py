from flask import Blueprint, render_template, redirect, request

testimonial = Blueprint('testimonial', __name__, template_folder="templates")

@testimonial.route('/community/testimonial')
def Testimonial():
    return render_template('community/testimonial.html')