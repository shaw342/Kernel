import sys
sys.path.append("database")
import sanic
from sanic import Sanic,response,json
from sanic_cors import CORS, cross_origin
from sanic.response import text,html
from sanic_ext import render
from sanic_jinja2 import SanicJinja2
from script import Model

app = Sanic(__name__)
CORS(app)
jinja = SanicJinja2(app, enable_async=True)



MODEL = Model()

@app.route("/")
async def home(req):
    template = await jinja.render_async("home.html",req)
    return response.html(template.body)

@app.route("/index.js")
async def index_js(req):
    return await response.file("templates/index.js")

@app.route("/image_home.jpg")
async def image(req):
    return await response.file("templates/img/image_home.jpg")

@app.route("/signin",methods=["POST","GET"])
async def signin(req):
    template = await jinja.render_async("signin.html",req)
    return response.html(template.body)

@app.route("/style.css",methods=["GET","POST"])
async def style(req):
    return await response.file("templates/style.css")

@app.route("/register",methods=["POST"])
async def register(req: sanic.Request):
    data = req.json
    
    if not MODEL.verification(data):
        return response.json({'error': 'among us exists'})
    
    MODEL.user_data(data)
    template =  await jinja.render_async("home.html",req)
    return response.html(template.body)

@app.route("/login.js")
async def login_js(req):
    return await response.file("templates/login.js")

@app.route("/login",methods=["POST","GET"])
async def login(req: sanic.Request):
    template =  await jinja.render_async("login.html",req)
    return response.html(template.body)

@app.route("/success", methods=["POST"])
async def login_success(req: sanic.Request):
    data = req.json
    if MODEL.confirmation_login(data.get('mail'),data.get('user')):
        return response.json({"error":"among us not exist"})
    template = await jinja.render_async("home.html",req)
    return response.html(template)




if __name__ == "__main__":
    app.run(debug=True)