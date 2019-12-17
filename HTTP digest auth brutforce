# -*- coding: utf-8 -*-
############################################################################
"""
HTTP Digest Auth - строка, которая отправляется на сервер рассчитывается следующим образом
1. MD5 от комбинации username; realm; password, результат представляется как HA1.
2. MD5 от комбинации метода digest + URi
пример: "GET" и "/dir/index.html" результат представляется как HA2
3. MD5 от комбинации HA1, nonce,request counter(nc), cnonce, qop, HA2; результат является ответом предоставленным
клиентом.
Все комбинации идут через ":"!!!
HTTP Digest Auth - the line that is sent to the server is calculated as follows
1. MD5 from username combination; realm; password, the result is represented as HA1.
2. MD5 from a combination of the digest + URi method
example: "GET" and "/dir/index.html" the result is represented as HA2
3. MD5 from a combination of HA1, nonce, request counter (nc), cnonce, qop, HA2; the result is the answer provided
by customer.
All combinations go through ":" !!!
"""
method = "GET"
uri = "/"
username = "admin"
realm = "Private Area"
nonce = "1447149417"
nc = "00000001"
cnonce = "69dd8dd24dd85752"
qop = "auth"
response = "a36f9b9239f1c8bf427f9a66db2a9e90"

############################################################################

import hashlib


stroka_h2 = '{0}:{1}'.format(method, uri)
password = open('passwords.txt').read().splitlines()
print(stroka_h2)
h2 = hashlib.md5(stroka_h2.encode('utf-8')).hexdigest()
# print(h2)
for i in range(len(password)):
    stroka_h1 = '{0}:{1}:{2}'.format(username, realm, password[i])
    #print(stroka_h1)
    h1 = hashlib.md5(stroka_h1.encode('utf-8')).hexdigest()
    stroka_result = '{0}:{1}:{2}:{3}:{4}:{5}'.format(h1, nonce, nc, cnonce, qop, h2)
    #print(stroka_result)
    result = hashlib.md5(stroka_result.encode('utf-8')).hexdigest()
    #print(result)
    if result == response:
        print("[*] Password found: " + password[i])
        exit()
