# Metrics Server (Prometheus+Grafana)

## Настройки Prometheus

Для настройки источников, а также конфигурации дополнительных параметров необходимо изменить файл prometheus.yml

## Запуск

Для запуска Prometheus+redis+grafana введите:
```
docker-compose up
```
Prometheus доступен на порту 9090, Grafana - 3000.
При настройке ресурсов данных Grafana в списке источников выберите "Prometheus" и введите URL: 
```http://prometheus:9090``` (см. рисунки ниже)

![Выбор ресурса данных](https://github.com/normall777/Stm32-Devops/blob/main/pic/Grafana%20data%20source.png)

![Настройка URL Grafana](https://github.com/normall777/Stm32-Devops/blob/main/pic/Grafana%20Prometheus.png)

## Dashboard

При желании можно импортировать готовый дашборд для отображения метрик, например, **My Node Explorer dashboard.json**, находящийся в данном проекте. Либо сделать свой.

![My Node Explorer dashboard](https://github.com/normall777/Stm32-Devops/blob/main/pic/Grafana%20dashboard.png)
