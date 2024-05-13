import smtplib, ssl

def  sendEmail(sender_email,receiver_email,password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receiver_email = receiver_email
    password = password

    // It's not automatic, might be changeable
    message = """\
    Subject: Hi there
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message),

sendEmail(#parameters)

// UTILS
// sender_email = "rsberkay123@gmail.com"  # Enter your address
// receiver_email = "231110053@stu.gedik.edu.tr"  # Enter receiver address
// password = input("Type your password and press enter: ")
