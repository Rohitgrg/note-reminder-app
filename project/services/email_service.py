from flask_mail import Message

class EmailService:
    def send_email(self, email, subject, body):
        from project import mail
        try:
            msg = Message(subject, recipients=[email])
            msg.body = body
            mail.send(msg)
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False