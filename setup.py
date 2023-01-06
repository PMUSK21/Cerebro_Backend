from setuptools import setup, find_packages

setup(
  name="Cerebro113_Server",
  version="1.0",
  description='Rest API to enable access to Cerebro 113 commits database.',
  author='Nathan Spencer',
  author_email='nathanspencer97@hotmail.com',
  packages=find_packages(),
  install_requires=[
    "click==8.1.3",
    "colorama==0.4.6",
    "Flask==2.2.2",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "Werkzeug==2.2.2"]
)