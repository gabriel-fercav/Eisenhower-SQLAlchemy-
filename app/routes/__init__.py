from flask import Flask
from app.routes.leads_blueprint import bp as bp_leads

def init_app(app: Flask):
    app.register_blueprint(bp_leads)