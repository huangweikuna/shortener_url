build:
	docker build -t shortener .
tag:build
	docker tag shortener freekn/shortener
push:tag
	docker push freekn/shortener

install:
	helm install shortener ./depoy/url-shortener/
uninstall:
	helm uninstall shortener