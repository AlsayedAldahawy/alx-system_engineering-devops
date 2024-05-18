# Puppet script that configures a new ubuntu machine to install Nginx and handles redirection and 404 page.


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

# Set permissions for Nginx document root
file { '/var/www/html':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

exec { '/var/www':
  provider => shell,
  command  => 'sudo chmod -R 755 /var/www',
}

# Create custom index and 404 pages
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure Nginx server block
file { '/etc/nginx/sites-enabled/default':
  content => '
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

        error_page 404 /404.html;

        location / {
            try_files $uri $uri/ =404;
        }
    }
  ',
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
