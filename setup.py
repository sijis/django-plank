from setuptools import setup, find_packages

setup(
    name='django-plank',
    version = '0.1',
    description = 'A django based status board with an api.',
    long_description = open('README.rst').read(),
    author = 'Sijis Aviles',
    author_email = 'sijis.aviles@gmail.com',
    packages = find_packages(),
    install_requires=[
        'django>=1.5.1',
        'south>=0.7.6',
        'django-tastypie>=0.9.14',
    ],
    keywords = 'django status board',
    url = 'https://github.com/sijis/django-plank',
    download_url = 'https://github.com/sijis/django-plank',
    platforms = ['OS Independent'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
