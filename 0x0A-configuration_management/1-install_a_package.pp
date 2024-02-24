# Using Puppet install flask from pip3.
package { 'python3':
  ensure   => 'installed',
}
# PIP3 installation
package { 'python3-pip':
  ensure   => 'installed',
}

# Werkzeug installation
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}

# Flask installation
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
