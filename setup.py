from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'TikTakBackEnd',         
  packages = ['TikTakBackEnd'],   
  version = '3.1.1',      
  license='MIT',        
  description = 'The Unofficial backend for the tiktak app. Video platform for adults 35 and over.',   
  author = 'Mike Harley',                   
  author_email = 'info@mike-harley.tech',     
  url = 'https://github.com/mharley/tiktak',
  long_description=long_description,
  long_description_content_type="text/markdown",  
  download_url = 'https://github.com/mharley12345/Tik-Tak', 
  keywords = ['tiktak', 'python3', 'api', 'unofficial', 'tiktak-api'], 
  install_requires=[
          'requests',
          'selenium',
          'asyncio',
          'asyncio',
          'bs4',
          'pyppeteer',
          'pyppeteer_stealth'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.5', 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)