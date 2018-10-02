from setuptools import setup

setup(
   name='Tenable2Trello',
   version='0.1',
   description='Export vulnerabilities from Tenable IO and import into Trello board',
   author='Timothy J. Scott',
   author_email='tim@scott.id.au',
   packages=['Tenable2Trello'],  #same as name
   install_requires=['tenable_io', 'trello'], #external packages as dependencies
)