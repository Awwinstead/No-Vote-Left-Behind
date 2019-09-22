# HandHeldServer
# Kyle Stead /// kyle1elyk
# 2019-09-21

from flask import Flask

hhs = Flask(__name__)

@hhs.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    hhs.run(debug=True, host='0.0.0.0', port=int("80"))