from flask import Flask, request, render_template, redirect, session
import pymongo
from bson.objectid import ObjectId 
db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["Authentication"]

app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/', methods=['GET', "POST"])
def register():
    f_user = False
    f_pass = False
    f_pass2 = False
    f_email = False
    f_pass_m = False
    f_phone_l =False
    f_len = False
    if request.method == "POST" :
        form_data = dict(request.form)
        username = form_data["username"]
        password = form_data["pass"]
        password2 = form_data["pass2"]
        email = form_data["email"]
        phone = form_data["phone"]
        userName = db.users.find_one({"username": username})
        userEmail = db.users.find_one({"email": email})
        userPhone = db.users.find_one({"phone": phone})
        newUser = {"username": username, "password": password, "email": email, "phone": phone}
        if userName is not None:
            f_user = True
        if password != password2:
            f_pass_m = True
        if len(password) < 6:
            f_len = True
        if userEmail is not None:
            f_email = True
        if len(phone) != 11:
            f_phone_l = False

        # returen valuo
        if :
            return " User Already Exist "
        if f_pass_m == True:
            return "Password is not Match"
        if f_len == True:
            return "Enter more den 6 character !!"
        if f_email == True:
            return "Email Already Exist "
        if f_phone_l == True:
            return "Phone number is not have 11 digit"

        if f_user == True  and caseB == False  and caseC == False and caseD == False and caseBB == False:
            return "Email Already Exist "
        if caseA == False and caseB == False  and caseC == False and caseD == False and caseBB == False:
            return "Email Already Exist "
        if caseA == False and caseB == False  and caseC == False and caseD == False and caseBB == False:
            db.users.insert_one(newUser)
            return "Registration Successsfull"

    return render_template("register.html", **locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5009)
    #serve(app, host='127.0.0.1', port=5002)
    #serve(app, host='0.0.0.0', port=80)


