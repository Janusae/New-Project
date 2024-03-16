from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags


def Email_Funk(subject , to , context , template):
    try:
        html = render_to_string(template, context)
        plain_text = strip_tags(html)
        who = settings.EMAIL_HOST_USER
        send_mail(subject , plain_text , who  , [to], html_message=html)
        print("everything is successful")
    except Exception as e:
        print(e)