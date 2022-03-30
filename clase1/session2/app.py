import email
from flask import Flask

app = Flask(__name__)
"""
class User():
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=True)
    email= db.Column(db.String(120),unique=True,nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
"""
@app.route('/')
def index():
    name='Angel'
    return f'Hello World {name}'

if __name__ == '__main__':
    app.run(debug=True)