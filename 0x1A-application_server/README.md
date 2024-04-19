0x1A-application_server


for database :
echo "
export HBNB_ENV=dev
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db
" >>  ~/.bashrc && source ~/.bashrc

task 3:
cd /home/ubuntu/AirBnB_clone_v2
tmux new-session -d ' gunicorn --bind 0.0.0.0:5001 web_flask.0-hello_route:app'

task 4:
cd /home/ubuntu/AirBnB_clone_v3
tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'

task 5:
cd /home/ubuntu/AirBnB_clone_v4
tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'
