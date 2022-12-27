# scrapy_parser_pep
Склонируйте проект на Ваш компьютер
```
git clone https://github.com/Oborotistova/scrapy_parser_pep.git
```
Перейдите в папку с проектом
```
cd scrapy_parser_pep
```
Активируйте виртуальное окружение
```
python3 -m venv venv
source venv/Scripts/activate
```
Обновите менеджер пакетов (pip)
```
pip3 install --upgrade pip
```
Установите необходимые зависимости
```
pip3 install -r requirements.txt
```

Использование
Запуск парсера осуществляется из командной строки при помощи команды::
```
scrapy crawl pep
```
Результаты работы парсера будут сохранены в csv-файлах в папке results