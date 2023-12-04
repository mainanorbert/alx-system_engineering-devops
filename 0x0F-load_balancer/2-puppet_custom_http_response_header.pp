# 2-puppet_custom_http_response_header.pp

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/nginx.conf.backup':
  ensure  => present,
  source  => '/etc/nginx/nginx.conf',
  require => Package['nginx'],
}

file { '/etc/nginx/conf.d/custom_http_response_header.conf':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
    }
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/conf.d/custom_http_response_header.conf'],
}
