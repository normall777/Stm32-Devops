# Stm32-Devops

Проект сделан для курса Программная инженерия 2020

Система автоматического развертывания встроенного программного обеспечения микроконтроллера STM32 представлена на рисунке ниже. 

При загрузке изменений в репозиторий Gitlab (1) запускается сценарий компиляции (2) загруженного кода на отдельной докер-машине. Собранные файлы (3) отправляются на стенд (4) и в репозиторий Gitlab, где хранятся определенное время. Стенд производит процедуру очистки памяти и программирования микроконтроллера (5) и подключает веб-камеру. Специальный telegram-бот отправляет пользователю сообщение, в котором содержится информация о подключении к веб-камере стенда (6). После окончания работы пользователь с помощью сообщения (7) отключает веб-камеру, производится отчистка кэша. 

Мониторинг системы осуществляет сторонний сервер (8) с помощью платформы Prometheus, отображая данные в Grafana. 

![Концепция системы](https://github.com/normall777/Stm32-Devops/edit/main/pic/conception.png)
