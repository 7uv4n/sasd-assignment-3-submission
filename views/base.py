from flask import Blueprint, render_template, request, jsonify, send_from_directory
from datetime import datetime
import os
import json
from db import Messages, Admin
from db.base import db
from sqlalchemy import insert, text, delete


app = Blueprint('base', __name__, template_folder='templates')

@app.before_request
def setup_request():
    bod = None
    if "favicon.ico" in request.url:
        return
    if request.is_json:
        bod = request.get_json()
    if len(request.form):
        bod = request.form
    item = {
        "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "url": request.url,
        "args": str(request.args),
        "body": str(bod),
    }
    with open(f"{os.getcwd()}/logs/access.log", "a") as fp:
        json.dump(item, fp)
        fp.write("\n")


@app.route("/")
def index():


    """
    # Commands to create the tables if it does not exist, manually add admins and delete all messages 

    db.create_all()
    # Manually make Carter an admin by inserting account_id as 1
    manual_admin = insert(Admin).values(account_id=1)
    db.session.execute(manual_admin)
    db.session.commit()

    # Manually adding admin by inserting account_id as 6
    manual_admin = insert(Admin).values(account_id=6)
    db.session.execute(manual_admin)
    db.session.commit()
    new_message = Messages(account_id='%')   

    # Manually adding an admin by inserting account_id as 7
    manual_admin = insert(Admin).values(account_id=7)
    db.session.execute(manual_admin)
    db.session.commit() 
    
    # Delete all messages from messages Table
    db.session.query(Messages).delete()
    db.session.commit()
    """
    

    return render_template("index.html")

# Send the static content like CSS and JS
@app.route('/s/<path:path>')
def send_stylesheet(path):
    dirname = os.path.dirname(path)
    if not dirname:
        dirname = f"{os.getcwd()}/templates/static"
    else:
        if not dirname.startswith("/"): 
            dirname = f"/{dirname}"
    filename = os.path.basename(path) 
    return send_from_directory(dirname, filename) 


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template("500.html"), 500

# Fix for Command Injection Vulnerability
# @app.route("/json/test")
# def extra_flag():
#     if not request.args.get("cmd", False):
#         return jsonify({})
#     arguments = str(request.args.to_dict())
#     resp = os.popen(json.loads(arguments.replace("'", '"'))["cmd"]).read()
#     return jsonify({"response": resp})