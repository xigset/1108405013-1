from flask import Flask
from resource.user import users,user #把resource的users引渡到main.py
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
api.add_resource(users,"/users")
api.add_resource(user,"/user/<id>")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/test") #在網址後打的test
def test():
    return "test"

@app.route("/heyyou/<userid>")  #在網址後打的東西
def heyyou(userid):
    return "hey you {}".format(userid)

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host="0.0.0.0",port=5013)