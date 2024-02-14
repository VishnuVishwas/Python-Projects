from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class SimpleForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')

@app.route('/', methods=['GET', 'POST'])
def simple_form():
    form = SimpleForm()

    if form.validate_on_submit():
        pass

    return render_template('simple_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)