import os
os.system("rm db.sqlite3")
os.system("python3 manage.py makemigrations rare_rest_api")
os.system("python3 manage.py migrate")
os.system("python3 manage.py loaddata categories comments posts rare_user subscriptions tags tokens users")

