# python-docker

## docker-compose

修改`docker-compose.yml`中的`volumes`配置, 将宿主机数据库路径映射到容器中

```yaml
volumes:
    - /Users/lincenying/web/mongodb/data:/data/db
```

```bash
docker-compose up -d
```
