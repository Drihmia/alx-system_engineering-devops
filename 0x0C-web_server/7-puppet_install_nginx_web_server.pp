# Nginx should be listening on port 80

exec {'apt-get update':
  command => 'apt-get update -y',
  path    => ['/usr/bin/', '/usr/sbin/'],
  }

package {'nginx':
  ensure => installed,
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!\n',
}

file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index  index.html index.htm index.nginx-debian.html ;

	server_name _;
	
	location /redirect_me/ {
		return 301 https://github.com/Drihmia;
	}
	location / {
		try_files \$uri \$uri/ =404;
	}
}",
}

exec {'restart':
  command     => 'sudo service nginx restart',
  path        => ['/usr/bin/', '/usr/sbin/'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
