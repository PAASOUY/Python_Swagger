from flask import Flask,request;

tblproduct=[
    {"id":1,"name":"abc","price":2},
    {"id":2,"name":"anchor","price":21},
    {"id":3,"name":"hanuman","price":24}
]

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return "Welcome Flask!"

@app.route('/r001',methods=['POST'])
def getjson():
    lst=["male","female"]
    resp={"cd":"001","sms":"error field!","data":lst}
    return resp;

@app.route('/r002',methods=['POST'])
def searchProductById():
    try:
        body = dict(request.json)
        id = body["id"]
        for itm in tblproduct:
            if (itm['id'] == id):
                resp = {'cd': "000", "sms": "Success!", "data": itm}
                return resp;

        return {"cd": "888", "sms": "not found!", "data": {}};
    except Exception as ex:
        return {"cd":"999","sms":"unhandle error!","data":{}};

@app.route('/r003',methods=['POST'])
def searchUserById():
    import psycopg2
    try:
        body = dict(request.json)
        uid = body["uid"]
        from psycopg2.extras import DictCursor;
        con = psycopg2.connect(database="st1112db", user="postgres",
                               password="123456", host="127.0.0.1", port="5433")
        cur = con.cursor(cursor_factory=DictCursor)
        cur.execute("select * from usr.tbluser where uid=%s"
                    ,
                    (uid,)
                    )

        if(cur.rowcount>0):
            dr = cur.fetchone();
            resp = {'cd': "000", "sms": "Success!", "data": dr}
            return resp;
        else:
            return {"cd": "888", "sms": "not found!", "data": {}};
    except Exception as ex:
        return {"cd":"999","sms":"unhandle error!","data":{}};

app.run(port=9089)