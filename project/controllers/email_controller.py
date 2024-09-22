from flask import jsonify
from flask_restful import abort

from project.services.email_service import EmailService


class EmailController:
    def __init__(self):
        self.service = EmailService()

    def send_email(self):
        recipient = 'rohitgrg75@gmail.com'
        subject = 'Test from project'
        body = 'Test from project'
        success = self.service.send_email(recipient, subject, body)
        if success:
            return jsonify({"message": "Email sent successfully."}), 200
        else:
            abort(500, message="Failed to send email.")