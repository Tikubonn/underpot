
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
  long_description = readme.read()

setup(
  name="underpot",
  version="2.0.0",
  description="this package provide utility for saving data with encryption.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="tikubonn",
  author_email="https://twitter.com/tikubonn",
  url="https://github.com/tikubonn/underpot",
  license="MIT",
  packages=find_packages(),
  install_requires=[
    "pycryptodomex",
  ],
  dependency_links=[],
  entry_points={},
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
  ],
  test_suite="test"
)
