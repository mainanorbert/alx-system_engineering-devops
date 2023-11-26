# configuring the ssh file with puppet
include stdlib

  file_line { 'identity_file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    }

    file_line { 'authentic_key':
      ensure => present,
      path   => '/etc/ssh/ssh_config',
      line   => 'PasswordAuthentication no',
      }
