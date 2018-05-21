from setuptools import setup

setup(
    name='imagehoster',
    version='0.0.1',
    packages=["imagehoster",],
    url='http://github.com/emre/imagehoster-python-clilent',
    license='MIT',
    author='emre yilmaz',
    author_email='mail@emreyilmaz.me',
    description='Steemit Image Hoster Python Client',
    entry_points={
        'console_scripts': [
            'imagehoster = imagehoster.upload:cli',
        ],
    },
    install_requires=["requests", "steem"]
)