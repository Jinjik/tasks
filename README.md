﻿Программа разрабатывалась для проекта SMART COFFEE MACHINE.


Цель проекта
====== 
Создание программы для создания фотографии лица человека и взаимодействия с сервером для обменна данными.

Требования
======
Инструменты необходимые для корректной работы данной программы:

* Raspberry Pi
* SD-карта
* Операционная система Raspbian
* Веб-камера
* Python с установленными дополнительными библиотеками

Инструкция
----
 На SD-карту устанавливается операционная система Raspbian. Затем к Raspberry Pi подключается Веб-камера и по необходимости устанавливается ПО для веб-камеры. Установить Python, если он отсутствует.
 К Python устанавливаем дополнительные библиотеки: 
 1 OpenCV
 2 Paramiko
 3 Requests
 Также скачиваем haarcascade_frontalface_default.xml и п программе прописываем полный путь до файла.
 
 Скачать haarcascade_frontalface_default.xml можно здесь -> https://github.com/opencv/opencv/tree/master/data/haarcascades
