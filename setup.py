from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now
# 1) we have a top level README file, and 
# 2) it's easier to type in the README file than to put a raw string in below.

# read the contents of  README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name = "opcodify",
    version ="0.1.2",
    author = "Sumit Banik",
    author_email = "sumitbanik02@gmail.com",
    description = "opcodify is a command-line tool designed to simplify the process of visualizing Opcodes within Solidity Smart Contracts. With opcodify, you can effortlessly generate treemap visualizations that provide insights into the distribution of opcodes used within your contracts.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=["py-solc-x", "matplotlib", "seaborn", "squarify"],
    entry_points={
        "console_scripts": ["opcodify=opcodify.cli:main"]
    },
)
