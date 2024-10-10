from app import db

class Person(db.Model):
    __tablename__ = 'people'
    
    pid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    def __repr__(self):
        return f'Person{self.pid} with {self.name} and {self.age} and with salary of {self.salary} '