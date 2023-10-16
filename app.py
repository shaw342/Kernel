import sys
sys.path.append("database")
import sanic
from sanic import Sanic,response,json
from sanic_cors import CORS, cross_origin
from sanic.response import text,html
from sanic_ext import render
from sanic_jinja2 import SanicJinja2
app = Sanic(__name__)
CORS(app)
jinja = SanicJinja2(app, enable_async=True)


from script import Model

MODEL = Model()

@app.route("/")
async def home(req):
    template = await jinja.render_async("home.html",req)
    return response.html(template.body)

@app.route("/index.js")
async def index_js(req):
    return await response.file("templates/index.js")

@app.route("/signin",methods=["POST","GET"])
async def logout(req):
    template = await jinja.render_async("signin.html",req)
    return response.html(template.body)

@app.route("/register",methods=["POST"])
async def register(req: sanic.Request):
    data = req.json
    
    if not MODEL.verification(data):
        return response.json({'error': 'among us exists'})
    
    MODEL.user_data(data)
    
    return response.json({'message': 'Received JSON data', 'data': data})

if __name__ == "__main__":
    app.run(debug=True)