# Using puppet to install a package
package{'python3-pip':
ensure => 'installed',
}

package{'flask':
ensure   => 'installed',
provider => 'pip',
require  => Package['python3-pip'],
}