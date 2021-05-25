# Pooling
    Задание: cпроектировать и разработать API для системы опросов пользователей.  
#### Install require:  
* python3.8
* Django2.2.10
* Django restframework

### Install Guide:  
    pipenv sync  
    pipenv shell
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
#### API Doc:  


### Создать Опросник:
* Request method: POST
* URL: http://localhost:8000/api/poll/create_poll/
* Header:
   *  Authorization: Token userToken
* Body:
    * poll_name: name of polls
    * date_start: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    * date_end: poll end date, format: YYYY-MM-DD HH:MM:SS
    * description: description of polls  
    
* Например: 
 ````
curl --location --request POST 'http://localhost:8000/api/poll/create/' \
--header 'Authorization: Token %userToken' \
--form 'name=%name' \
--form 'date_start=%date_start' \
--form 'date_end=%date_end \
--form 'description=%description'
````  


### Обновить Опросник:
* Request method: PATCH
* URL: http://localhost:8000/api/poll/update_poll/[poll_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id 
* Body:
    * poll_name: name of polls
    * date_start: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    * date_end: poll end date, format: YYYY-MM-DD HH:MM:SS
    * description: description of polls  
* Например:
```
curl --location --request PATCH 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken' \
--form 'name=%name' \
--form 'date_end=%date_end \
--form 'description=%description'
```


### Удаление опросника:
* Request method: DELETE
* URL: http://localhost:8000/api/poll/update_poll/[poll_id]
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
* Например:
```
curl --location --request DELETE 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken'  
```  

###  Чтобы посмотреь все опросы:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/
* Header:
    * Authorization: Token userToken
* Например:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/' \
--header 'Authorization: Token %userToken'
```

### Актуальные опросники:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/active_pools/
* Header:
    * Authorization: Token userToken
* Например:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/active/' \
--header 'Authorization: Token %userToken'
```  

### Создать ответ:
* Request method: POST
* URL: http://localhost:8000/api/question/create_question/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll 
    * question_text: 
    * question_type: can be only `one`, `multiple` or `text`
* Например:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Обновить вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update_question/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * poll: id of poll 
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Например:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Удалить вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update_question/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Например:
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```


### Создать выборку:
* Request method: POST
* URL: http://localhost:8000/api/choice/create_choice/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Например:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```


### Обновить выборку:
* Request method: PATCH
* URL: http://localhost:8000/api/choice/update_choice/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Например:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```
### Удалить выборку:
* Request method: DELETE
* URL: http://localhost:8000/api/choice/update_choice/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Например:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```


### Создать ответ:
* Request method: POST
* URL: http://localhost:8000/api/answer/create_answer/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Например:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Обновить ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update_answer/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Например:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```


### Удалить ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/update_answer/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```
### Посмотреть ответ usera:
* Request method: GET
* URL: http://localhost:8000/api/answer/view_answer/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
```
