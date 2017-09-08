from setuptools import setup

setup(
    name='sentiment',
    packages=['sentiment'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'flask-jwt-extended',
        'passlib',
        'bcrypt'
    ],
    tests_require=[
        'pytest'
    ]
)
