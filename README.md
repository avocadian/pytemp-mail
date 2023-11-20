# pytemp-mail
Api of temp-mail.lol

## Explanation about
This is an unofficial API wrapper for https://temp-mail.io/
You can create an email address, receive messages, etc.

## Install
`pip install git+https://github.com/2-l0/pytemp-mail.git`

# Instructions
### *Generate email address*
```py
import tempmail

api = tempmail.api()
api.random_email()
api.random_email(30)
```
result
>>>{'status': {'code': 200}, 'data': {'email': 'xlomgnzr2v@rfcdrive.com', 'token': 'gT-lF8Zuc32zBq7Ocysc'}}
