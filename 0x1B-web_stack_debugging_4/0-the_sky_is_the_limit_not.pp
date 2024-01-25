# fixing error request in apache

exec { 'error request fix':
  command  => 'sudo sed -i \'s/15/30000/\' /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
