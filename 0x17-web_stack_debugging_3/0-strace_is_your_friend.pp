#  Strace is your friend
exec { 'sed config':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin/'
}
