from setuptools import setup, find_packages

setup(
        name='pytemp-mail',
        version='1.0.0',
        packages=find_packages(),
        description='Api of temp-mail.lol',
        url='https://github.com/2-l0/pytemp-mail',
        install_requires=[
            'httpx'
            ],
        )
