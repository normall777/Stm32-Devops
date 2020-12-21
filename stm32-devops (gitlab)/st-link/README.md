# ST-Link

Docker-образ с установленными пакетами, необходимыми для записи программы в микроконтроллер через программатор ST-link.

![Программатор ST-link](https://github.com/normall777/Stm32-Devops/blob/main/pic/stlink-v2.jpg)

Пакеты:
- git 
- build-essential 
- cmake 
- rpm 
- libusb-1.0-0-dev
- libusb-1.0
Дистрибутив ST-Link: https://github.com/stlink-org/stlink.git

Docker-образ производит сборку дистрибутива. При запуске выполняет процедуру очистки памяти и прошивки файлов *.hex, 
находящихся в директории **stm32-devops (gitlab)/build**

## Сборка образа

Для сборки введите команду
```
docker build -t <registry url>:st-link .
```

## Загрузка образа в GitLab Container Registry

```
docker login registry.gitlab.com
docker push <registry url>:st-link
```

## Использование образа программирования микроконтроллера STM32

Для запуска процедуры программирования проекте используется файл docker-compose-stand.yml, оторый находится в папке stm32-devops (gitlab), 
совместно с docker-образом трансляции видео с веб-камеры motion.
Предварительно в папку **stm32-devops (gitlab)/build** должны быть загружены собранные артефакты. Для запуска необходимо ввести:
```
docker-compose --file docker-compose-stand.yml up
```
