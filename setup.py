import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='leagueapi',
    version='0.0.3',
    zip_safe=False,
    python_requires=">=3.6",
    description='A league of legends API tools',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'python-dotenv',
        'backoff',
        'ratelimit'
    ],
)
