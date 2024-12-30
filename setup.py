from setuptools import setup, find_packages

setup(
    name='hwcicdnew',
    version='0.1',
    description='Simple Flask Math App',
    author='Oleg Prizov',
    author_email='oleg12345prisov@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask==3.1.0',
    ],
    entry_points={
        'console_scripts': [
            'hwcicdnew=app:main',
        ],
    },
)
