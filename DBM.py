import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='itv')

def adduser(t):
    db=getConnection()
    sql="insert into users values(%s,%s,%s,%s,%s,%s)"#--------->id,fullname,contact,address,username,passw
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def validuser():
    db=getConnection()
    sql="select username,passw from users"
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def addmem(t):
    db=getConnection()
    sql="insert into members values(%s,%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def alldata():
    db=getConnection()
    sql="select * from members"
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def deldata(t):
    db=getConnection()
    sql="delete from members where name=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def updatemembers(t):
    db=getConnection()
    sql="update members set your_plan=%s,contact=%s,aadharcard_number=%s,age=%s,membership=%s where name=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectmembers(name):
    db=getConnection()
    sql='select * from members where name=%s'
    cr=db.cursor()
    cr.execute(sql,name)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]















    
    





    
