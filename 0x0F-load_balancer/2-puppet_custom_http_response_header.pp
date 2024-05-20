# Installs a Nginx server with custome HTTP header

# Install Nginx package
exec { 'apt update':
  command  => 'sudo apt-get update -y',
  provider => shell,
}

-> package { 'nginx':
  ensure          => installed,
  provider        => apt,
  install_options => ['-y'],
}

# Allow Nginx through the firewall
exec { 'allow Nginx HTTP':
  provider => shell,
  command  => "sudo ufw allow 'Nginx HTTP';",
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;
  \n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

# Restart Nginx
-> service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
