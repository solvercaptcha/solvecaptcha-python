#!/usr/bin/env python3

from setuptools import setup, find_packages
import re

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    with open('solvecaptcha/__init__.py', 'r') as f:
        return re.search(r'__version__ = ["\'](.*?)["\']', f.read()).group(1)


setup(name='solvecaptcha-python',
      version=get_version(),
      description='Python module for easy integration with solvecaptcha.com API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/solvercaptcha/solvecaptcha-python/',
      install_requires=['requests'],
      author='solvecaptcha.com',
      author_email='info@solvecaptcha.com',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Scientific/Engineering :: Image Recognition",
          "Topic :: Utilities",
          "Intended Audience :: Developers",
      ],
      keywords=[
          'solvecaptcha', 'captcha', 'api', 'captcha solver', 'reCAPTCHA',
          'FunCaptcha', 'Geetest', 'image captcha', 'Coordinates', 'Click Captcha',
          'Geetest V4', 'Lemin captcha', 'Amazon WAF', 'Cloudflare Turnstile',
          'hcaptcha'],
      python_requires='>=3.6',
      test_suite='tests')
