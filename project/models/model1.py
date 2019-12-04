from project import db


class Model1(db.Model):
    __tablename__ = "model1"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))

    def full_name(self):
        return f"{self.name} {self.surname}"
