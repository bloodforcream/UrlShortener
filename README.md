## Инструкция по установке
```
Создать .env file

MYSQL_ROOT_PASSWORD={}
MYSQL_DATABASE={}
MYSQL_USER={}
MYSQL_PASSWORD={}
SECRET_KEY={}
```
```
docker-compose up -d --build
```

## Основные методы

### GET /
Главная страница со всеми url правилами пользователя и формой для добавления новых

### POST /
Добавление нового url правила

### GET r/{url_subpart}/
Переход на оригинальный url указанного {url_subpart}
