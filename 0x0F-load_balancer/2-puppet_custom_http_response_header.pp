# Update system packages
exec { 'apt-update':
  command => '/usr/bin/apt-get update -y',
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

        location = /redirect_me {
                return 301 /redirect_me/;
        }
        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html;
                internal;
                }
        }
}
",
  require => Package['nginx'],
}

# Restart the Nginx server
exec {'restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
