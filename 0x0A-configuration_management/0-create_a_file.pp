 # Puppet creating a  file that creates a file
 
file { '/tmp/school/':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'

