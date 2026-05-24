all:
	@echo "Nothing to do"

bindir ?= /usr/bin
sysconfdir ?= /etc

install:
	install -d -m 0755 $(DESTDIR)$(bindir)
	install -d -m 0755 $(DESTDIR)$(sysconfdir)/yum
	install -p -m 0755 yummie $(DESTDIR)$(bindir)/yummie
	install -p -m 0644 yummie.conf.example $(DESTDIR)$(sysconfdir)/yum/yummie.conf
	@echo "Do not forget to edit /etc/yum/yummie.conf"

test: yummie
	pycodestyle --ignore=E128 $^

lint: yummie
	ruff check $^

format: yummie
	ruff format $^
