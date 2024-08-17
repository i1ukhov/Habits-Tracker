В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.
## Модели

В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

```
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
```

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка».

### Привычка:

- Пользователь — создатель привычки.
- Место — место, в котором необходимо выполнять привычку.
- Время — время, когда необходимо выполнять привычку.
- Действие — действие, которое представляет собой привычка.
- Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
- Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
- Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

## Запуск проекта (в PyCharm)
1. Заполните файл .env по шаблону.
2. Установите зависимости из requerments.txt.
3. Запустите Redis.
4. Запустите проект Django.
## Запуск проекта (Docker)
1. Заполните файл .env по шаблону.
2. Управление с помощью команд:

`docker-compose up` – запуск проекта

`docker-compose up -d` – запуск в режиме демона

`docker-compose up -d` – запуск в режиме демона

`docker-compose down` – для остановки с удалением контейнеров 
## Покрытие тестами
![test coverage](https://github.com/user-attachments/assets/2f0cc586-69c2-4e73-84d6-1d1de8723b17)


## Критерии приёмки
- [ ] Настроили CORS.
- [ ] Настроили интеграцию с Телеграмом.
- [ ] Реализовали пагинацию.
- [ ] Использовали переменные окружения.
- [ ] Все необходимые модели описаны или переопределены.
- [ ] Все необходимые эндпоинты реализовали.
- [ ] Настроили все необходимые валидаторы.
- [ ] Описанные права доступа заложены.
- [ ] Настроили отложенную задачу через Celery.
- [ ] Проект покрыли тестами как минимум на 80%.
- [ ] Код оформили в соответствии с лучшими практиками.
- [ ] Имеется список зависимостей.
- [ ] Результат проверки Flake8 равен 100%, при исключении миграций.
- [ ] Решение выложили на GitHub.
  
