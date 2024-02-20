# flask_blueprint

### Introduction
Register and Login/Logout page connect mySQL with flask, and seperate files with flask-blueprint firmwork

### File tree

``` bash
│  main.py
│  Pipfile
│  Pipfile.lock
│  README.md
│
└─user
    │  auth.py
    │  models.py
    │  views.py
    │  __init__.py
    │
    ├─static
    │  └─css
    │          style.css
    │
    └─templates
            login.html
            manage.html
            register.html
```

### Website process
register and confirm -> send data with flask -> sve into database(mySQL) -> client: it will jump to the login page, and then you can login with your username and password / auth: you can see all accounts data in manage page, and you can edit every account as well

### Password hashed
Use werkzeug hash function to make users' password hashed and secret.
You can see functions in __init__.py 

### RF
> 1. https://blog.csdn.net/m0_45319424/article/details/125574439
> 2. https://roytuts.com/delete-multiple-rows-from-table-using-flask-ajax-jquery-mysql/#google_vignette
> 3. https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2FSJmhFpXmf
> 4. https://medium.com/seaniap/python-web-flask-%E4%BD%BF%E7%94%A8%E9%9D%9C%E6%85%8B%E6%AA%94%E6%A1%88-ac00e863a470
> 5. https://ithelp.ithome.com.tw/articles/10185668