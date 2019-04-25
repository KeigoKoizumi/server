import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from flask import Flask, request, render_template

FROM_ADDRESS ='dustdetection707@gmail.com'
MY_PASSWORD ='3993lily'
TO_ADDRESS ='al16043@shibaura-it.ac.jp'
BCC = 'receiver2@test.net'
SUBJECT = 'Gmailでの数値送信'


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


app = Flask(__name__)
file_path = "./sensor_data.csv"
my_port = 16043
@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/dust', methods=['POST'])
def update_dust():
    time = request.form["time"]
    dust = request.form["dust"]
    try:
        to_addr = TO_ADDRESS
        subject = SUBJECT
        body =time+'・・・・・'+dust

        msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
        send(FROM_ADDRESS, to_addr, msg)
        print ("success")
        return "succeeded to send email"
    except Exception as e:
        print(e)
        return "failed to send email"
        
@app.route('/dust', methods=['GET'])
def get_dust():
    try:
        f = open(file_path, 'r')
        for row in f:
            dust = row
        return dust
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=my_port)