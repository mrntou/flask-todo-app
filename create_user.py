from TODO.models import User,db

username = input('Username: ')
password = input('Password: ')

user = User(username=username)
user.set_password(password)
db.session.add(user)
db.session.commit()
print('Done!')