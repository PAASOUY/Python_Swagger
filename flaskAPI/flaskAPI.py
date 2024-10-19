from flask import Flask,request;
from psycopg2.extras import DictCursor;
import psycopg2

app=Flask(__name__)

@app.route('/home',methods=['GET','POST'])
def home():
    return "Welcome Flask!"

@app.route('/r1',methods=['GET','POST'])
def login():
    try:
        body = dict(request.json)
        uname = body["uname"]
        upass = body["upass"]
        con = psycopg2.connect(database="flaskapi", user="postgres",
                               password="123", host="127.0.0.1", port="5432")
        cur = con.cursor(cursor_factory=DictCursor)
        cur.execute("select * from usr.tbluser where uname=%s and upass=%s" ,(uname,upass))

        if(cur.rowcount>0):
            dr = cur.fetchall();
            resp = {'cd': "000", "sms": "Success!", "data": dr}
            return resp;
        else:
            return {"cd": "888", "sms": "not found!", "data": {}};
    except Exception as ex:
        return {"cd":"999","sms":"unhandle error!","data":{}};
app.run(port=9089)