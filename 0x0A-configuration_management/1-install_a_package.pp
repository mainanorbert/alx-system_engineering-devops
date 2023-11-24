# installing flask from pip3 with puppet

exec { 'install_flask':
  command   => '/usr/bin/pip3 install Flask==2.1.0',
}
