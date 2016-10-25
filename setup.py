from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./test')

setup(
    name='Futhon',
    version='0.0.1',
    description='Lisp with power of Python',
    long_description='Futhon is a Lisp designed for Natural Language Processing and Machine Learning.',
    author='delihiros',
    author_email='delihiros@gmail.com',
    url='futhon.delihiros.jp',
    license='MIT License',
    packages=find_packages(),
    test_suite='futhon_test.suite',
    platforms='requires Python 3'
)
