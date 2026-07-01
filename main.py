from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
import os
from dotenv import load_dotenv


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = os.getenv('SECRET')

@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")