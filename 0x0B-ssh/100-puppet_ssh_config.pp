# Seting ssh client config file
# must be configured to use the private key ~/.ssh/school
# must be configured to refuse to authenticate using a password

file { 'shh_config':
  ensure  => file,
  path    => '/home/alsayed/.ssh/ssh_config',
  content => " Host *\n   PasswordAuthentication no\n   IdentifyFile ~/.ssh/school\n",
}
