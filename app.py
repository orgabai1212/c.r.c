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
    if request.method == 'POST':
      id = request.form.get('id')
      first_name=request.form.get('first_name')
      last_name=request.form.get('last_name')
      sql_insert(id,first_name,last_name)
      return  "criminal added"
    return render_template("add.html")

#get all criminal list im db
@app.route('/all',methods=['GET'])
def all():
  result =sql_command("select * from criminals;")
  return jsonify(result)


#serch for Specific criminal in db
@app.route('/find',methods=['GET','POST'])
def find():
  if request.method == 'POST':
    check_id= request.form.get('id')   
    command =f"select id,first_name,last_name from criminals where id ={check_id};"
    criminal=sql_command(command)
    return jsonify(criminal)
  return render_template("find.html")
  



@app.route('/delete',methods=['GET','POST'])
def delete():
  if request.method == 'POST':
    criminal_to_rm=request.form.get('id')
    sql_delete(criminal_to_rm)
    return "criminal removd"
  return render_template("delete.html")
 



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)