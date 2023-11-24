from flask import Flask
from public import public_var
from admin import admin
from user import user

app = Flask(__name__)
app.register_blueprint(public_var)
app.register_blueprint(admin)
app.register_blueprint(user)

app.secret_key="hihihi"

app.run(debug=True,port="5001") 