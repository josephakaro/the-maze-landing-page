from flask import Blueprint, render_template, redirect, request

game = Blueprint('game', __name__, template_folder="templates")

@game.route('/game', methods=['GET', 'POST'])
def Game():
    return render_template('games/games.html')