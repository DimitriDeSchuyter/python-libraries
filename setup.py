import os
from setuptools import find_packages, setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "depuydt",
    version = "0.0.1",
    author = "Frederic Depuydt",
    author_email = "frederic.depuydt@outlook.com",
    description = ("A basic set of library functions."),
    license = "GPL-3.0",
    keywords = "depuydt libraries",
    url = "https://github.com/fredericdepuydt/python-libraries",    
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    install_requires=["influxdb"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Depuydt libraries",
        "License :: GPL-3.0 License",
    ],
)