# manifest that kills a process named killmenow.

exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
}
# The path parameter specifies where to find the pkill command (common locations like /usr/bin and /bin)


# Another Solutions
#
# exec { 'kill_killmenow':
#   command  => 'pkill killmenow',
#   provider => 'shell',
# }
# The provider was set to 'shell', which means the command is executed in a shell environment.

# or
# exec { 'killmenow':
#     command => '/usr/bin/pkill killmenow',
# }

