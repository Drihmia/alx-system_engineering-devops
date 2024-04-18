# raise number of request in the stack to handle
file {'/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 6000"',
  notify  => Service['nginx'],
  }

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  }

package { 'nginx':
  ensure => installed,
  }
