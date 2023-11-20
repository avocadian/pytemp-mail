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
api.custom_email(name='testHogehoge', domain='greencafe24.com')

```
#### *result*
```
{'status': {'code': 200}, 'data': {'email': 'xlomgnzr2v@rfcdrive.com', 'token': 'gT-lF8Zuc32zBq7Ocysc'}} #aaaa
{'status': {'code': 200}, 'data': {'email': 'cisaij11c9wf8csqr0f0xubh9ccczu@sfolkar.com', 'token': '2-gaxp-bH3koXCCdcUoI'}}
{'status': {'code': 200}, 'data': {'email': 'testhogehoge@greencafe24.com', 'token': 'QOSzfJD6huIGmiNiPKSY'}}
{'status': {'code': 200}, 'data': [{'id': 'f1b74906-5b2b-45bc-a7af-af436b7755ea', 'from': '"SendTestEmail" <noreply@sendtestemail.com>', 'to': 'testhogehoge@greencafe24.com', 'cc': None, 'subject': 'SendTestEmail.com - Testing Email ID: 31a2a481809e17f807828c3025dcd4bf', 'body_text': "Congratulations!\n\nIf you are reading this your email address is working.\n\nThis is not spam or a solicitation. This email was sent to your email address because you, or someone else, requested a test email to be sent to this address. We work hard to ensure a balance between testing, transparency, and privacy. If you did not request this email test, it's likely that someone accidentally mistyped their email address as yours. You can request your email address be blocked here: https://sendtestemail.com/block ( https://sendtestemail.com/block )\n\nThe IP address of the requester of this test email is: 146.70.205.148", 'body_html': '<html>\nCongratulations!<br><br>\nIf you are reading this your email address is working.<br><br>\nThis is not spam or a solicitation. This email was sent to your email address because you, or someone else, requested a test email to be sent to this address. We work hard to ensure a balance between testing, transparency, and privacy. If you did not request this email test, it\'s likely that someone accidentally mistyped their email address as yours. You can request your email address be blocked here: <a href="https://sendtestemail.com/block">https://sendtestemail.com/block</a><br><br>\nThe IP address of the requester of this test email is: 146.70.205.148\n</html>\n', 'created_at': '2023-11-20T01:02:28.491168368Z', 'attachments': []}]}
```
