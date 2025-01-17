from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Technique for Order Preference by Similarity to Ideal Solution(TOPSIS) Package'
LONG_DESCRIPTION = 'The TOPSIS package is a Python library that implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). This method is commonly used in multi-criteria decision-making (MCDM) problems, where you need to evaluate a set of alternatives based on multiple criteria or attributes. The goal is to rank the alternatives and choose the best one, considering their proximity to an "ideal" solution and their distance from a "worst" solution.'

# Setting up
setup(
    name="topsis-102217105",
    version=VERSION,
    author="Varun Kumar",
    author_email="varunkumar2004.vk@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'topsis', 'multi-criteria decision-making', 'mcdm', 'ranking'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)