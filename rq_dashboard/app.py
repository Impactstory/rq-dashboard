from flask import Flask
from rq_dashboard import RQDashboard
import os


app = Flask(__name__)

if os.getenv('RQ_DASHBOARD_SETTINGS'):
    app.config.from_envvar('RQ_DASHBOARD_SETTINGS')

app.config['REDIS_DB'] = 3
app.config['REDIS_URL'] = os.getenv("REDIS_URL")

RQDashboard(app, '')
