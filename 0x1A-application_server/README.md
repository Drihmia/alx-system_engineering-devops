# **0x1A-application_server**


```bash
## for database :
echo "
export HBNB_ENV=dev
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db
" >>  ~/.bashrc && source ~/.bashrc
```

## task 3:
```bash
cd /home/ubuntu/AirBnB_clone_v2

tmux new-session -d ' gunicorn --bind 0.0.0.0:5001 web_flask.0-hello_route:app'
```


## task 4:
```bash
cd /home/ubuntu/AirBnB_clone_v3

tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
```

## task 5:
```bash
cd /home/ubuntu/AirBnB_clone_v4

tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'
```



## setting limit for user, can be done in two parts:

- 1st part:
    Open limits.conf file and use this syntax:
  ```bash
  sudo vim /etc/security/limits.conf
  ```

        
        <domain>      <type>  <item>         <value>

        #*               soft    core            0
        #root            hard    core            100000
        #*               hard    rss             10000
        #@student        hard    nproc           20
        #@faculty        soft    nproc           20
        #@faculty        hard    nproc           50
        #ftp             hard    nproc           0
        #ftp             -       chroot          /ftp
        #@student        -       maxlogins       4
        
 - 2nd part related to NGINX:
    Open default's NGINX's file and set ULIMIT to a high value:
    ```bash
    sudo vim /etc/default/nginx
    ```
    ```
    #  Example: ULIMIT="-n 4096
    ```



