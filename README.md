# Обучающий проект запуска программы в Docker

## 1. Установка Docker

Установку осуществлял по интрукции к курсу.

Добавил официальные GPG ключи
```
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
Добавил репозиторий Docer в источники Apt
```
echo \
"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Обновил индексы пакетов
```
sudo apt-get update
```
Установил пакеты Docker
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Проверил установку 
```
sudo docker run hello-world
```
Получил вывод
```
roma@roma-System-Product-Name:~$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:d000bc569937abbe195e20322a0bde6b2922d805332fd6d8a68b19f524b7d21d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
Создал группу docker 
```
sudo groupadd docker
```
Добавил текущего пользователя в группу docker:
```
sudo usermod -aG docker $USER
```
Выполнил команду, что бы изменения вступили в силу
```
newgrp docker
```
Права на подключение 
```
sudo chmod 666 /var/run/docker.sock
```

Проверил работоспособность работы docker без sudo
```
roma@roma-System-Product-Name:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
Включил автозапуск. 
```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

## 1.1 Установка Docker Compose
Загрузил последний дистрибутив
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
```
Установил разрешения
```
sudo chmod +x /usr/local/bin/docker-compose
```
Проверил установки
```
roma@roma-System-Product-Name:~$ docker-compose --version
Docker Compose version v2.24.6
```
## 2. Разработал простую программу для вывода текущей даты 
```
Gettime.py
```
Создал репозиторий на GitHub
```
???
```
## 3 Создание Docker-образа для программы

Создаем Dockerfile

Собираем его
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker build -t get-time-app .
[+] Building 0.9s (8/8) FINISHED                                                                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                                                                               0.0s
 => => transferring dockerfile: 322B                                                                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                                                                                 0.4s
 => [internal] load .dockerignore                                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [1/3] FROM docker.io/library/python:3.8-slim@sha256:23252009f10b4af8a8c90409c54a866473a251b001b74902f04631dd54cfccc8                                           0.0s
 => [internal] load build context                                                                                                                                  0.0s
 => => transferring context: 87.48kB                                                                                                                               0.0s
 => CACHED [2/3] WORKDIR /app                                                                                                                                      0.0s
 => [3/3] COPY . /app                                                                                                                                              0.2s
 => exporting to image                                                                                                                                             0.2s
 => => exporting layers                                                                                                                                            0.2s
 => => writing image sha256:9b949e3495dc0a963857941a4b3ce90b5f11b7a3ee7c94433d5cf156580daf4f                                                                       0.0s
 => => naming to docker.io/library/get-time-app  
```
Проверяем наличие образа 
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
get-time-app   latest    9b949e3495dc   36 seconds ago   139MB
```
## 4 Запуск Python-приложения в Docker-контейнере
Запустим его и проверим его работу
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker run -itd  get-time-app 
cefc9ebe582f12756c5b0ac4cef77b1ee4be0ebeaa663487b4a3d1df907ba199
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
cefc9ebe582f   get-time-app   "python GetTime/Gett…"   18 seconds ago   Up 17 seconds             stupefied_dirac
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker logs --follow cefc9ebe582f
Currenttime =  21.02.2024 02:03:37
Currenttime =  21.02.2024 02:03:42
Currenttime =  21.02.2024 02:03:47
Currenttime =  21.02.2024 02:03:52
Currenttime =  21.02.2024 02:03:57
Currenttime =  21.02.2024 02:04:02
Currenttime =  21.02.2024 02:04:07
Currenttime =  21.02.2024 02:04:12
Currenttime =  21.02.2024 02:04:17
Currenttime =  21.02.2024 02:04:22
Currenttime =  21.02.2024 02:04:27
Currenttime =  21.02.2024 02:04:32
```
Остановим работу контейнера 
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker stop cefc9ebe582f
cefc9ebe582f
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
## 5. Работа с Docker Compose
Создадим docker-compose.yml. Запустим два контейнира с нашим приложением. 
Запустим контейнеры описаные в compose файле.
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker-compose up -d
[+] Running 2/3
 ⠴ Network gettime_default         Created                                                                                                                         0.6s 
 ✔ Container gettime-get_time_1-1  Started                                                                                                                         0.3s 
 ✔ Container gettime-get_time_2-1  Started                                                                                                                         0.5s 
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker-compose ps
NAME                   IMAGE          COMMAND                  SERVICE      CREATED          STATUS          PORTS
gettime-get_time_1-1   get-time-app   "python GetTime/Gett…"   get_time_1   17 seconds ago   Up 17 seconds   
gettime-get_time_2-1   get-time-app   "python GetTime/Gett…"   get_time_2   17 seconds ago   Up 16 seconds   
```
Проверяю вывод в лог
```
roma@roma-System-Product-Name:~/PycharmProjects/getTime$ docker-compose logs -f
get_time_2-1  | Currenttime =  21.02.2024 17:36:06
get_time_2-1  | Currenttime =  21.02.2024 17:36:11
get_time_2-1  | Currenttime =  21.02.2024 17:36:16
get_time_2-1  | Currenttime =  21.02.2024 17:36:21
get_time_2-1  | Currenttime =  21.02.2024 17:36:26
get_time_2-1  | Currenttime =  21.02.2024 17:36:31
get_time_2-1  | Currenttime =  21.02.2024 17:36:36
get_time_1-1  | Currenttime =  21.02.2024 17:36:05
get_time_1-1  | Currenttime =  21.02.2024 17:36:10
get_time_1-1  | Currenttime =  21.02.2024 17:36:15
get_time_1-1  | Currenttime =  21.02.2024 17:36:20
get_time_1-1  | Currenttime =  21.02.2024 17:36:25
get_time_1-1  | Currenttime =  21.02.2024 17:36:30
get_time_1-1  | Currenttime =  21.02.2024 17:36:35
get_time_1-1  | Currenttime =  21.02.2024 17:36:40
get_time_2-1  | Currenttime =  21.02.2024 17:36:41
get_time_1-1  | Currenttime =  21.02.2024 17:36:45
get_time_2-1  | Currenttime =  21.02.2024 17:36:46
get_time_1-1  | Currenttime =  21.02.2024 17:36:50
get_time_2-1  | Currenttime =  21.02.2024 17:36:51
get_time_1-1  | Currenttime =  21.02.2024 17:36:55
get_time_2-1  | Currenttime =  21.02.2024 17:36:56

```

