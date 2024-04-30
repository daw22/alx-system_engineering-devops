# configure nginx with custom http_header 'X-Served-By'
-> package {'nginx':
  ensure => present,
}

-> file_line {'custum header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

-> exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
