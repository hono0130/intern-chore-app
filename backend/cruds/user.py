from db import session

from models.model import User
import schemas.user as user_scheme

#create
def create_user(user_info: user_scheme.SignUpUser):
    user = User()
    user.username = user_info.username
    user.email = user_info.email
    user.password = user_info.password

    session.add(user)
    session.commit()
    session.close

# Read
def get_user_by_email(email: str) -> user_scheme.UserUpdate:
    return session.query(User).filter(User.email == email).first()


def get_user_by_id(user_id: int) -> user_scheme.UserUpdate:
    return session.query(User).filter(User.user_id == user_id).first()


# Update
def update_user(user_id: int, user_info: user_scheme.UserUpdate):
    user = session.query(User).filter(User.user_id == user_id).first()
    user.username = user_info.username
    user.layout = user_info.layout
    user.gender = user_info.gender
    user.birthday = user_info.birthday
    session.commit()
    session.close()
