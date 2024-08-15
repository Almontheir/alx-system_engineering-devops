# 0-strace_is_your_friend.pp

# Ensure the necessary configuration file exists
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  source  => 'puppet:///modules/your_module/000-default.conf', # Adjust the source path as needed
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'], # Restart Apache if the config changes
}

# Ensure the necessary permissions are set
exec { 'set_permissions':
  command => 'chown -R www-data:www-data /var/www/html', # Adjust the path as needed
  refreshonly => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'],
}
