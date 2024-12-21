from flask import render_template,jsonify,request,flash,url_for,redirect
from models import Person

def register_routes(app,db):
    
    @app.route('/')
    def home():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('home.html',people=people)
        
    @app.route('/transactions',methods=['POST'])
    def transactions():
        name = request.form['name'].strip()
        try:
            age = int(request.form['age'])
        except:
            age = 'None'
        try:
            salary = int(request.form['salary'])
        except:
            salary = 'None'
        '''
        action = request.form['action']
        if action == 'add':
            
            #flash('Person Added.')
        elif action == 'del':
            person = Person.query.filter(
                Person.name.like(f'{name}'),
                Person.age.like(age)
            )
            db.session.delete(person)
            #flash('Person Deleted.')
        '''
        action = request.form['action']
        if action == 'del':
                person = Person.query.filter_by(name=name, age=age,salary=salary).first()
                if person: 
                    db.session.delete(person)
                    flash('Person Deleted!')
                else:
                    flash('Unvalaible Person!!!')
        else:
            person = Person(name=name,age=age,salary=salary)
            db.session.add(person)
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/clear')
    def clear():
        db.session.query(Person).delete()
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/delete/<pid>',methods=['GET'])
    def delete(pid): 
        Person.query.filter(Person.pid==pid).delete()
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/details/<pid>',methods=['GET'])
    def details(pid): 
        person = Person.query.filter_by(pid=pid).first()
        return render_template('details.html',person=person)