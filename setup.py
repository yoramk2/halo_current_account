from io import open

from setuptools import setup

# python setup.py sdist --formats=zip
# python setup.py sdist bdist_wheel
# twine upload dist/halolib-0.13.8.tar.gz -r pypitest

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='halo_current_account',
    version='0.11.01',
    packages=['halo_current_account_service'],
    package_dir={'halo_current_account_service': 'halo_current_account_service'},
    url='https://github.com/yoramk2/halo_current_account',
    license='MIT License',
    author='yoramk2',
    author_email='yoramk2@yahoo.com',
    description='this is the Halo halo_current_account_service library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
