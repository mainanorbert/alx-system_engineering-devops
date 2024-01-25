# increasing traffic in nginx
exec { 'fixing-nginx':
  command => 'sed -i "s/15/3096" /etc/defualt/nginx',
  path    => "/usr/bin/bin/:/bin/"
} ->

# restarting nginx
exec { 'restarting-nginx'
  command => "sudo service nginx restart"
  path => "/etc/init.d"
