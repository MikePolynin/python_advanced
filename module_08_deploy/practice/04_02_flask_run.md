#### Урок 4, практика 2
Давайте чуть-чуть плотнее изучим команту `flask run`.

Запуская приложение мы можем указывать `host` (как мы это делали) и `port`. Давайте попрактикуемся.

Запустите `hello_world` приложение на порту `5555`, `8080` используя аргумент `-p` у `flask run`.
    Каждый раз проверяйте, что приложение открывается через браузер.
    
В web разработке есть 2 особенных порта: `:80` и `:443`.
Первый из них - порт по умолчанию для протокола `http`, второй -- для протокола `https`.

Давайте попробуем запустить наш flask web сервер на порту `:80`
    (для того чтобы запустить приложение на этом порту потребуется запускать `flask run`
     с помощью `sudo`).

А теперь проверьте, что ваше web приложение открывается в браузере НЕ указывая порт. Работает!

Теперь когда вы открываете какой то сайт по протоколу `http` (например [http://example.com]), знайте,
    что вы обращаетесь к `:80`ому порту web сервера, на котором крутится сайт.

Ещё одна небольшая хитрость. Работая на незнакомом сервере мы можем не знать какой `host`
    правильно передать команде `flask run`.

В таком случае нас выручит маленькая хитрость. Мы можем задать специальный `host` `0.0.0.0`
    и тогда `flask` запустит приложение на всех доступных хостах.

Попробуйте стартануть приложение на хосту `0.0.0.0` и посмотрите как это работает.

Вы можете почитать больше про хост `0.0.0.0` в статье на английской википедии:
    [https://en.wikipedia.org/wiki/0.0.0.0] и по ссылкам
    [раз](https://www.lifewire.com/four-zero-ip-address-818384) и
    [два](https://www.howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0/)
    (особенно я рекомендую вторую статью, раньше вопрос 
    "в чём разница между 0.0.0.0 и 127.0.0.1" был популярен на собеседованиях)