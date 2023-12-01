# pytemp-mail
Api of temp-mail.io

## Explanation about
This is an unofficial API wrapper for https://temp-mail.io/
You can create an email address, receive messages, etc.

## Install
`pip install git+https://github.com/2-l0/pytemp-mail.git`

# Instructions
### *sample code*
```py
import tempmail

api = tempmail.api()

random_email = api.random_email()
30_length_email = api.random_email(30)
custom_email = api.custom_email(name='testhogehoge', domain='greencafe24.com')
message = api.messages(email='testhogehoge@greencafe24.com')
email_delete = api.email_delete(email='testhogehoge@greencafe24.com', token='QOSzfJD6huIGmiNiPKSY')
domains = api.domains()
```
### *result*
```
{'status': {'code': 200}, 'data': {'email': 'xlomgnzr2v@rfcdrive.com', 'token': 'gT-lF8Zuc32zBq7Ocysc'}}
{'status': {'code': 200}, 'data': {'email': 'cisaij11c9wf8csqr0f0xubh9ccczu@sfolkar.com', 'token': '2-gaxp-bH3koXCCdcUoI'}}
{'status': {'code': 200}, 'data': {'email': 'testhogehoge@greencafe24.com', 'token': 'QOSzfJD6huIGmiNiPKSY'}}
{'status': {'code': 200}, 'data': [message received]}
{'status': {'code': 200}}
['greencafe24.com', 'waterisgone.com', 'superblohey.com', 'happy2023year.com', 'gixenmixen.com', 'bloheyz.com', 'zipcatfish.com', 'myinfoinc.com', 'skygazerhub.com', 'sfolkar.com', 'pirolsnet.com', 'rentforsale7.com', 'tippabble.com', 'rfcdrive.com']
```
