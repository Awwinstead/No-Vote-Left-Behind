#importing all utilities we used, mysql connector, json config file, and flask
from flask import Flask, render_template, flash, request, send_from_directory
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from pdfMaker import main as pdfMaker

from datetime import datetime, date

import json
import mysql.connector
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a' 

with open('config.json') as config_file:
    cfg = json.load(config_file)

mydb = mysql.connector.connect(
                               host="localhost",
                               user=cfg['MYSQL_USER'],
                               passwd=cfg['MYSQL_PWD'],
                               database=cfg['MYSQL_DB']
)



@app.route('/json', methods = ['POST'])     #handles request sent from RasberryPI server
def postJsonHandler():
    user_token = request.form.get('user_token')
    hhs_token = request.form.get('hhs_token')
    name = request.form.get('name')
    email = request.form.get('email')
    key_hhs_token = cfg['HHS_TOKEN']
    
    if(key_hhs_token != hhs_token):         #if the token they submit does not match our token, reject the request
        return 'Error: key not valid'
    else:
        bigstrng = '{}\n{}\n{}'.format(user_token, name, email)
        print(bigstrng)
        mycursor = mydb.cursor(buffered=True)
        sql = "INSERT INTO Voters (`token`, `email`, `name`) VALUES (%s, %s, %s)"
        val = (user_token, email, name)
        mycursor.execute(sql, val)
        mydb.commit()                       #send it in to the db
    return 'Success!'
    
@app.route('/form', methods=['GET'])
def from_code():
    my_cursor = mydb.cursor(buffered=True)
    row_count = my_cursor.execute("SELECT `name` FROM Voters WHERE `token`=\"{}\"".format(request.args.get('t')))
    result = my_cursor.fetchone()
    if result:
        (name,) = result
        print(name)
        return "<meta http-equiv=\"refresh\" content=\"3; URL='https://sites.google.com/view/novoteleftbehind/home'\" /><b>Hello {}! Hang on a moment while we redirect you! If you are not redirected, <a href=\"https://sites.google.com/view/novoteleftbehind/home\">click here</a>".format(name)
    else:
        return "<meta http-equiv=\"refresh\" content=\"0; URL='/'\" />"


@app.route('/form2', methods=['POST'])
def from_google_site():
    today = date.today()
    data_dict = {
        'where applicable': 0,
        'New Registration': 1,
        'Record UpdateChange eg Address Party Affiliation Name Signature': "Yes",
        'Request to Replace Voter Information Card': 'On',
        'Are you a citizen of the United States of America': 'On',  # or NO
        'I affirm I have never been convicted of a felony': '1',
        'If I have been convicted of a felony I affirm my voting rights have been restored by': '1',
        'If I have been convicted of a felony I affirm my voting rights have been restored': '1',
        'I affirm that I have not been adjudicated': '1',
        'MM': '',
        'MM_2': '',
        'DD': '',
        'DD_2': '',
        'Y': '',
        'YY': '',
        'YYY': '',
        'YYYY': '',
        'FLFL': '',
        'FLFL_2': '',
        'FLFL_3': '',
        'FLFL_4': '',
        'FLFL_5': '',
        'FLFL_6': '',
        'FLFL_7': '',
        'FLFL_8': '',
        'FLFL_9': '',
        'FLFL_10': '',
        'FLFL_11': '',
        'FLFL_12': '',
        'FLFL_13': '',
        'SS': '',
        'SS_2': '',
        'SS_3': '',
        'SS_4': '',
        'Last Name': request.form['lastname'],
        'First Name': request.form['firstname'],
        'Middle Name': request.form['middlename'],
        'numbers': 'sr.',
        'Address Where You Live legal residenceno PO Box': request.form['currentaddress'],
        'AptLotUnit':'',
        'City': request.form['city1'],
        'County': request.form['state1'],
        'Zip Code': request.form['zipcode1'],
        'Mailing Address if different from above address': request.form['mailingaddress'],
        'AptLotUnit_2':'',
        'City_2': request.form['city2'],
        'County_2': request.form['state2'],
        'Zip Code_2': request.form['zipcode2'],
        'Address Where You Were Last Registered to Vote': request.form['lastvotingaddress'],
        'AptLotUnit_3':'',
        'City_3': request.form['city3'],
        'State': request.form['state3'],
        'Zip Code_3': request.form['zipcode3'],
        'Former Name if name is changed': request.form['formername'],
        'Gender':'',
        'State or Country of Birth': request.form['birthstate'],
        'Area Code':request.form['areacode'],
        'Telephone No Prefix': request.form['telePrefix'],
        'Telephone No Subscriber':request.form['teleSubscriber'],
        'undefined_2': '2',
        'Email me SAMPLE BALLOTS': 'Y',
        'Florida Democratic Party': 'Y',
        'Republican Party of Florida': '',
        'No party affiliation': '',
        'Minor party print party name': '',
        'American IndianAlaskan Native': '',
        'AsianPacific Islander': '',
        'Black not of Hispanic Origin': '',
        'Hispanic': 'Y',
        'White not of Hispanic Origin': '',
        'Multi-racial': "/On",
        'Other': '',
        'I am an active duty Uniformed Services or Merchant': True,
        'I am a spouse or a dependent of an active duty uniformed': True,
        'I am a US citizen residing outside the US': "Yes",
        'I will': 'Y',
        'I am': 'Y',
        'undefined_party': '',
        'undefined_Race': '',
        'SIGN MARK HERE': 'sdddd',
        'Signature': request.form['Signature'],
        'Date': today
    }
    pdfMaker(datetime.today().strftime("%Y%m%d%H%M%S"), data_dict)
    return "<a href=\""+datetime.today().strftime("%Y%m%d%H%M%S")+".pdf\">View file</a>"

@app.route('/')
def index():
    return "We are live"

    

app.run(host='0.0.0.0', port = 443, ssl_context=('cert.pem', 'key.pem'))
