# app_project_01

Django application project

Приложение "Меню" на django

![weather](/image/menu.png)
<br>

Функционал:
<pre>
    - добавление, удаление и изменение объектов меню и дочерних элементов можно делать через панель администратора
    - динамические маршруты в паттерне
    - активный пункт меню определяется исходя из URL текущей страницы
    - выделение активного пункта меню при переходе на него
    - меню на одной странице может быть несколько
    - доступ в панель администратора login: admin, password: admin
</pre>

Развернуто:

![weather](/image/menu_up.png)
<br>

Обновить пакетный менеджер pip:
    
    python -m pip install --upgrade pip

Установить зависимости: 
    
    pip install -r requirements

Запуск приложения:
    
    python manage.py runserver
    
Starting development server at http://127.0.0.1:8000/

![weather](/image/menu_up2.png)

Панель администратора:

![weather](/image/admin_panel.png)
