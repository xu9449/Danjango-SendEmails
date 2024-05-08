from django.core.mail import send_mail
from django.conf import settings
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

def sendInternalEmail(recipient_email, form_url):
    subject = "Complete Form for Data Processing"
    message = f"Click the link below to complete the form:\n\n{form_url}"
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, [recipient_email])

def sendData(recipient_email, data):
    subject = "This is the data you need"
    message = f"Below is the data you want:\n\n{data}"
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, [recipient_email])
    

    # # Email configuration
    # smtp_server = 'smtp.gmail.com'
    # smtp_port = 587
    # sender_email = 'bobangbiao@gmail.com'  # Your email address
    # password = 'qgtbrdrerbfycvzh'  # App-specific password generated for your Django application
    # recipient_email = 'xu9449@gmail.com'  # Recipient's email address

    # # Create a message
    # message = MIMEMultipart()
    # message['From'] = sender_email
    # message['To'] = recipient_email
    # message['Subject'] = 'Test Email'
    # body = 'This is a test email sent using Python SMTP.'
    # message.attach(MIMEText(body, 'plain'))

    # # Connect to the SMTP server
    # try:
    #     server = smtplib.SMTP(smtp_server, smtp_port)
    #     server.starttls()
    #     server.login(sender_email, password)
    # except Exception as e:
    #     print(f"Failed to connect to the SMTP server: {e}")
    # else:
    #     # Send the email
    #     try:
    #         server.sendmail(sender_email, recipient_email, message.as_string())
    #     except Exception as e:
    #         print(f"Failed to send the email: {e}")
    #     else:
    #         print("Email sent successfully.")
    #     finally:
    #         # Close the connection
    #         server.quit()

