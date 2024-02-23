# create a file in /tmp.

file {'/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'redouane',
  group   => wheel,
  mode    => '0744',
}
