# Manifest that kills a process
exec{'killmenow_process':
command => 'pkill killmenow',
path => '/usr/bin/'
}