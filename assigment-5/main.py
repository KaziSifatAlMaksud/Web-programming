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
        if f_user == True  and f_pass_m == False  and f_len == False and f_email == False and f_phone_l == False:
            return "User Already Exist "
        if f_user == False  and f_pass_m == True  and f_len == False and f_email == False and f_phone_l == False:
            return "Password is not Match"
        if f_user == False  and f_pass_m == False  and f_len == True and f_email == False and f_phone_l == False:
            return "Enter more den 6 character !!"
        if f_user == False  and f_pass_m == False  and f_len == False and f_email == True and f_phone_l == False:
            return "Email Already Exist "
        if f_user == False  and f_pass_m == False  and f_len == False and f_email == False and f_phone_l == True:
            return "Mobile Number Already Exist "
        if f_user == True  and f_pass_m == True  and f_len == False and f_email == False and f_phone_l == False:
            return "User Already Exist <br/> Password is not Match"
        if f_user == True  and f_pass_m == False  and f_len == True and f_email == False and f_phone_l == False:
            return "User Already Exist <br/>Enter more den 6 character !!"
        if f_user == True  and f_pass_m == False  and f_len == False and f_email == True and f_phone_l == False:
            return "User Already Exist <br/>Email Already Exist "
        if f_user == True  and f_pass_m == False  and f_len == False and f_email == False and f_phone_l == True:
            return "User Already Exist <br/> Mobile Number Already Exist "
        if f_user == True  and f_pass_m == False  and f_len == False and f_email == True and f_phone_l == True:
            return "User Already Exist  <br/> Email Already Exist <br/> Mobile Number Already Exist "
        if f_user == True  and f_pass_m == False  and f_len == True and f_email == False and f_phone_l == True:
            return "User Already Exist <br/> Enter more den 6 character !! <br/> Mobile Number Already Exist  "
        if f_user == True  and f_pass_m == True  and f_len == False and f_email == False and f_phone_l == True:
            return "User Already Exist <br/> Password is not Match <br/> Mobile Number Already Exist"
        if f_user == False  and f_pass_m == True  and f_len == False and f_email == False and f_phone_l == True:
            return "Password is not Match <br/> Mobile Number Already Exist"
        if f_user == False  and f_pass_m == False  and f_len == True and f_email == False and f_phone_l == True:
            return "Enter more den 6 character !! <br/> Mobile Number Already Exist"
        if f_user == False  and f_pass_m == False  and f_len == False and f_email == True and f_phone_l == True:
            return "Email Already Exist <br/> Mobile Number Already Exist"
        if f_user == False  and f_pass_m == False  and f_len == True and f_email == True and f_phone_l == True:
            return "Enter more den 6 character !!<br/>Email Already Exist <br/> Mobile Number Already Exist"
        if f_user == True  and f_pass_m == True  and f_len == True and f_email == True and f_phone_l == True:
            return " User Already Exist <br/> Password is not Match <br> Enter more den 6 character !! <br/>Email Already Exist  <br/>  Mobile Number Already Exist "
        if f_user == True and f_pass_m == True and f_len == True and f_email == False and f_phone_l == True:
            return " User Already Exist<br/>Password is not Match<br> Enter more den 6 character !!<br/> Mobile Number Already Exist"
        if f_user == False and f_pass_m == False and f_len == True and f_email == True and f_phone_l == False:
            return " Enter more den 6 character !!<br/>Email Already Exist "
        if f_user == False and f_pass_m == True and f_len == False and f_email == False and f_phone_l == True:
            return " Password is not Match <br/> Mobile Number Already"
        if f_user == False and f_pass_m == True and f_len == False and f_email == True and f_phone_l == False:
            return " Password is not Match <br/> Email Already Exist"
        if f_user == False and f_pass_m == True and f_len == False and f_email == True and f_phone_l == True:
            return " Password is not Match <br/> Email Already Exist<br/> Mobile Number Already"
        if f_user == False and f_pass_m == True and f_len == True and f_email == True and f_phone_l == False:
            return " Password is not Match <br/> Email Already Exist"
        if f_user == False and f_pass_m == True and f_len == True and f_email == True and f_phone_l == False:
            return " Password is not Match <br> Enter more den 6 character !! <br/> Email Already Exist"
        if f_user == True and f_pass_m == True and f_len == True and f_email == True and f_phone_l == False:
            return "User Already Exist <br/> Password is not Match <br/> Enter more den 6 character !! <br/> Email Already Exist"
        if f_user == True and f_pass_m == True and f_len == True and f_email == False and f_phone_l == False:
            return " User Already Exist <br/>Password is not Match <br> Enter more den 6 character !!  "
        if f_user == True and f_pass_m == True and f_len == False and f_email == True and f_phone_l == True:
            return " User Already Exist <br/>Password is not Match <br> Email Already Exist<br> Mobile Number Already "
        if f_user == True and f_pass_m == True and f_len == False and f_email == True and f_phone_l == False:
            return " User Already Exist <br/>Password is not Match <br> Email Already Exist"
        if f_user == True and f_pass_m == False and f_len ==True and f_email == True and f_phone_l == False:
            return " User Already Exist <br> Enter more den 6 character !! <br> Email Already Exist "
        if f_user == True and f_pass_m == False and f_len ==True and f_email == True and f_phone_l == True:
            return " User Already Exist <br> Enter more den 6 character !! <br> Email Already Exist <br> Mobile Number Already "
        if f_user == False  and f_pass_m == False  and f_len == False and f_email == False and f_phone_l == False:
            db.users.insert_one(newUser)
            return "Registration Successsfull"

    return render_template("register.html", **locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=50001)
    #serve(app, host='127.0.0.1', port=5002)
    #serve(app, host='0.0.0.0', port=80)


