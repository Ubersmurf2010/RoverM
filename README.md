# **Rover & Student**
Ссылка на актуальный репозиторий проекта: [Открыть ссылку](https://github.com/Ubersmurf2010/RoverM/)

В инструкции описана первоначальная настройка ноутбука или компьютера, с которого будет управляться робот (далее пульт) и самого робота. 
Сначала рассмотрим установку дополнительных программ, а затем сам процесс запуска робота.
## ПО для работы робототехнических сиситем Ровер и Студент. 

Пульт тестировался на ОС Ubuntu 22.04.2 LTS и Windows 10.
Пульт универсален для Unix и Windows, так как python это интерпретируемый язык, а не компилируемый, как C++ или Java.
На плате уже установлено все ПО, которое необходимо только запустить.
Все рабочие файлы находятся в домашнем каталоге робота.

## Установка дополнительных программ на Windows для установки *ssh* или *vnc* соединения.
Наиболее простой способ запустить исполняемый файл, это воспользоваться утилитами, которые позволяют подключиться по ssh-соединению, например, putty [Download putty](https://www.putty.org).
Также можно использовать программу для удаленного доступа, например, [Download RealVNC](https://www.realvnc.com/en/).

## Linux не требует установки дополнительных программ.
Linux уже имеет встроенный ssh-протокол.

## SSH-протокол
Для установки ssh-соединения необходимо открыть терминал и использоваться команду(на примере Rover1):
```
ssh rover1@192.168.0.17
```
Далее необходимо ввести пароль, который на всех роботах по умолчанию 123.

## Настройка пульта перед использованием роботов (Windows).
Пример настройки ПО для Windows 10.

Мы рекомендуем пользоваться python *IDE PyCharm*, поэтому ее и установим. Важно в процессе установки добавить python в переменную среду *PATH*. Также Вы же можете использоваться любую удобную Вам *IDE*.
После установки необходимо убедиться, что версия Интерпретатор python выше, чем 3.10. В ином случае добавить новый интерпретатор версией выше, чем 3.10.

Далее необходимо подключить *github* к *PyCharm*.
Для переходим на вкладку создание проекта.
![image](https://github.com/Ubersmurf2010/RoverM/assets/113335397/5352eaeb-1025-4944-a871-a1a9ef9b8fbd)
На этой вкладке выбираем Get from VCS. 
- Version control: git
- URL: https://github.com/Ubersmurf2010/RoverM.git
- Directory: выбираем папку, куда необходимо клонировать репозиторий проекта. 
Если PyCharm пишет, что git не установлен, значит его необходимо установить. (кнопка ниже Download and install)
После нажимаем кнопку CLone. 

Если все установилось и скопировалось правильно, то на нижней панели будет доступна вкладка *git*.
Теперь открываем папку с нашим проектом.

Для работы программы необходимо установить зависимость *pynput*.
Откроем терминал внутри *IDE* и введем команду:
```
pip install pynput
```

## Настройка пульта перед использованием роботов (UNIX). 
Пример установки ПО на Unix систему, например Ubuntu 22.04.2 LTC (для других версий linux набор стандартных команд может существенно отличаться).
```
sudo apt update
sudo apt install git
```
Скопируем репозиторий в домашний каталог.
```
cd ~/
sudo git clone https://github.com/Ubersumrf2010/RoverM
```
Для работы *onpult.py* необходимо установить сам python и дополнительные зависимости к нему.
Сначала необходимо убедиться, что Python 3 установлен в системе выполнив команду в терминале.
```
python3 --version
```
Команда выведет текущую версию Python, которая используется в системе. Далее необходимо установить pip3:
```
sudo apt -y install python3-pip
sudo pip install pynput
```
## Запуск робота
1. Воткнуть разъем от аккумулятора в робот.
2. Подключить по *ssh* или *vnc* к pi.
3. *onpult.py* и *onboard.py* перед работой необходимо настроить. Ввести в обоих файлах одинаковый ip-адрес робота. 
В конфигурационном файле *cval.py* можно настроить клавиши для управления роботом.
4. После того, как нам удалось подключиться к плате, необходимо запустить исполняемый файл *onboard.py*.
```
cd ~/
cd RoverM/control/
sudo python onboard.py
```
5. Заупстить дисплей для отображения параметров системы (действие не является обязательным).
```
cd ~/
sudo python I2Cdisplay.py
```
6. Запустить исполняемый файл на пульте.
```
cd RoverM/pult
sudo python onpult.py
```
В *IDE PyCharm* нажать на зеленую кнопку *run*.
Важно отметить, что испольняемый файл *onpult.py* (клиент) должен запускаться только после *onboard.py* (сервер). 
В ином случае соединение не будет установлено.

7. Загрузка интерфейса для работы с камерой, а также же включение самой камеры выполняется автоматически при включении робота.
Чтобы получать изображение с камеры необходимо зайти в любой браузер и вбить в адресную строку ip-адрес робота:port/html/
Например, для Rover1 запрос будет иметь следующий вид:
192.168.0.17:100/html/

=> Обновление репозитория выполняется (PyCharm: pull)
```
cd ~/
cd RoverM/
sudo git pull
```


## Управление движением роботом
- w – движение вперед;
- s – двжиение назад;
- a – танковый поворот налево;
- d – танковый поворот направо;
- q – поворот налево;
- e – поворот направо;
## Управлением камерой
- 1 – поднять камеру;
- 2 – опустить камеру;
## Управление скоростью моторов
- z – замедлиться;
- x – ускориться;
## Управление манипулятором
- u, h – управление первой осью манипулятора
- i, j – управление второй осью манипулятора
- o, k – управление третьей осью манупулятора
- p, l – управление схватом
## Управление фарой
- v, b – включить и выключить фару
