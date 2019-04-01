﻿Программа разрабатывалась для проекта **SMART COFFEE MACHINE**.


Цель проекта
====== 
Создание программы для создания фотографии лица человека, отправки фотографии на сервер и получения данных от сервера.

Требования
======
Инструменты необходимые для корректной работы данной программы:

* Raspberry Pi
* SD-карта минимум 8 гб
* Операционная система Raspbian
* Веб-камера
* Python3  с установленными дополнительными библиотеками
* Каскад Хаара - haarcascade_frontalface_default.xml

Инструкция
----
 На SD-карту устанавливается операционная система Raspbian. Затем к Raspberry Pi подключается Веб-камера и по необходимости устанавливается ПО для веб-камеры. Установить Python, если он отсутствует.
 К Python устанавливаем дополнительные библиотеки: 
 
 1. OpenCV
 
 2. Paramiko
 
 3. Requests
 
 Скачать haarcascade_frontalface_default.xml можно здесь -> [ссылка на репозиторий](https://github.com/opencv/opencv/tree/master/data/haarcascades)

Авторы
=====
* Ануар Нурмат (Nnnurrrma@gmail.com)
* Красников Евгений (krasnikovevgen16@gmail.com)
