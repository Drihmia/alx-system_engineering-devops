# create a manifest that kills a process named killmenow.
exec { 'kill ./killmenow':
  command => '/usr/bin/pkill -xf \'/bin/bash ./killmenow\'',
  onlyif  => '/usr/bin/pgrep -af \'/bin/bash ./killmenow\'',
  }
