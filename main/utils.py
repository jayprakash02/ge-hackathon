from .models import User
from cryptography.fernet import Fernet

#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

def get_user(signature):
    for u in User.objects.all():
        if u.verify(signature):
            return u
    return None

