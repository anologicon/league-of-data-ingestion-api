import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Paulo Raimundi',
    author_email='pauloraimundi2009@gmail.com',
    description='A league of legends API tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anologicon/league-of-data-ingestion-api',
    project_urls={
        "Bug Tracker": "https://github.com/anologicon/league-of-data-ingestion-api/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'dotenv',
        'backoff',
        'ratelimit'
    ],
)
