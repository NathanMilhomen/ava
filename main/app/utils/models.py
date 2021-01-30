from main.app import db


def save_model(model: db.Model):

    db.session.add(model)
    db.session.commit()


def delete_model(model: db.Model):

    db.session.delete(model)
    db.session.commit()
