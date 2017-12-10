from app import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from bson.objectid import ObjectId


class User(UserMixin):
    def __init__(self, uid, username, email):
        self.id = str(uid)
        self.username = username
        self.email = email

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


# Each time the logged in user navigates to a new page, it retrieves the ID of
# the user from the session, and then loads the user into memory
@login.user_loader
def load_user(uid):
    user = db.users.find_one({'_id': ObjectId(uid)})
    if not user:
        return None
    return User(user['_id'], user['username'], user['email'])
