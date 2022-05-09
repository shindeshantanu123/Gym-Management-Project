from flask import *
from DBM import *

app = Flask(__name__)

@app.route("/")
def home():                            
    return render_template("home.html")

@app.route("/reg")
def register():                        
    return render_template("signup.html")

@app.route("/log")
def login():
    return render_template("login.html")

@app.route("/members")
def mem():
    return render_template("members.html")

@app.route("/adduser",methods=["post"])
def add_user():
    ids=request.form["id"]
    fullname=request.form["fullname"]
    contact=request.form["contact"]
    address=request.form["address"]
    username=request.form["username"]
    passw=request.form["passw"]

    t=(ids,fullname,contact,address,username,passw)
    adduser(t)
    return redirect("about")


@app.route("/validuser",methods=["post"])
def auth():
    username=request.form["username"]
    passw=request.form["passw"]
    t=(username,passw)
    authen=validuser()
    if (t in authen):
        return render_template("about.html")
    return redirect("log")


@app.route("/memberslist")
def memlist():
    data=alldata()
    return render_template("memberslist.html",elist=data)


@app.route("/addmem",methods=["post"])
def add_mem():
    name=request.form["name"]
    your_plan=request.form["your_plan"]
    contact=request.form["contact"]
    aadharcard_number=request.form["aadharcard_number"]
    age=request.form["age"]
    membership=request.form["membership"]
    t=(name,your_plan,contact,aadharcard_number,age,membership)
    addmem(t)
    return redirect("memberslist")


@app.route("/delete")
def dele():
    name=request.args.get("name")
    deldata(name)
    return redirect("memberslist")

@app.route("/edit")
def edit_mem():
    name=request.args.get("name")
    data=selectmembers(name)
    return render_template("update.html",row=data)

@app.route("/updatemembers" ,methods= ["post"])
def update_mem():
    name=request.form["name"]
    your_plan=request.form["your_plan"]
    contact=request.form["contact"]
    aadharcard_number=request.form["aadharcard_number"]
    age=request.form["age"]
    membership=request.form["membership"]    

    t=(name,your_plan,contact,aadharcard_number,age,membership)
    updatemembers(t)
    return redirect("memberslist")

@app.route("/about")
def aboutmem():
    return render_template("about.html")



if __name__ == "__main__" :
    app.run(debug=True)
    

























































    
    


