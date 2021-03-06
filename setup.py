#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="threefive",
    version="2.1.91",
    author="fu-corp",
    author_email="spam@futzu.com",
    description="A Fast SCTE 35 Decoder for Mpeg-TS Video, and Base64 or Hex Encoded Messages.", 
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/SCTE35-threefive",
    packages=setuptools.find_packages(),
    install_requires=["bitn>=0.0.29",],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    python_requires=">=3.6",
   
)
