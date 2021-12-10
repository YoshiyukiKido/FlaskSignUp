# Flask_loginとMySQLでログイン＋サインアップ機能

## migrate
cd LoginSample
python migration_kaiin_table.py

## execute (Windows)
cd ..
set FLASK_APP=LoginSample/__init__:create_app
flask run

## execute (Mac or Linux)
cd ..
export FLASK_APP=LoginSample/__init__:create_app
flack run
