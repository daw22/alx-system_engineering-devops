# script to fix wrong file path in apache2 setting file

# corrects the class name extension from phpp to php
exec { 'correct_class_name':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin', '/usr/bin']
}
