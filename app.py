from flask import Flask, session
from db.base import db
from db import Transaction, Account, Admin
from db.base import db

from flask_migrate import Migrate

# Import views
from views.accounts import app as accounts_view
from views.base import app as base_view
from views.display import app as display_view
from views.admin import app as admin_view
from dotenv import load_dotenv          
import os                               

load_dotenv()

app = Flask(__name__)
app.register_blueprint(accounts_view)
app.register_blueprint(base_view)
app.register_blueprint(display_view)
app.register_blueprint(admin_view)

# Fix for Hardcoded passwords
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") 
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["DEBUG"] = True if os.getenv("DEBUG") == "True" else False 

db.init_app(app)
Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
    
    admin = db.session.query(Admin).filter_by(account_id= session["account_id"] ).first()
    session["admin"] = True if admin else False