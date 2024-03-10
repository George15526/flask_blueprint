from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
# from flask_login import current_user, login_required, login_user, logout_user
from . import db
from .models import Users
from .__init__ import set_password, check_password
from .email import send_email
from user.token import generate_token, confirm_token
from datetime import datetime

auth = Blueprint('auth', __name__)

# 主頁面歡迎函式，登入後會出現的主畫面
# @auth.route('/<username>', methods=['GET', 'POST'])
# def index(username):
#     return render_template('index.html', username=username)

# 登入函式
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        if request.values.get("login_submit") == 'login':
            login_username = request.form['username']
            login_password = request.form['password']
            
            user = Users.query.filter_by(username = login_username).first()
            
            if check_password(user, login_password):
                session['username'] = login_username
                flash('Login Success', 'success')
                return redirect(url_for('auth.index', username=login_username))
            else:
                flash('Login Failed, Please Check.', 'danger')
    return render_template('login.html')

# 登出按鈕函式，登出後會跳轉至登入頁面
@auth.route('/logout')
def logout():
    return render_template('login.html')

# 註冊函式，註冊完成會跳轉至登入頁面
@auth.route('/register2', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        
        if request.values.get("register_submit") == 'register':
        
            username = request.form['username']
            gender = request.form['gender']
            email = request.form['email']
            password = request.form['password']
            check_password = request.form['check_password']
            
            if check_password == password:
                
                new_user = Users(username=username, 
                                gender=gender,
                                email=email,
                                password_hashed=set_password(password)
                                )
            
                db.session.add(new_user)
                db.session.commit()
                
            
                subject = "Verify your account"
                token = generate_token(new_user.email)
                confirm_url = url_for("auth.confirm_email", token=token, _external=True)
                html = render_template("confirm_email.html", confirm_url=confirm_url)
                
                send_email(new_user.email, subject, html)
                
                response = make_response('Signup Success! Verify Email already been sent.', 'success')
                
                return response
            
            else:
                flash('Two password are not the same, please check!')
    
    return render_template('register.html')
                

# 後臺管理系統table展示頁面
@auth.route('/manage', methods=['GET', 'POST'])
def manage():
    query = Users.query.all()
        
    return render_template('manage.html', query=query)

# 後臺管理系統table的資料刪除函式
@auth.route('/delete_datas', methods=['GET', 'POST'])
def delete_datas():
    if request.method == 'POST':
        users = request.form.getlist("row_check")
        for i in users:
            user_id = int(i)
            delete_user = Users.query.filter_by(id=user_id).first()
            db.session.delete(delete_user)
            db.session.commit()
        
        if request.values.get("select_all") == "select_all":
            delete_users = Users.query.all()
          
    return redirect(url_for('auth.manage'))

# 驗證信箱連結啟動
@auth.route('/confirm/<token>')
def confirm_email(token):
    
    email = confirm_token(token)
    user = Users.query.filter_by(email=email).first_or_404()
    
    if user.is_confirmed:
        flash("Account already confirmed.", "success")
        return redirect(url_for("auth.login"))
    
    elif email == user.email:
        user.is_confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        response = make_response("You have confirmed your account. Thanks!", "success")
        return response
    
    else:
        flash("The confirmation link is invalid or has expired.", "danger")
    
    return redirect(url_for("auth.register"))

# 重新發送驗證碼
# @auth.route("/resend")
# @login_required
# def resend_confirmation():
#     if current_user.is_confirmed:
#         flash("Your account has already been confirmed.", "success")
#         return redirect(url_for("core.home"))
#     token = generate_token(current_user.email)
#     confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
#     html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
#     subject = "Please confirm your email"
#     send_email(current_user.email, subject, html)
#     flash("A new confirmation email has been sent.", "success")
#     return redirect(url_for("accounts.inactive"))