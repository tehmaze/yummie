from distutils.core import setup, Extension

setup(
    name         = 'yummie',
    version      = '0.1.10',
    author       = 'Wijnand Modderman-Lenstra',
    author_email = 'maze@pyth0n.org',
    description  = 'Automated yum upgrades',
    license      = 'MIT',
    keywords     = 'yum rpm update upgrade',
    scripts      = ['yummie'],
    data_files   = (
        ('/etc/yum/yummie.conf', 'yummie.conf.example'),
    ),
)
