from static_data import db as database


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(64), index=True, unique=True)
    password_hash = database.Column(database.String(128))
    first_name = database.Column(database.String(64))
    last_name = database.Column(database.String(64))
    sure_name = database.Column(database.String(64))
    number = database.Column(database.String(1))
    gender = database.Column(database.String(64))

    def __repr__(self):
        return '{}'.format(self.username)
