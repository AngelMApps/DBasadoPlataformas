from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurations 
app = Flask(__name__) #dander-name meta data
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:dev123@localhost:5432/dbp10'
db= SQLAlchemy(app)

#models
class Person(db.Model):
    ___tablename__='person'
    id=db.Column(
        db.Integer,
        primary_key=True
    )
    name=db.Column(
        db.String(),
        unique=True,
        nullable=False
    )
    
    def __repr__(self):
        return f'<User id={self.id}, name={self.name}>'
db.create_all()
#Controllers
@app.route('/')
def index():
    name='Angel'
    return f'Hello World {name}'

#run
if __name__ == '__main__':
    app.run(debug=True)