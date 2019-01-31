# -*- coding:utf-8 -*-
import traceback
import smtplib
from bson import ObjectId
from email.mime.text import MIMEText
from email.utils import make_msgid, formatdate
from email import encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
import os
import mimetypes

from nameko.dependency_providers import Config
from nameko.rpc import rpc

class EmailService:
    name = "emailService"

    # 配置文件
    config = Config()

    @rpc
    def send_mail(self, data):
        adr_from = self.config['SMTP_FROM']
        smtp_host = self.config['SMTP_HOST']
        smtp_port = self.config['SMTP_PORT']
        smtp_login = self.config['SMTP_LOGIN']
        smtp_password = self.config['SMTP_PASSWORD']
        subject = data['Subject']
        text = data.get('html', data.get('text'))
        adr_to = data.get('to')
        files = data.get('files', None)

        try:
            if smtp_port == 465:
                smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
            else:
                smtp = smtplib.SMTP(smtp_host, smtp_port)

            if smtp_login and smtp_password:
                smtp.login(smtp_login, smtp_password)

            if type(adr_to) in (list, tuple):
                adr_to = ','.join(adr_to)
            
            msg = self.as_rfc_message(subject, text, adr_from, adr_to, files)
            content = msg.as_string()
            smtp.sendmail(adr_from, adr_to, content) 
            smtp.quit()
            return True
        except Exception as e:
            traceback.print_exc()

    @rpc
    def as_rfc_message(self, subject, text, adr_from, adr_to, files):
        msg = MIMEMultipart()
        msg.attach(MIMEText(text, 'html', 'utf-8'))  

        msg['Subject'] = subject
        msg['From'] = adr_from
        msg['To'] = adr_to
        msg['Date'] = formatdate()
        msg['Reply-To'] = adr_from
        msg['Message-Id'] = make_msgid('unique-send')
        if type(files) in (tuple, list):
            for filename in files:
                with open(filename, 'rb') as f:
                    # judge the file type: text or other
                    mimetype, mimeencoding = mimetypes.guess_type(filename)
                    if mimeencoding or (mimetype is None):
                        mimetype = "application/octet-stream"
                    maintype, subtype = mimetype.split("/")

                    if maintype == "text":
                        retval = MIMEText(f.read(), _subtype = subtype)
                    else:
                        retval = MIMEBase(maintype, subtype)
                        retval.set_payload(f.read())
                        encoders.encode_base64(retval)
                    retval.add_header("Content-Disposition","attachment",filename = filename)
                    msg.attach(retval)
        return msg    
