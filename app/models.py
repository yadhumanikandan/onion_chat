from app import db


#user table
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    # email = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))

    def __init__(self, username, password_hash):
        self.username = username
        # self.email = email
        self.password_hash = password_hash



# #admin table
# class admin(db.Model):
#     username = db.Column(db.String(20))
#     password_hash = db.Column(db.String(100))

#     def __init__(self, username, password_hash):
#         self.username = username
#         self.password_hash = password_hash
