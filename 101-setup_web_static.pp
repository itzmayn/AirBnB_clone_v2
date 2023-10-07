# Configures a web server for deployment of web_static.

# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"


# Ensure directories are created
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
  owner   => 'root',
  group   => 'root',
}

# Ensure symbolic link is created
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                location /hbnb_static {
                    alias /data/web_static/current/;
                }

                location /redirect_me {
                    return 301 http://www.holbertonschool.com/;
                }

                error_page 404 /custom_404.html;
                location = /custom_404.html {
                    root /usr/share/nginx/html;
                    internal;
                }
              }",
  owner  => 'root',
  group  => 'root',
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => File['/etc/nginx/sites-available/default'],
}
