from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Fruitscolor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(20))
    description = db.Column(db.String(120))

    def ___repr__(self):
        return f"{self.name} - {self.color} - {self.description}"



@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/fruitscolor')
def get_fruitscolor():
    fruits = Fruitscolor.query.all()
    output = []
    for fruit in fruits:
        fruit_data = {'name': fruit.name, 'color': fruit.color, 'description': fruit.description}
        output.append(fruit_data)
    return {"fruits": output}

@app.route('/fruitscolor', methods=['POST'])
def add_fruits():
    fruit = Fruitscolor(name=request.json['name'], color=request.json['color'], description=request.json['description'])
    db.session.add(fruit)
    db.session.commit()
    return {'id': fruit.id, 'name': fruit.name}


@app.route('/fruitscolor/<id>')
def get_fruitsid(id):
    fruit = Fruitscolor.query.get_or_404(id)
    return {"name": fruit.name, "color": fruit.color, "description": fruit.description}

@app.route('/fruitscolor/<id>', methods=['DELETE'])
def delete_fruit(id):
    fruit = Fruitscolor.query.get(id)
    if fruit is None:
        return {"error": "Fruit does not exist"}
    db.session.delete(fruit)
    db.session.commit()
    return {"message": "Yikes fruit deleted", 'id': fruit.id, 'name': fruit.name}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



