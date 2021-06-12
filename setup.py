from setuptools import setup, find_packages


dependencies = [
    'gunicorn',
    'iniconfig == 1.1.1',
    'packaging == 20.9',
    'py == 1.10.0',
    'pyparsing == 2.4.7',
    'pytest == 6.2.2',
    'bddrest == 2.6.2',
    'nanohttp == 1.11.11',
    'restfulpy == 3.8.0',
]


setup(
    name='tiger',
    version=0,
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tiger = tiger:tiger.cli_main'
        ]
    }
)

