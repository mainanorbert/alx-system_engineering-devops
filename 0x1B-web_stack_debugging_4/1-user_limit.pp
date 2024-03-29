# puppet script to configure and allow holberton user log
# and open files without error

# increase hard file limit
exec { 'increase-file-hard-limit':
  command => 'sed -i \'/holberton hard/s/5/50000/\' /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}

# increase-file-soft-limit
exec { 'increase file limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
