from flask import Blueprint, render_template, request, session
from db import Messages
from db.base import db

app = Blueprint('admin', __name__, template_folder='templates')

#Fix for accessing Admin previleges
@app.route("/admin", methods=["GET", "POST"])
def admin():
    try:
        isadmin = False
        if session['admin']:
            isadmin = True
        else:
            isadmin = False
        messages = Messages.query.all()
        return render_template(
            "admin.html",
            isadmin = isadmin,
            messages= messages
        )
        # cookies=request.cookies,
    except:
         return render_template('404.html')