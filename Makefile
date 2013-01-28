all:
	@echo "Nothing to do"

install:
	install -m755 yummie /usr/bin/yummie
	install -m644 yummie.conf.example /etc/yum/yummie.conf
	@echo "Do not forget to edit /etc/yum/yummie.conf"

test:
	pep8 --ignore=E128 yummie
