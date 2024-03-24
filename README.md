# Микросервис для создания задач на вычислительном кластере

Используется:
+ Python 3.12
+ FastApi
+ Dockerfile


Запуск происходит на порту `9024` при помощи команд:

`docker build -t vm_service .`

`docker -d -p 9024:9024 --name vm_container vm_service`