# Проект для микроконтроллера STM32

Проект сгенерирован с помощью программы STM32CubeMX для среды MDK-ARM (Keil uVision IDE) и для сборки с помощью утилиты make (Makefile).

## Сборка проекта
- С помощью встроенного компилятора среды Keil
- С помощью утилиты make:
```
make
```

## target.txt
В данном файле указываются артефакты, которые будут скопированы в папку **stm32-devops (gitlab)/build** после компиляции, например, файлы .bin, .hex и .map.

## compile.sh
В данном файле содержатся инструкции для сборки и копирования артефактов.

## flash.sh
В данном файле содержатся инструкции для программирования утилитой st-flash.
