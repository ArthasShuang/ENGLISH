
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
  c = input('Hi, please input your name: ')
  c0 = get_stroke(c)
  
  
