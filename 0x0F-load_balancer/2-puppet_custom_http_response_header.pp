# configure nginx with custom http_header 'X-Served-By'
exec {'update':
  command  => 'apt-get update',
  provider => shell,
}
-> package {'nginx':
  ensure => present,
}

-> file_line {'custum_header':
  ensure => present,
  path   => '/etc/nginx/nginx/nginx.conf',
  line   => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match  => 'http {',
}

-> exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
