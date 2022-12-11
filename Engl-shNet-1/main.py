# Django

# flask

# tornado

from flask import Flask, render_template, request, session, redirect, url_for
from importlib import reload
import requests
import time
import sys
import re
import logging
import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler

def reject():
  print('It is not in the time for Recordıng!')

def repeat():
  print('You have recorded today!')

def CARD(card):   
  print('Welcome to extend the vocabulary!')
  card += 1
  return card

  
#创建flask duixiang
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'


#返回一些数据给浏览器
@app.route("/index")
def index():
  return render_template("index.html")
  
#qidong flask zijide fuwuqi
@app.route("/tran")
def tran():
  kd = request.args.get("kd")
  print(kd)
  #yunyong youdaozhiyun AI fanyi
  res = requests.post(
    "http://aidemo.youdao.com/trans",
    data={
      "q": kd.strip()  #jian zhi dui
    })
  ret = res.json()["basic"][
    "explains"]  #fan test.json zhong xunzhao n.pingguo suozai{{}}
  print(ret)  # print(res)
  return render_template("fanyi.html", **{
    "kd": kd,
    "ret": ret
  })

#** hou fanhui {}
@app.route("/beidanci")
def beidanci():  
  return render_template('beidanci.html')

#** hou fanhui {}
@app.route("/danci")
def danci(chapter):  
  conn = sqlite3.connect()  
  #buıld connector
  cursor = conn.cursor()  
  cursor.execute('select * from words where   chapter = chapter')
  data = cursor.fetchall()
  #print(data)
  return render_template('danci.html',**{"data": data})


# Details on the Secret Key: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.


@app.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to the session object
        session['email'] = request.form['email_address']
        return redirect(url_for('get_email'))

    return """
        <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
        """


@app.route('/get_email')
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """)


@app.route('/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return '<h1>Session deleted!</h1>'



@app.route("/daka")
def daka():
  t0 = time.time()
  loct = time.localtime(t0)
  if (loct.tm_hour == 0 and loct.tm_min == 0 and   loct.tm_sec == 0):
    card = 0
  if card == 0:
    sched = BlockingScheduler()
    sched.add_job(func = CARD, trigger = 'cron', month = '*', day = '*', hour = '8', minute = '*')
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '0-7', minute = '*')
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '9-24', minute = '*')
    card += 1
  if card > 0:  
    repeat()
  return render_template("index.html", **{
    "card": card,
    "loct": loct
  })


if __name__ == '__main__':
    app.run()
    
    

  
#pachong: daidianji
#F12 wangluo quanbu fanyidianji trans biaotou changgui fuzhi url

#qidong flask zijide fuwuqi bing huoqu IP, jinxing jishi
#peizhi logging and document and level
#logging.basicConfig(filename = 'logger.log', level = logging.INFO)
#@app.route("/timing")
#def check(str):
#  hasLogIn = '<button id ="login" class ="btn btn-success btn-flat">'
#  noLogged = '<a class ="btn btn-success btn-flat disabled" href="#">'
#  yes = re.search(hasLogIn, str)
#  if yes == None:
#    no = re.search(noLogged, str)
#    if no == None:
#      return -1 #nothing is found
#    else:
#      return 0 #'log error'is found
#  else:
#    return 1 #'log' is found

#def match(str):
#  res = r'<dl class = "dl-horizontal">(.*?)</dl>'
#  mm = re.findall(res, str, re.S | re.M)
#  res = r'<dd>(.*?)</dd>'
#  mm = re.findall(res, mm[0], re.S | re.M)
#  return mm
  
#reload(sys)
#email = '你的账号'
#password = '你的密码'
#remember_me = True 


#shezhi weichi cookie
#loginurl = 'http://ssr.0v0.loan/auth/login'

#@app.route("/")
#@app.route('/', methods =["GET", "POST"])
#ctx = app.test_request_context()
#ctx.push()
#app.preprocess_request()
#s = request.session()

#yng lai dai biaodan de canshu
#loginparams = {'email':email, 'passwd':password}
#'remember_me':remember_me }
# if request.method == "POST":
#       emaıl = request.form.get("email")
#       session['email'] = email
#r = request.session.post(loginurl, data = loginparams) 
#r = request.session().get(loginurl)
#res = check(r.content)
#if(res==1):  
#  loginUrl="http://ssr.0v0.loan/user/login"
#  r = request.session.post(loginUrl)
#  r = request.session.get(loginurl)
#lastWord = match(r.content)
#huoqu dangqian shijian
#nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#str = nowtime + ',\t总单词量：' + lastWord[0] + ',\t已背单词量：' + lastWord[1] + ',\t 剩余流量：' + lastWord[2]
#print(str)
#写入日志
#logging.info(str)


