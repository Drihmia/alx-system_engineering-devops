# create a manifest that kills a process named "killmenow".
exec { 'kill_killmenow':
  command => 'pkill  -xf \'/bin/bash ./killmenow\'',
  onlyif  => 'pgrep -af \'/bin/bash ./killmenow\'',
  path    => '/usr/bin/',
}
