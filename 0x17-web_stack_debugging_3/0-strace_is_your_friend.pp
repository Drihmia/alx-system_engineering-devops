# make sure the file "/var/www/html/wp-settings.php" exist
# and replace the phpp (syntax error) into php in the line 137.

# Define the file path
$file_path = '/var/www/html/wp-settings.php'

# Ensure the file exists
file { $file_path:
  ensure => present,
  notify => Exec['replace phpp']
}

exec { 'replace phpp':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => '/bin/',
  require => File[$file_path],
}
