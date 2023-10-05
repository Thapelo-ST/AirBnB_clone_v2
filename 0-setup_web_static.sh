#!/usr/bin/env bash
# set up web servers for the deployment of web static

 sudo apt-get -y update

if ! command -v nginx &> /dev/null; then
        sudo apt-get -y install nginx
fi
sudo ufw allow 'Nginx HTTP' > /dev/null

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test

echo "<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>" | sudo  tee /data/web_static/releases/test/index.html > /dev/null

# sudo rm -rf /data/web_static/current

sudo ln -s -f /data/web_static/releases/test /data/web_static/current

config_file="/etc/nginx/sites-available/default"
sudo sed -i "\#listen 80 default_server#a \
location /hbnb_static/ {\
    alias /data/web_static/current/;\
}" "$config_file"
sudo service nginx restart
