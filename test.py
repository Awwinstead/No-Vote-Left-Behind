from flask import Flask, render_template, flash, request, send_from_directory
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from secrets import token_urlsafe
import qrcode
import os
import requests 

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = os.path.join('qrcode')
website = "http://novoteleftbehind.tech/"

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        print (name)
    qr_filename = ""
    if form.validate():
        # Save the comment here.
        flash('Hello ' + name)
        user_token = token_urlsafe(32)
        full_site = website + "form?t=" + user_token
        img = qrcode.make(full_site)
        img = img.resize((240,240))
        img.save("qrcode/"+user_token+".png")
        qr_filename = os.path.join(app.config['UPLOAD_FOLDER'], user_token + ".png")
        send_to_db(name, user_token, email)
    else:
        # flash('Error: All the form fields are required. ')
        pass

    return render_template('hello.html', form=form, qr_image=qr_filename)
    
@app.route('/qrcode/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def send_to_db(name, user_token, email):
    r = requests.post(website + "json", data={'hhs_token':'[redacted]', 'user_token':user_token, 'name':name, 'email':email},headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("80"))