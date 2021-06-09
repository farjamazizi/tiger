from setuptools import setup, find_packages


dependencies = [
    'gunicorn',
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

