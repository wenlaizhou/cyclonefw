from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='cyclonefw',
    version='1.0.17',
    description='Cyclone Python Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wenlaizhou/cyclonefw',
    author='CODAIT',
    author_email='',
    license='Apache',
    packages=['cyclonefw', 'cyclonefw.core', 'cyclonefw.model', 'cyclonefw.utils'],
    zip_safe=True,
    install_requires=[
        'requests',
        'flask-restplus',
        'flask-restx==0.1.1',
        'flask-cors==3.0.9',
    ],
    test_suite='nose.collector',
    tests_require=['nose']
)
