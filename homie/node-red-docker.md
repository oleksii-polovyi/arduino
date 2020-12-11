Run docker container

```
docker run -it -p 1880:1880 --name homie nodered/node-red
```

Open Node-Red in your web browser to import the flow and configure the dashboard.
```
http://127.0.0.1:1880
```

View dashboard
```
http://127.0.0.1:1880/ui/
```