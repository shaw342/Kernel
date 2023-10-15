import sys
sys.path.append("database")
from sanic import Sanic,response,json
from sanic.response import text,html
from sanic_ext import render
from sanic_jinja2 import SanicJinja2
app = Sanic(__name__)
jinja = SanicJinja2(app, enable_async=True)
from script import Model



@app.route("/")
async def home(req):
    template = await jinja.render_async("home.html",req)
    return response.html(template.body)

@app.route("/logout",methods=["POST","GET"])
async def logout(req):
    template = await jinja.render_async("logout.html",req)
    return response.html(template.body)

@app.route("/register",methods=["POST"])
async def register(req):
    username = req.json.get("username")
    email = req.json.get("email")
    password = req.json.get("password")
    
    data = {
        username:username,
        email:email,
        password:password
    }
    try:
        Model.user_data(data)
    except Exception as e:
        raise (e)
    
    return response.html("<h1>connexion reussie</h1>")

if __name__ == "__main__":
    app.run(debug=True)