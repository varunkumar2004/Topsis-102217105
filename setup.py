from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Technique for Order Preference by Similarity to Ideal Solution(TOPSIS) Package'

# Setting up
setup(
    name="topsis-102217105",
    version=VERSION,
    author="Varun Kumar",
    author_email="varunkumar2004.vk@gmail.com",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'openpyxl'],
    keywords=['python', 'topsis', 'multi-criteria decision-making', 'mcdm', 'ranking'],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main'
        ]
    },
    # classifiers=[
    #     "Development Status :: 1 - Planning",
    #     "Intended Audience :: Developers",
    #     "Programming Language :: Python :: 3",
    #     "Operating System :: Unix",
    #     "Operating System :: MacOS :: MacOS X",
    #     "Operating System :: Microsoft :: Windows",
    # ]
)