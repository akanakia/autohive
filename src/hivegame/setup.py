# -*- coding: utf-8 -*-

import setuptools


def read_file(f):
    with open(f, "r") as fp:
        return fp.read()


description = read_file("README.md")
version = read_file("version.txt")

setuptools.setup(
    name="hivegame",
    version=version,
    author="Anshul Kanakia",
    author_email="anshul.p.kanakia@gmail.com",
    long_description=description,
    long_description_content_type="text/markdown",
    package_dir={"", "src"},
    packages=setuptools.find_packages(
        where="src",
        include=[
            "hivegame",
        ],
    ),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Board Games",
    ],
    python_requires=">=3.6",
)
