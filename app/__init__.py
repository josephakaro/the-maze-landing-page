from flask import Flask

app = Flask(__name__)

from app.auth import login
from app.home import index
from app.routes import about
from app.routes import contact
from app.routes import testimonial
from app.routes import forum
from app.routes import support
from app.routes import game
from app.routes import faqs

app.register_blueprint(login.login)
app.register_blueprint(index.index)
app.register_blueprint(about.about)
app.register_blueprint(contact.contact)
app.register_blueprint(testimonial.testimonial)
app.register_blueprint(forum.forum)
app.register_blueprint(support.support)
app.register_blueprint(game.game)
app.register_blueprint(faqs.faqs)
