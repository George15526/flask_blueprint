# flask_blueprint

Login/Logout page connect mySQL with flask, and seperate files with flask-blueprint firmwork

File tree:

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

> register and confirm -> send data with flask -> sve into database(mySQL) -> client: it will jump to the login page, and then you can login with your username and password / auth: you can see all accounts data in manage page, and you can edit every account as well