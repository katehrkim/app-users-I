from classes.app import App
from classes.users import User

test = App()
test.list_users()
user_one = {'name':'kate'}
user_one['email'] = 'katekim@gmail.com'
user_one['drivers_license'] = 'none'
test.add_user(user_one)
test.list_users()