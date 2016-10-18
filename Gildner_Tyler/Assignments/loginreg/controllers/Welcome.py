from system.core.controller import *
import re

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')

    def index(self):
        if 'user' in session:
            return redirect('/congrats')
        return self.load_view('index.html')

    def create_user(self):
        user = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': request.form['password'],
            'passconfirm': request.form['passconfirm']
        }
        create_status = self.models['WelcomeModel'].create_user(user)
        if create_status['status'] == False:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
        else:
            print 'HI!'
            return redirect('/loginpage')

    def loginpage(self):
        return self.load_view('login.html')

    def login(self):
        user_data = {
            'email': request.form['email'],
            'password': request.form['password'],
        }
        user = self.models['WelcomeModel'].login(user_data)
        if user:
            session['user'] = user[0]
            return redirect('/congrats')
        else:
            message = "Bad email / password combination"
            flash(message)
            return redirect('/loginpage')

    def congrats(self):
        return self.load_view('congrats.html')


    def logout(self):
        session.clear()
        return redirect('/')
