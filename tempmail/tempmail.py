import httpx


class api:
    def __init__(self):
        self.host = 'api.internal.temp-mail.io'
        self.url = f'https://{self.host}/api/v3/email'
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
        if name_length is None:
            r = httpx.post(
                    f'{self.url}/new',
                    headers=self.headers,
                    json={
                        'min_name_length': 10,
                        'max_name_length': 10,
                        }
                    )
            print({'status': {'code': r.status_code},
                    'data': r.json()})
        else:
            r = httpx.post(
                    f'{self.url}/new',
                    headers=self.headers,
                    json={
                        'min_name_length': name_length,
                        'max_name_length': name_length
                        }
                    )
            print({'status': {'code': r.status_code},
                    'data': r.json()})

    def custom_email(self, name: str, domain: str):
        r = httpx.post(
                f'{self.url}/new',
                headers=self.headers,
                json={
                    'name': name,
                    'domain': domain
                    }
                )
        print({'status': {'code': r.status_code},
                'data': r.json()})

    def messages(self, email: str):
        r = httpx.get(
                f'{self.url}/{email}/messages',
                headers=self.headers
                )
        print({'status': {'code': r.status_code},
                'data': r.json()})
    
    def email_delete(self, email: str, token: str):
        with httpx.Client() as client:
            r = client.request(
                    "DELETE", f'{self.url}/{email}',
                    headers=self.headers, 
                    json={'token': token}
                    )
        print({'status': {'code': r.status_code}})

    def domains(self):
        domain_list = [
                 'greencafe24.com',
                 'waterisgone.com',
                 'superblohey.com',
                 'happy2023year.com',
                 'gixenmixen.com',
                 'bloheyz.com',
                 'zipcatfish.com',
                 'myinfoinc.com',
                 'skygazerhub.com',
                 'sfolkar.com',
                 'pirolsnet.com',
                 'rentforsale7.com',
                 'tippabble.com',
                 'rfcdrive.com',
                ]
        print(domain_list)
