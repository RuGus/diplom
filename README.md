# Crypto HUB

Данное решение выполняется в качестве дипломного проекта в Otus.

Микросервис для криптографической обработки файлов.
Задание\результат через RMQ
Файлы в S3 minio

## TODO
1. Привести в порядок логи
2. Написать юнит тесты
3. CI/CD
4. Доработать документацию и докстринги
5. Подготовить презентацию для защиты

### Настройки
Настройки задаются через переменные окружения.
Настройки по умолчанию реализованы в settings.py.
### Локальный запуск
Через docker compose
> docker compose up
### Демо прогон
При локальном развертывании в хранилище создается 100 файлов.
Для их обработки можено использовать скрипт scripts/rpc_client.py
> python rpc_client.py

### OpenSSL команды
Генерация закрытого (приватного) ключа и сертификата
>openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:4096 -keyout private.pem -out private.crt         

Извлечение открытого ключа
>openssl rsa -in private.pem -outform PEM -pubout -out pubkey.pem

Перекодирование сертификата для подписи
>openssl x509 -in private.crt -outform pem -out cert.pem   

Подписать
>openssl cms -sign -nodetach -in file.txt -out file.txt.sgn -signer cert.pem -inkey private.pem 

Зашифровать
>openssl cms -encrypt -in file.txt.sgn -out file.txt.sgn.enc cert.pem

Расшифровать
>openssl cms -decrypt -in file.txt.sgn.enc -out file.txt.sgn.enc.dec -inkey private.pem 

Снять подпись
>openssl cms -verify -noverify -in file.txt.sgn.enc.dec -out file.txt.sgn.enc.dec.unsgn 

Полезная статья по openssl
>https://opensource.com/article/19/6/cryptography-basics-openssl-part-2