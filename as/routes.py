from app import app, db
from database import User, Train, Reservation
from app.database import create_user, create_train, create_reservation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Create a new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        # Redirect to the login page
        flash('User account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    # If the request method is GET, show the signup form
    return render_template('signup.html')

