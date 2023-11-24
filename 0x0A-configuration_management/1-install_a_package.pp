# installing falsk using pip3 using puppet

  puppet { 'flask':
    ensure  => '2.1.0',
    provide => 'pip3'
    }
