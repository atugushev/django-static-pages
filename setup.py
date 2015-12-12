import os
import re
from setuptools import setup, find_packages

VERSION = re.search(
    r"VERSION\s*=\s*['\"](.*)['\"]",
    open(os.path.join(os.path.dirname(__file__), 'static_pages', '__init__.py')).read()
).group(1)

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-static-pages',
    version=VERSION,
    packages=find_packages(),
    install_requires=['Django>=1.5'],
    test_suite="static_pages.tests.runner.runtests",
    include_package_data=True,
    license='MIT License',
    description='A reusable Django app that generates static pages using Django test client',
    long_description=README,
    url='https://github.com/atugushev/django-static-pages',
    author='Albert Tugushev',
    author_email='albert@tugushev.ru',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
