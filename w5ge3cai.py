
# flask

from flask import Flask, render_template, request, session, redirect, url_for
from importlib import reload
import requests

start = [13311,19968,63744,131072,173824,177984,178208,194995]
end = [19893, 40917, 64045, 173782, 177972, 178205,183969, 194998]
strokes_path = https://github.com/helmz/Corpus/blob/master/zh_dict/strokes.txt

def get_stroke(c):
    # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
    strokes = []
    with open(strokes_path, 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))

    unicode_ = ord(c)

    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        print("c should be a CJK char, or not have stroke in unihan data.")
        # can also return 0
        
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/w5ge3cai")
def w5ge3cai():
  return render_template("w5ge3cai.html")

@app.route("/danci")
def danci():  
  return render_template('danci.html',**{"data": data})

def main():
  c1 = input('Hi, please input your surname: ')
  c01 = get_stroke(c1)
  c2 = input('Hi, please input your First name: ')
  c02 = get_stroke(c2)
  c3 = input('Hi, please input your Middle name: . If none just input 0')
  c03 = get_stroke(c3)
  t0 = time.time()
  loct = time.localtime(t0)
  card = 0
  if (loct.tm_hour == 0 and loct.tm_min == 0 and   loct.tm_sec == 0):
    card = 0
  if card == 0:
    sched = BlockingScheduler()
    sched.add_job(func = CARD, trigger = 'cron', month = '*', day = '*', hour = '8', minute = '*', args=[card])
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '0-7', minute = '*')
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '9-23', minute = '*')
    card += 1
  if card > 0:  
    repeat()
  
