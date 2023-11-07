# Crypto HUB

Данное решение выполняется в качестве дипломного проекта в Otus.

Микросервис для криптографической обработки файлов.
Задание\результат через RMQ
Файлы в S3 minio


Генерация закрытого (приватного) ключа 
openssl genrsa -aes128 -out private.pem 1024
Извлечение открытого ключа
openssl rsa -in private.pem -pubout > public.pem

Зашифровать
openssl rsautl -encrypt -inkey public.pem -pubin -in top_secret.txt -out top_secret.enc
Расшифровать
openssl rsautl -decrypt -inkey private.pem -in top_secret.enc > top_secret.txt
Подписать
openssl dgst -sha256 -sign private.pem -out sign.sha256 file.txt
https://opensource.com/article/19/6/cryptography-basics-openssl-part-2