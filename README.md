# yummie

Automated system upgrades using yum.


## Usage

You can specify options via the command line, use `yummie --help` to see what
commands are available. Yummie uses an ini-style configuration file, default it
is installed in `/etc/yum/yummie.conf`.


## Configuration

### Package exclusions

You can specify strings or globs to match package names. Packages listed in the
`packages` section will be excluded from automated upgrades.

To prevent apache from upgrading automatically, add:

    [package]
    exclude.apache = httpd*

### Repository exclusions

You can specify strings or globs to match repository names. Packages in the
repositories listed in the `repository` section will be excluded from automated
upgrades.

To prevent packages in the `mysql` repository from upgrading automatically,
add:

    [repository]
    exclude.mysql = mysql*

## Bugs/Features

You can issue a ticket in GitHub: https://github.com/tehmaze/yummie/issues
