from flask import Flask     #importing all utilities we used, mysql connector, json config file, and flask
from flask import request

import json
import mysql.connector
app = Flask(__name__)

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
        mycursor = mydb.cursor()
        sql = "INSERT INTO Voters (`token`, `email`, `name`) VALUES (%s, %s, %s)"
        val = (hhs_token, email, name)
        mycursor.execute(sql, val)
        mydb.commit()                       #send it in to the db
    return 'Success!'

app.run(host='0.0.0.0', port = 5000)
