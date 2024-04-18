# raise number of request in the stack to handle
file {'/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 3000"',
  }
