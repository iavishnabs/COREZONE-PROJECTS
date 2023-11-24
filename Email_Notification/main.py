from flask import *
from admin import admin


app = Flask(__name__) 
app.register_blueprint(admin)


app.run(debug=True,port="5003")