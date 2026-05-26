from distutils.core import setup

setup(
    name="yummie",
    version="0.2.0",
    author="Wijnand Modderman-Lenstra",
    author_email="maze@pyth0n.org",
    description="Automated yum upgrades",
    license="MIT",
    keywords="yum rpm update upgrade",
    python_requires=">=3.6",
    scripts=["yummie"],
    data_files=(("/etc/yum/yummie.conf", "yummie.conf.example"),),
)
