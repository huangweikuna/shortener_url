# URL-SHORTENER

## 预备工作

- 一个k8s集群
- Helm部署工具

## 安装

```
git clone https://github.com/huangweikuna/shortener_url.git
cd url_shortener
make install
```

## 访问服务

```
kubectl --namespace ${namespace} port-forward svc/shortener-server 8080

curl -X 'POST' localhost:8000/newurl -d '{"url":"https://www.google.com"}'
```

### 或

```
# add /etc/hosts
${Cluster entry ip} url-shortener.com

curl -X 'POST' url-shortener.com/newurl -d '{"url":"https://www.google.com"}'
```

## 说明

服务依赖 Mysql Redis 服务，Mysql 作为持久化数据组件，Redis 作为缓存组件，这两个组件在生产环境中应该是单独的高可用集群，这里为了专注与服务本身并没有为此做出很多，只是为功能准备。

服务架构图如下：
<img width="375" alt="image" src="https://user-images.githubusercontent.com/41366091/159145678-32f0d439-6d7e-491d-8345-61d824de0c58.png">


