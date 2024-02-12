import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER,SMTP_PASSWORD

SMTP_HOST = "smtp.mail.ru"
SMTP_PORT = 465

celery = Celery("tasks", broker="redis://localhost:6379")


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = "Натрейдил Отчёт Дашборд"
    email["From"] = SMTP_USER
    email["To"] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчёт. Зацените 😉</h1>'
        '<img src="https://plecto-website-2020.s3.amazonaws.com/images/types_of_dashboard_fi.ecd'
        'c0cf6.fill-1200x625.format-jpeg.jpg" width="600">'
        '</div>',
        subtype = 'html'   
    )
    return email

@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        print(SMTP_PASSWORD)
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)