from admin import User, Admin, Privileges

administrator = Admin('Isabel', 'Ruiz', 'iris9112', 'iris@email.com', 'Colombia')
administrator.permissions.show_privileges()