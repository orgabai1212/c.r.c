from flask import Flask,request,jsonify,render_template,flash
import mysql.connector
import time


app = Flask(__name__)
#conet to mysql
def connect():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crc",
    port="3306"
    )
#a sql command function (work only to get information and not for changes in the db)
def sql_command(command):
    conection =connect()
    cursor = conection.cursor()
    cursor.execute(command)
    result=cursor.fetchall()
    cursor.close()
    conection.close()
    return result

#the insert function
def sql_insert(id,first_name,last_name):
    conection =connect()
    cursor = conection.cursor()
    qury="insert into criminals (id,first_name,last_name) values (%s,%s,%s)"
    values=(id,first_name,last_name)
    cursor.execute(qury,values)
    conection.commit()
    cursor.close()
    conection.close()

def sql_delete(id):
  conection=connect()
  cursor = conection.cursor()
  qury=f"delete from criminals where id = {id};"
  cursor.execute(qury)
  conection.commit()
  cursor.close()
  conection.close()



@app.route('/')
def welcom():
  return render_template("index.html")

#insert a new criminal in db
@app.route('/add',methods=['POST','GET'])
def add():
    # data = request.get_json()
    # id = data['id']
    # first_name = data['first_name']
    # last_name = data['last_name']
    id = request.form.get['id']
    first_name=request.form.get['first_name']
    last_name=request.form.get['last_name']
    render_template("index.html")
    sql_insert(id,first_name,last_name)
    return  f"ID: {id}<br>First Name: {first_name}<br>Last Name: {last_name}"

#get all criminal list im db
@app.route('/all',methods=['GET'])
def all():
  result =sql_command("select * from criminals;")
  return jsonify(result)


#serch for Specific criminal in db
@app.route('/find',methods=['GET'])
def find():
  check_id= request.args.get('id')   
  command =f"select id,first_name,last_name from criminals where id ={check_id};"
  criminal=sql_command(command)
  #criminal became a list 
  if len(criminal)==0:
    return "criminal not found"
  else:
    return jsonify(criminal)



@app.route('/delete',methods=['GET'])
def delete():
  criminal_to_rm=request.args.get('id')
  check_before=sql_command("select * from criminals;")
  print(len(check_before))
  sql_delete(criminal_to_rm)
  time.sleep(5)
  print(len(check_after))
  check_after=sql_command("select * from criminals;")
  if len(check_before)==len(check_after):
    
    return "wrong id"
  else:
    return "criminal removed"



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)