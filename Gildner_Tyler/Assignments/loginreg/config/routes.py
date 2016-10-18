from system.core.router import routes
routes['default_controller'] = 'Welcome'
routes['POST']['/registration'] = 'Welcome#create_user'
routes['GET']['/loginpage'] = 'Welcome#loginpage'
routes['POST']['/login'] = 'Welcome#login'
routes['GET']['/congrats'] = 'Welcome#congrats'
routes['POST']['/logout'] = 'Welcome#logout'
