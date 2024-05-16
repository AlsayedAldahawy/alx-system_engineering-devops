# Seting ssh client config file
# must be configured to use the private key ~/.ssh/school
# must be configured to refuse to authenticate using a password

include stdlib

file { '/etc/ssh/ssh_config':
  ensure => present,
}

-> file_line { 'shh_config':
  path    => '/etc/ssh/ssh_config',
  line    => "   PasswordAuthentication no\n   IdentityFile ~/.ssh/school\n",
  replace => true,
}
