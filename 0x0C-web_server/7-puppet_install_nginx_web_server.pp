# Nginx should be listening on port 80


package {'nginx':
  ensure => installed,
}
file {'/var/www/html/index.html':
  content => 'Hello World!',
}
file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index  index.html index.htm index.nginx-debian.html ;

	server_name _;
	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
		internal;
		}

	location / {
		try_files \$uri \$uri/ =404;
	}

}",
  notify  => Service['nginx'],
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
