# Crypto HUB

Данное решение выполняется в качестве дипломного проекта в Otus.

Микросервис для криптографической обработки файлов.
Задание\результат через RMQ
Файлы в S3 minio


Генерация закрытого (приватного) ключа и сертификата
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:4096 -keyout private.pem -out private.crt         
Извлечение открытого ключа
openssl rsa -in private.pem -outform PEM -pubout -out pubkey.pem
Перекодирование сертификата для подписи
openssl x509 -in private.crt -outform pem -out cert.pem   


Подписать
openssl cms -sign -nodetach -in file.txt -out file.txt.sgn -signer cert.pem -inkey private.pem 
Зашифровать
openssl cms -encrypt -in file.txt.sgn -out file.txt.sgn.enc cert.pem
Расшифровать
openssl cms -decrypt -in file.txt.sgn.enc -out file.txt.sgn.enc.dec -inkey private.pem 
Снять подпись
openssl cms -verify -noverify -in file.txt.sgn.enc.dec -out file.txt.sgn.enc.dec.unsgn 

https://opensource.com/article/19/6/cryptography-basics-openssl-part-2