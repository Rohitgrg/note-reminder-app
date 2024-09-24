import os
from datetime import datetime, timezone

from celery.schedules import crontab
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from flask_mail import Mail
from flask_cors import CORS

from project.utils import make_celery
from project.db import db
from project.error import CustomError
from project.routes.email_routes import email_routes
from project.routes.note_routes import notes_api, note_api
from project.routes.reminder_routes import reminder_api

load_dotenv()
mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    #celery
    app.config["CELERY_CONFIG"] = {"broker_url": os.getenv('REDIS_URL'), "result_backend": os.getenv('REDIS_URL'),"beat_schedule":{
        "every-one-hour":{
            "task" : "project.tasks.check_reminders_task",
            "schedule": crontab(minute="0"),
        }
    }}
    celery = make_celery(app)
    celery.set_default()

    # database
    db.init_app(app)
    migrate = Migrate(app, db)

    # mail config
    app.config['MAIL_SERVER']="smtp.gmail.com"
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
    mail.init_app(app)

    # resources
    api = Api(app)
    api.add_resource(CustomError, '/error')
    api.add_resource(notes_api, '/notes')
    api.add_resource(note_api, '/note/<int:pk>')
    api.add_resource(reminder_api, '/reminders')
    app.register_blueprint(email_routes)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"message": error.description}), 400

    return app, celery


