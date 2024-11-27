import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


class Gmail:
    def __init__(self,whoami,app_pass,send_to,title,body,file_path):
        self.whoami = whoami
        self.app_pass = app_pass
        self.send_to = send_to
        self.title = title
        self.body = body
        self.msg = MIMEMultipart()
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.file_path = file_path

    def login(self):
        self.smtp.starttls()
        self.smtp.login(self.whoami, self.app_pass)

    def config_message(self):
        self.msg['From'] = self.whoami
        self.msg['To'] = self.send_to
        self.msg['Subject'] = self.title

        # Anexa o corpo do e-mail
        self.msg.attach(MIMEText(self.body, 'plain'))

    def attach_file(self):
        with open(self.file_path, 'rb') as anexo:
            # Cria um objeto MIMEBase
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())  # Lê o conteúdo do arquivo e anexa
            
            # Codifica o arquivo em base64
            encoders.encode_base64(part)
            
            # Define o cabeçalho do arquivo anexo
            part.add_header(
                'Content-Disposition',
                f'attachment; filename="{self.file_path.split("/")[-1]}"'
            )
            
            self.msg.attach(part)
            

    def send_email(self):
        try:
            self.smtp.sendmail(self.whoami, self.send_to, self.msg.as_string())
            print("Message sent")
        except:
            raise

