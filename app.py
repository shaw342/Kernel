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

@app.route("resgister",methods=["POST"])
async def register(req):
    data = req.json
    Model.user_data(data)
    return text("connexion reussie !")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)