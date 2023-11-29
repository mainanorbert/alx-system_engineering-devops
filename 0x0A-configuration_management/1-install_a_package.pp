# installing flask with puppet
  package { 'flask':
    ensure    => '2.1.0',
    providere => 'pip3'
}

  package { 'werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3'
}
