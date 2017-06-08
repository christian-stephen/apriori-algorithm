from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='apriori',
    version='1.0',
    description='An implementation of the Apriori algorithm for association rule mining',
    long_description=long_description,
    author='Christian Stephen',
    author_email='chrisj.stephen2@gmail.com',
    license='MIT',
    py_modules=['apriori', 'export_result', 'generate_candidates', 'generate_rules',
                'load_database', 'prune_itemsets']
)
