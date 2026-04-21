from dotenv import load_dotenv
import os
import smtplib
load_dotenv()

def email(sender,reciever,app_password):
    subject="Stay Hydrated babeeee"
    word="As it is Summer, it is always good to be hydrated. "
    email_message = f"Subject: {subject}\n\n{word}"
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,app_password)
        server.sendmail(sender,reciever,email_message)
        server.quit()
        print("Emailed successfully !")
    except Exception as e:
        print(f"Error: {e}")


if __name__=='__main__':
    sender=os.environ.get("my_email")
    app_password=os.environ.get("password")
    email(sender,sender,app_password)

    
        
