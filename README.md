# m-d6-shelter
Study project
Учебный проект "Приют для животных"
к модулю D6
<br><br>
<b>Описание.</b><br>
Простой проект Приют, в шаблоны подключен собраный bootstrap 4.5.1 через static files, для примера натыкано bootstrap разметки, добавлены кнопки для навигации и хедер с картинкой из static files.<br>
В модели добавлено:<br>
    - Вид животного (сейчас попугай, кот, пес, можно добавить новые через админку), порода<br>
    - Несколько дополнительных моделей для разнообразия<br>
    - модель для питомца с загрузкой фото, вывод превью фото в админке<br>
    - CBV для ListView, DetailView для питомцев с фотками<br>
    - добавлено красоты в разметку: красивых табличек для отображения списков, добавлено меню для навигации, стилизованное под вкладки с сохранением активной для текущего выбранного пункта с помощью наследования шаблонов.<br>
    - ListView для одолженных/вернутых книг теперь реализованы через CBV и атрибут queryset<br>
Добавление нового вида животных не требует дополнительных изменений в проекте.
<br>
<b>Системные требовани.</b>
python 3.7+<br>
django 2.2.13+<br>
pillow 7.2.0<br>
<br>
<b>Установка.</b><br>
- скачать, распаковать<br>
- создать виртуальную среду там, куда распаковано<br>
- запустить среду,(для unix-like систем: source bin/activate)<br>
- установить зависимости, (pip install -r requirements.txt)<br>
БД заполнена исходными данными<br>
<br>
<b>Запуск.</b><br>
1. запустить виртуальную среду (source bin/activate),<br>
2. создать суперпользователя, (python manage.py createsuperuser)<br>
3. запустить сервер, (python manage.py runserver)<br>
4. по умолчанию фронтенд доступен по ссылке http://127.0.0.1:8000/<br>
<br>
Для навигации по сайту использовать меню навигации на фронте.<br>
