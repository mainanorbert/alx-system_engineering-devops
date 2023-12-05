# configuring nginx

# Update package lists
exec { 'apt-get-update':
  command     => 'apt-get update',
  path        => '/usr/bin',
  refreshonly => true,
}

# Install Nginx
package { 'nginx':
  ensure => 'installed',
  require => Exec['apt-get-update'],
}

# Create directory and files
file { '/var/www/html':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}

# Notify a script to restart Nginx after configuration changes
exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
