import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(sender_email, password, receiver_email, subject, content):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    # MIME multipart message oluşturma
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # E-posta içeriği olarak HTML ekleme
    html_part = MIMEText(content, "html")
    msg.attach(html_part)

    # SMTP sunucusuna bağlanma ve e-postayı gönderme
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def confirm(sender_email, password, receiver_email):
    subject = "Kullanıcının Formu İncelendi - Sorunsuz Bulundu!"
    content = f"""\
        <html>
        <body>
            <p>Konu: Kullanıcının Formu İncelendi - Sorunsuz Bulundu!</p>
            <p>Merhaba Değerli Kullanıcı,</p>
            <p>Formunuz incelendi ve memnuniyetle bildirmek isteriz ki, gönderdiğiniz bilgilerde herhangi bir sorun bulunmamaktadır. Takdir edilesi titizlik ve düzenli bilgilendirme için teşekkür ederiz. Herhangi bir sorunuz veya ek talebiniz olduğunda bize ulaşmaktan çekinmeyin.</p>
            <p>İyi günler dileriz,</p>
            <p>FormülForum Ekibi</p>
        </body>
        </html>
    """
    sendEmail(sender_email, password, receiver_email, subject, content)

def reject(sender_email, password, receiver_email, article):
    subject = "Form İncelemesi Sonucu - Sorun Tespit Edildi"
    content = f"""\
    <html>
      <body>
        <p>Merhaba,</p>
        <p>Formunuz incelendi ve maalesef bir sorun tespit edildi. Size daha detaylı bilgi verebilmemiz için aşağıda belirtilen detaylarla ilgili olarak lütfen gönderdiğiniz metni kontrol edin:</p>
        <p><pre>{article}</pre></p>
        <p>Lütfen gerekli düzeltmeleri yapın ve tekrar gönderin. Herhangi bir sorunuz veya ek bilgiye ihtiyacınız varsa bize ulaşmaktan çekinmeyin.</p>
        <p>Teşekkürler,</p>
        <p>FormülForum Ekibi</p>
      </body>
    </html>
    """
    sendEmail(sender_email, password, receiver_email, subject, content)


def problem(sender_email, password, receiver_email, article_author):
    subject = "Form İncelemesi Sonucu - Tartışmalı Konu İçeren Gönderi"

    content = f"""\
    <html>
      <body>
        <p>Konu: Form İncelemesi Sonucu - Tartışmalı Konu İçeren Gönderi</p>
        <p>Merhaba,</p>
        <p>Forumumuzda <strong>{article_author}</strong> tarafından paylaşılan gönderiyi aşağıda bulabilirsiniz. Ancak, önemli bir bilgilendirme yapmak istiyoruz. Gönderide yer alan bazı noktalar halk arasında tartışma yaratabilecek potansiyele sahip olabilir. Bu tür konuları hoşgörülü bir şekilde ele almamız gerektiğini hatırlatmak istiyoruz.</p>
        <p>Lütfen gönderiyi dikkatlice inceleyin ve forum kurallarına uygun olduğundan emin olun. Herhangi bir sorunuz veya endişeniz varsa bize ulaşmaktan çekinmeyin.</p>
        <p>Teşekkürler,</p>
        <p>FormülForum Ekibi</p>
      </body>
    </html>
    """
    sendEmail(sender_email, password, receiver_email, subject, content)

def CheckEmail(sender_email, password):
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        context = ssl.create_default_context()

        # SMTP sunucusuna bağlanma ve kimlik doğrulama
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
        
        return True
    except Exception as e:
        return False
    
def MainMail(sender_email, password, receiver_email, article, article_author, status="confirm"):
    if status == "confirm":
        confirm(sender_email, password, receiver_email)
    elif status == "reject":
        reject(sender_email, password, receiver_email, article)
    elif status == "problem":
        problem(sender_email, password, receiver_email, article_author)