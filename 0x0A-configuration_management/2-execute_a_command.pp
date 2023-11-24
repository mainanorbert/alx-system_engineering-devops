# creating a manifest that kills a process
  exec { 'killmenow':
    path    => '/usr/bin',
    command => 'pkill killmenow'
    }
