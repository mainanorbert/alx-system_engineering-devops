# Installing Nginx and configuration
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/http_header.conf':
    ensure  => present,
    content => "add_header X-Served-By ${hostname};",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
