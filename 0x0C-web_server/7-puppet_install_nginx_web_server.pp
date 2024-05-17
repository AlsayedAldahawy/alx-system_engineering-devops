# Puppet script that configures a new ubuntu machine to install Nginx and handles redirection and 404 page.


# Install Nginx package

exec { 'apt update':
  command => 'sudo apt-get update -y',
}

-> package { 'nginx':
  ensure          => installed,
  provider        => apt-get,
  install_options => ['-y'],
}

# Allow Nginx through the firewall
exec { 'allow Nginx HTTP':
  provider => shell,
  command  => "sudo ufw allow 'Nginx HTTP';",
}

# Set permissions for Nginx document root
file { '/var/www/html':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create custom index and 404 pages
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure Nginx server block
file { '/etc/nginx/sites-enabled/default':
  content => "
    server {
        listen 80 default_server;
        server_name _;

        location = /redirect_me {
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }

        error_page 404 /404.html;

        # Other server block configuration...
    }
  ",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
