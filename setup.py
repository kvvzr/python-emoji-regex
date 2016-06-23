from setuptools import setup, find_packages
import sys

setup(
    name='python-emoji-regex',
    version='0.0.1',
    packages=find_packages(),
    package_data={'emoji_regex': ['emojis.txt', 'emojis.v2.txt']},
    test_suite = 'tests'
)
