# cAdvisor-exporter

Данный инструмент позволяет собирать метрики с docker-контейнеров. На Raspberry Pi работает спорно, но позволяет вывести метрики о количестве запущенных контейнеров.

Для запуска cAdvisor скопируйте каталог на Raspberry Pi и введите:
```
docker-compose up
```
О настройке node-exporter можно почитать [тут](https://linuxhit.com/prometheus-node-exporter-on-raspberry-pi-how-to-install/).
