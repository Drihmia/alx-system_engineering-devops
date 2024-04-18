file {'/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 3000"',
  }
