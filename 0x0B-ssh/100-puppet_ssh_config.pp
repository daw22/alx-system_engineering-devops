# update client ssh config to use private key Auth and not password
include stdlib

file_line {'Turn of password Auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	passwordAuthentication no',
  replace => true,
}

file_line {'Set prv key to use for Auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentitfyFile ~/.ssh/school',
  replace => true,
}

