# Fix for admin previleges
from db.base import db
# Database Admin
class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, unique=True, nullable=False)