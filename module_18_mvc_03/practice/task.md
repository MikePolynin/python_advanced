### 1


Мы забыли указать тело ответа в случае ошибки валидации. Давайте исправим это упущение и добавим еще один ключ в словарь responses метода post.


### 2 

Убедитесь в том, что скрывается за параметром json метода post:
перепишите ендпоинт так, чтобы вы сами отправляли сериализованную строку. И не забудьте указать MIME type
