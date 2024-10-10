from flask import render_template,request,flash,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user
from flask_admin import AdminIndexView

from models import User
from forms import RegistrationForm,LoginForm

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')

def register_routes(app,db,bcrypt):
    @app.route('/')
    def home():
        routes = ['register','login','logout','dashboard']
        return render_template('home.html',routes=routes)

    @app.route('/users')
    def users():
        users = User.query.all()
        return render_template('users.html',users=users)
    
    @app.route('/register',methods=['GET','POST'])
    def register():
        # Check if the user is already logged in
        if current_user.is_authenticated:
            flash(message='You Already Logged in',category='error')
            return redirect(url_for('home'))
        
        form = RegistrationForm()
        if request.method == 'POST':
            if form.validate_on_submit():  # Validate the form 
                username = form.username.data.strip().lower()
                email = form.email.data.strip().lower()
                password = form.password.data.strip()
                
                # Check if Username is Taken 
                existing_user = User.query.filter_by(name=username).first() 
                if existing_user:
                    flash(message='Username Taken!', category='error')
                    return redirect(url_for('register'))

                # Check if User exists by Email
                existing_user = User.query.filter_by(email=email).first()
                if existing_user:
                    flash(message='User already exists. Please login.', category='error')
                    return redirect(url_for('login'))
                
                # Hash the Password
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                
                # Create New User and Save to Database
                new_user = User(name=username,email=email,password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created successfully! You can now log in.', 'success')
                return redirect(url_for('login'))
            else:
                # If form validation fails, display errors
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error in {field}: {error}', 'error')

        return render_template('register.html', form=form)
        
        
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # Check if its logged in
        if current_user.is_authenticated:
            flash(message='You Already Logged in',category='error')
            return redirect(url_for('home'))
        
        form = LoginForm()
        
        if request.method == 'POST':
            if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data.strip().lower()).first()
                
                # Check if User is Already Logged In
                if user.is_logged:
                    flash(message='Account is Already Logged in',category='error')
                    return redirect(url_for('login'))
                
                # Check if the User exists and Password Incorrect
                if user:
                    if bcrypt.check_password_hash(user.password,form.password.data.strip()):
                        login_user(user)
                        user.is_logged = True
                        db.session.commit()
                        flash(message='Login successful!',category='success')
                        return redirect(url_for('dashboard'))
                else:
                    flash(message='Login unsuccessful. Please check your email and password.',category='error')
            else:
                # If form validation fails, display errors
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error in {field}: {error}', 'error')
                        
        return render_template('login.html',form=form)
        
    @app.route('/logout',methods=['GET','POST'])
    @login_required
    def logout():
        if request.method == 'POST':
            current_user.is_logged = False
            db.session.commit()
            logout_user()
            flash('You have been logged out.', 'success')
            return redirect(url_for('home'))
        
        return render_template('logout.html')
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html', username=current_user.name)
    
    @app.template_filter('title_')
    def title_(s):
        return str(s).title()
    
    