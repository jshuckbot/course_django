# course_django

## Урок 1. Первое Знакомство с Django

**Задание**
Создайте пару представлений в вашем первом приложении:

- главная
- о себе.
  Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем
  первом Django-сайте и о вас.
  Сохраняйте в логи данные о посещении страниц. [Решение](aboutmeapp)

## Урок 2. Django ORM и связи

**Задание**
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
Поля модели «Клиент»:

- имя клиента
- электронная почта клиента
- номер телефона клиента
- адрес клиента
- дата регистрации клиента

Поля модели «Товар»:

- название товара
- описание товара
- цена товара
- количество товара
- дата добавления товара

Поля модели «Заказ»:

- связь с моделью «Клиент», указывает на клиента, сделавшего заказ
- связь с моделью «Товар», указывает на товары, входящие в заказ
- общая сумма заказа
- дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой
бд. [Решение](shopapp)

## Урок 3. Шаблоны, классы и формы

**Задание**
Продолжаем работать с товарами и заказами.
Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:

- за последние 7 дней (неделю)
- за последние 30 дней (месяц)
- за последние 365 дней (год)
  <br>*Товары в списке не должны повторятся. [Решение](shopapp/views.py)

## Урок 4. Оптимизация проекта

**Задание**

- Измените модель продукта, добавьте поле для хранения фотографии продукта.
- Создайте форму, которая позволит сохранять фото. [Решение](shopapp)

## Урок 5. Административная панель

**Задание**

- Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации об объекте и
  вывода списка объектов. [Решение](shopapp)

## Урок 6. Административная панель

**Задание**

- Настроить работу проекта на сервере. [Решение](shopapp)
