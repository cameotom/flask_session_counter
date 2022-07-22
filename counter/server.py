from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret' # set a secret key for security purposes

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route("/show")
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

