file { 'shh_config':
  ensure  => file,
  path    => '/home/alsayed/.ssh/ssh_config',
  content => " Host *\n   PasswordAuthentication no\n",
}
