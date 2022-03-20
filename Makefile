build:
	docker build -t shortener .
tag:build
	docker tag shortener freekn/shortener
push:tag
	docker push freekn/shortener

install:
	helm install -f deploy/url-shortener/values.yaml shortener deploy/url-shortener/
uninstall:
	helm uninstall shortener
upgrade:
	helm upgrade --install shortener deploy/url-shortener/