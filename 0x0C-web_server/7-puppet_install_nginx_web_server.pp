# Using Puppet

exec { 'Install nginx':
  command  => "sudo apt-get -y update && sudo apt-get -y install nginx && echo 'Holberton School' > sudo /var/www/html/index.html && sudo sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://calypsobronte.me/ permanent;' /etc/nginx/sites-available/default && sudo service nginx restart",
  provider => 'shell',
}
