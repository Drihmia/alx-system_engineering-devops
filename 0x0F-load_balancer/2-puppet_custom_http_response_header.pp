# Update system packages
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => '/usr/bin/',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Package['update'],
}

# Add custom HTTP header to Nginx configuration
file_line { 'add_custom_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => '^\s*server_name _;',
  match   => '^(\s*)server_name _;$',
  after   => 'server_name _;',
  content => "        \\1add_header X-Served-By \"${trusted['hostname']}\";",
  require => Package['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
