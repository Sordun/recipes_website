## Книга рецептов

Пользователь может просматривать доступные рецепты и искать их по названию рецепта и по ингредиентам.

Также пользователь может добавлять новые рецепты.

Проект разработан на фреймворке Django 3.2.8, в качестве базы данных используется PostgreSQL 14. Для приложения создан
Docker контейнер.

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```
При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```

#### Применение миграций:

```bash
python manage.py migrate
```

#### Сборка статики:

```bash
python manage.py collectstatic
```

#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

#### Добавление фикстур

```bash
python manage.py loaddata ingredients
```

Проект доступен по адресу http://127.0.0.1:8000
