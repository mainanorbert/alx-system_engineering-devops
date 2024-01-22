# increasing traffic in nginx
exec { 'fixing-nginx':
  command => 'sed -i "s/15/4096" /etc/defualt/nginx',
  path => "/usr/bin/bin/:/bin/"
} ->

# restarting nginx
exec { 'restarting-nginx'
  command => "nginx restart"
  path => "/etc/init.d"
