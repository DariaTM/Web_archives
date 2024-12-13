## “Digital Archiving of Today. Web Archives, Big Data, and their Applications to Research", final project, HSE 2024
This repository contains a description of web archives collection created using the **[`wpull`](https://wpull.readthedocs.io/en/master/)** file upload tool. The metadata description is obtained using **[`metawarc`](https://github.com/datacoon/metawarc)**. The archivability of the collection of sites was analyzed using the ArchiveReady resource using [`CLEAR`](http://purl.pt/24107/1/iPres2013_PDF/CLEAR%20a%20credible%20method%20to%20evaluate%20website%20archivability.pdf). metrics.

# Итоговая работа по курсу "Цифровая архивация современности. Веб-архивы, большие данные и их применение в исследовательской работе", 2024

Этот репозиторий содержит описание ***коллекции веб-архивов***, созданной с использованием инструмента **[`wpull`](https://wpull.readthedocs.io/en/master/)** для загрузки файлов. Описание метаданных получено с помощью **[`metawarc`](https://github.com/datacoon/metawarc)**. Анализ архивируемости коллекции сайтов проводился с помощью ресурса **[ArchiveReady](https://archiveready.com/)** по метрикам [`CLEAR`](http://purl.pt/24107/1/iPres2013_PDF/CLEAR%20a%20credible%20method%20to%20evaluate%20website%20archivability.pdf).


## Краткое описание коллекции

<table>
    <tr>
        <th>сайт</th>
        <th>объем архива</th>
        <th>время скачивания</th>
    </tr>
    <tr>
        <td>http://andreyvoznesenski.ru</td>
        <td>946,8 Мб</td>
        <td>4 мин</td>
    </tr>
    <tr>
        <td>http://www.zoyaboguslavskaya.ru </td>
        <td>10,6 Мб</td>
        <td>8 сек</td>
    </tr>
    <tr>
        <td>https://voznesolog.ru</td>
        <td>49,9 Мб</td>
        <td>2 мин</td>
    </tr>
    <tr>
        <td>https://rustih.ru</td>
        <td>10.94 Гб</td>
        <td>17 ч 24 мин</td>
    </tr>
    <tr>
        <td>https://ruthenia.ru</td>
        <td>5,18 Гб</td>
        <td>20 ч 47 мин</td>
    </tr>
    <tr>
        <td>https://www.ashtray.ru</td>
        <td>694,8 Мб</td>
        <td>11 мин</td>
    </tr>
</table>


В рамках этой работы я сформировала архивную коллекцию сайтов, объединенных общей тематикой: это сайты, посвященные русской поэзии и созданные энтузиастами-литературоведами, а также официальные сайты поэта Андрея Вознесенского или его супруги Зои Богуславской.

Несмотря на то, что подобные сайты не пользуются особой популярностью, многие из них представляют собой настоящие сокровищницы. Здесь можно найти редкие стихотворные и прозаические произведения, глубокие аналитические статьи, уникальные публикации и размышления, рожденные в результате кропотливого труда. 

Подобная коллекция может быть полезной в академической среде, в частности, может быть использована для различных DH-исследований. 

 ![рисунок Collection](./pictures/Collection.png)

## В коллекцию входят сайты: ##

* http://andreyvoznesenski.ru - официальный сайт поэта Андрея Вознесенского. Последняя запись сделана в 2018.

* http://www.zoyaboguslavskaya.ru - официальный сайт Зои Богуславской (супруги Андрея Вознесенского), эксперта в области кино, театра и литературы. Последняя запись сделана в 2018.

* https://voznesolog.ru - сайт клуба «Авось!», где собраны произведения поэта А.А. Вознесенского, размышления о его творчестве, отзывы и публикации. Обширная и очень профессиональная коллекция материалов, посвященная творчеству не очень хорошо изученного поэта.

* https://rustih.ru - произведение как отечественных, так и зарубежных поэтов-классиков и разбор некоторых произведений, а также цитаты классиков и ряд интересных статей с анализом произведений. Сайт может служить образовательным ресурсом.

* https://ruthenia.ru - совместный интернет-проект московского издательства ОГИ и кафедры русской литературы Тартуского университета. Связи между кафедрой и издательством имеют давнюю историю и обусловлены тем исключительным значением, которое имела для развития отечественной гуманитарной науки деятельность Ю. М. Лотмана, З. Г. Минц и их тартуских коллег. Основная цель проекта — создание единого информационного ресурса, ориентированного на исследователей- русистов (в первую очередь — филологов и историков).

* https://www.ashtray.ru - это виртуальный лабиринт, посвященный утопиям и синтезу искусств, это то место, где обитают странные проекты и идеи, витающие в воздухе. Очень хороший раздел с текстами, туда складываются тексты, имеющие отношение к различным искусствам и их синтезу, в частности, есть редкие тексты и комбинаторной поэзии.


Более подробное описание коллекции, а также описание ход работы по загрузке архивов через `wpull` можно найти [в файле по ссылке](./wpull_metawarc/wpull_archiving_D.pdf).
 

## Метод создания и анализа коллекции

В данной работе мы использовали несколько инструментов для создания полноценной коллекции веб-архивов.

**1.** Для каждого архива мы проанаизировали параметры архивируемости сайта с помощью инструмента [ArchiveReady](https://archiveready.com/).

**2.** Для сохранения архива мы воспользовались `wpull`. Этот инструмент представляет из себя утилиту командной строки а также библиотеку `Python` и позволяет загружать архивы с широким выбором заданных параметром (глубина рекурсии, timeout, метаданные архивирующего лица итд). В данной работе для загрузки нескольких архивов последовательно, мы воспользовались `wpull` через `Python`(скрипт массовой загрузки [wpull_mass_DTM](./wpull_mass/wpull_mass_DTM.py)).


### $\color{#9d3dff}\fbox{{\textsf{УСТАНОВКА WPULL}}}$

<mark>Предварительно необходимо установить Python версии ниже 3.7 через pyenv.</mark>


```
python3.6 -m venv venv3.6
source venv3.6/bin/activate

pip3 install tornado==4.5.3
pip3 install sqlalchemy==1.0.13
pip3 install html5lib==0.9999999
pip3 install wpull
pip3 install psutil
pip3 install lxml 
```
$\textcolor{green}{\textsf{NOTE: Перед началом работы необходимо проверить наличие досаточного кол-ва памяти на диске.}}$
$\textcolor{green}{\textsf{Если wpull запущен, он может работать в фоновом режиме, на скачивание "тяжёлых" сайтов может уйти пара суток.}}$
$\textcolor{green}{\textsf{После выхода компьютера из режима "сна", скачивание возобновляется и wpull продолжит работу.}}$



видео
https://github.com/user-attachments/./wpull_metawarc/wpull_arch.mov



**3.** Воспроизвести полученные архивы удалось с помощью сервиса [ReplayWeb.page](https://replayweb.page/).


 ![рисунок replaywebpage_collection](./pictures/replaywebpage_collection.png)

**4.** Наконец, для каждого архива мы произвели анализ метаданных с помощью `Python`-библиотеки `metawarc` (как установить metawarc см. [`тут`](https://github.com/datacoon/metawarc)).




## Структура репозитория

Репозитарий содержит описание работы по сохранению и анализу каждого сайта архивной коллекции.по (см. папку Archives_collection), а также образец скрипта и пример формирования списка сайтов для массового скачивания (см. папку wpull_mass) и общее описание формирования коллекции через wpull и анализа метаданных коллекции через metawarc (см. папку wpull_metawarc).


## Итоги работы

В этой работе я создавала коллекцию сайтов, содержащих стихи русских поэтов, а также биографическую, аналитическую и исследовательскую информацию.
Создание архива коллекции сайтов, связанных с русским поэтическим наследием и литературой, является важной задачей для сохранения культурного наследия. Эти сайты представляют собой уникальные источники информации, включающие редкие материалы.

В конечном сете в архиве удалось сохранить в общей сложности **17,82 Гб** данных, на загрузку ушло **всего 38 часов 29 минут**, скачивание не сопровождалось трудностями или техническими сбоями.
Создание и поддержание такого архива требует внимательного подхода и систематической работы, чтобы обеспечить доступность ценных материалов для будущих поколений.




## Контакты
[Дарья Тюрякова-Матвеева](https://github.com/DariaTM), 
ЦМГН ВШЭ,
2024

## Условия использования 
<p xmlns:cc="http://creativecommons.org/ns#" >Данная работа может свободно распространяться по лицензиии <a href="http://creativecommons.org/publicdomain/zero/1.0?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC0 1.0 Universal<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/zero.svg?ref=chooser-v1"></a></p>