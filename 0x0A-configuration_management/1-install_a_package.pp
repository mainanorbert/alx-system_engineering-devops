#!/usr/bin/pup

# Installing Flask version 2.1.0 using pip3
  exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => ['/usr/bin'],
    unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0',
    require => Package['python3-pip'],
}
  package { 'python3-pip':
    ensure => installed,
}

