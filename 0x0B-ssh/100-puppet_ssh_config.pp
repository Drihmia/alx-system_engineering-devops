# using a puppet file (this manifest) to set up our server to use ~/.ssh/school as a private key
# and never allow the uses of pasword


# create or modifie if exist the needed file
file { '/home/ubuntu/.ssh/school':
  ensure  => file,
  mode    => '0400',
  owner   => ubuntu,
  content => '
  Host ./*
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
',
}
