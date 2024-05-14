import sqlalchemy
from flask_login import UserMixin
from app import app
db = sqlalchemy(app)

# Users Schema
class User(db.Model, UserMixin):
    """
        id: User Id, Integer Value
        UserName: Username, String Value
        Password: Password, Holds long Integer Values
    """
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(80), nullable=False)



# Contact Us Schema
class Contact(db.Model):
    """
        id: Contact ID, Integer Values
        FirstName: First Name field, String Value
        LastName: Last Name field, String Value
        Email: Email Address field, Strinf Value
    """
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(80), nullable=False)

# Blog Post Schema
class Blog(db.Model):
    """
    id: Auto Generated Integer ID, Auto_Increment in MySQL
    Title: String Values
    Contents: Holds the main content of the blog post
    PublishDate: Holds the Publish Date of the Blog post
    ModifiedDate: Hold the Date the Blog post changed by the User
    """
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Contents = db.Column(db.String(250), nullable=False)
    PublishDate = db.Column(db.Integer, nullable=False)
    ModifiedDate = db.Column(db.Integer, nullable=False)
    UserID = db.Column(db.Integer, foriegn_key=True)