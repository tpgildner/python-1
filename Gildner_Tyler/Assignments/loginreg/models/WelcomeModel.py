from system.core.model import Model
import re

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def index(self):
        query = "SELECT * FROM users"
        users = self.models['WelcomeModel'].index()
        return self.load_view('index.html', users=users)

    def create_user(self, user):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not user['first_name']:
            errors.append('First name cannot be blank')
        elif len(user['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not user['last_name']:
            errors.append('Last name cannot be blank')
        elif len(user['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not user['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Email format must be valid!')
        if not user['password']:
            errors.append('Password cannot be blank')
        elif len(user['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif user['password'] != user['passconfirm']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}

        query = ("SELECT email FROM users WHERE email = :email")
        data = {'email' :user['email']}
        check = self.db.query_db(query, data)
        insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (:first_name, :last_name, :email, :password)"
        user = {'id': id, 'first_name': user['first_name'], 'last_name': user['last_name'], 'email': user['email'], 'password': self.bcrypt.generate_password_hash(user['password'])}

        self.db.query_db(insert_query, user)
        return {"status": True, "errors": errors}

        # test_password_1 = 'thisiswrong'
        # self.bcrypt.check_password_hash(pw_hash, test_password_1)
        # test_password_2 = 'password'
        # self.bcrypt.check_password_hash(pw_hash, test_password_2)
        # return redirect('/loginpage')

    def login(self, user):
        password = user['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': user['email']}
 # same as query_db() but returns one result
        user = self.db.get_one(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user.pw_hash, password):
                return user

        return False

    def keeploggedin(self):
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            user_data = {'email': user['email']}
            return self.db.get_one
