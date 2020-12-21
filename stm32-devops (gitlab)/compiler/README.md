# Компилятор

Docker-образ с установленными пакетами, необходимыми для сборки встроенного ПО для микроконтроллера STM32.
Пакеты:
- make
- gcc-arm-none-eabi

## Сборка образа

Для сборки введите команду
```
docker build -t <registry url>:compiler .
```

## Загрузка образа в GitLab Container Registry

```
docker login registry.gitlab.com
docker push <registry url>:compiler
```

## Использование образа для сборки программы

Для сборки программы в данном проекте используется файл docker-compose-compile.yml, находящийся в папке **stm32-devops (gitlab)**.
Предварительно рекомендуется создать папку **stm32-devops (gitlab)/build**. Для запуска необходимо ввести:
```
docker-compose up
```
