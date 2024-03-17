# Update system packages
exec { 'apt-update':
  command => 'apt-get update -y',
  path    => ['/usr/sbin/', '/usr/bin/'],
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Overwrite the file with the custom header added
file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index  index.html index.htm index.nginx-debian.html ;

	server_name _;

	add_header X-Served-By ${hostname};

	location / {
		try_files \$uri \$uri/ =404;
	}
}
",
  require => Package['nginx'],
}

# Restart the Nginx server
exec {'restart':
  command     => 'service nginx restart',
  path        => ['/usr/sbin/', '/usr/bin/'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

# making sure that Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['restart'],
}
