from flask import Blueprint
from project.controllers.email_controller import EmailController

email_controller = EmailController()

email_routes = Blueprint('emails', __name__)

@email_routes.route('/send-email', methods=['POST'])
def send_email():
    return email_controller.send_email()