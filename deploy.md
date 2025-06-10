1. Instala dependencias de Python:

```bash
sudo apt update
sudo apt install -y python3-pip python3-dev python3-venv python3-wheel
```

```bash
sudo apt-get install nginx mysql-server -y
```

2. Clona el repositorio y crea el entorno virtual:

```bash
git clone git@github.com:fernandokbs/python-fest.git
python3 -m venv env
source env/bin/activate
```

3. Instala las dependencias del proyecto:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Configurar MySql

```bash
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '';
```

5. Crear schema
```bash
CREATE DATABASE python_fest;
use python_fest;

CREATE TABLE `visit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT (now()),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
``` 

5.2 Configurar .env
```bash
cp .env.example .env
```

6. Probar aplicacion

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

7. Configurar service

```bash
sudo nano /etc/systemd/system/flask.service
```

```bash
[Unit]
Description=Gunicorn instance to serve myapp
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/python-fest
Environment="PATH=/root/python-fest/env/bin"
ExecStart=/root/python-fest/env/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable flask
sudo systemctl start flask
sudo systemctl status flask
```


8. Configurar nginx

```
upstream flask {
    server 127.0.0.1:8000;
}

server {
    listen 80;

    location / {
        proxy_pass http://flask;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```