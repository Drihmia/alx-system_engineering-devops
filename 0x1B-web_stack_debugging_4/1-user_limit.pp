file { '/etc/default/nginx':
  ensure => present,
}

exec { 'replace_hard':
  command   => "sed -i '/^holberton[[:space:]]*hard/s/.*/holberton hard nofile 10000/' /etc/security/limits.conf",
  path      => ['/usr/bin', '/usr/sbin', '/bin'],
  subscribe => File['/etc/default/nginx'],
}
exec { 'replace_soft':
  command   => "sed -i '/^holberton[[:space:]]*soft/s/.*/holberton soft nofile 10000/' /etc/security/limits.conf",
  path      => ['/usr/bin', '/usr/sbin', '/bin'],
  subscribe => File['/etc/default/nginx'],
}
