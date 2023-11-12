import httpx


class api:
    def __init__(self):
        self.endpoint = 'api.internal.temp-mail.io'
        self.url = f'https://{self.endpoint}/api/v3/email'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
                'Content-Type': 'application/json;charset=utf-8',
                'Referer': 'https://temp-mail.io/',
                'Application-Name': 'web',
                'Application-Version': '2.3.5',
                'Origin': 'https://temp-mail.io',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Connection': 'keep-alive',
            }

    def random_email(self, name_length: int = None):
        if self.name_length is None:
            r = httpx.post(
                    f'{self.url}/new',
                    headers=self.headers,
                    json={
                        'min_name_length': 10,
                        'max_name_length': 10,
                        }
                    )
            print({'status': {'code': self.r.status_code},
                    'data': self.r.json()})
        else:
            r = httpx.post(
                    f'{self.url}/new',
                    headers=headers,
                    json={
                        'min_name_length': self.name_length,
                        'max_name_length': self.name_length
                        }
                    )
            print({'status': {'code': self.r.status_code},
                    'data': self.r.json()})

    def custom_email(self, name: str, domain: str):
        r = httpx.post(
                f'{self.url}/new',
                headers=self.headers,
                json={
                    'name': self.name,
                    'domain': self.domain
                    }
                )
        print({'status': {'code': self.r.status_code},
                'data': self.r.json()})

    def messages(self, email: str):
        r = httpx.get(
                f'{self.url}/{self.email}/messages',
                headers=self.headers
                )
        print({'status': {'code': self.r.status_code},
                'data': self.r.json()})
    
    def email_delete(self, email: str, token: str):
        with httpx.Client() as client:
            r = self.client.request(
                    "DELETE", f'{self.url}/{self.email}',
                    headers=self.headers, 
                    json={'token': self.token}
                    )
        print({'status': {'code': self.r.status_code}})

