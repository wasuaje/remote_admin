#!/usr/bin/env python
 
"""
    setup script for pyssh
 
"""
import sys, re

pat="([0-9.]*)"
ver=re.compile(pat)
pyver = ver.match(sys.version).groups()[0]

from distutils.core import setup, Extension  

            
setup(name="pyssh-"+pyver,
      version="0.3",
      description="Python library for programmatically controlling ssh and scp",
      author="Mark W. Alexander",
      author_email="slash@notnetslash.net",
      packages = ["pyssh"])

