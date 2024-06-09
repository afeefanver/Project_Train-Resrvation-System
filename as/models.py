from app import db
from database import User, Train, Reservation

def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_train(name, schedule):
    train = Train(name=name, schedule=schedule)
    db.session.add(train)
    db.session.commit()
    return train

def create_reservation(user, train, date):
    reservation = Reservation(user_id=user.id, train_id=train.id, date=date)
    db.session.add(reservation)
    db.session.commit()
    return reservation
