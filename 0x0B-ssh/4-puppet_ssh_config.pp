#!/ust/bin/env bash
# Client configuration file (w/ Puppet)

file_line {
line => 'IdentityFile ~/.ssh/holberton',
path => '/etc/ssh/ssh_config'
}

file_line {
line => 'PasswordAuthentication no',
path => '/etc/ssh/ssh_config'
}
