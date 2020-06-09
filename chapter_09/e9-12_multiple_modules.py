from user_class import User
from priveleges_admin import Admin, Privileges

administrator = Admin('Isabel', 'Ruiz', 'iris9112', 'iris@email.com', 'Colombia')
administrator.permissions.show_privileges()