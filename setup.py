from setuptools import setup, find_packages

setup(
    name="opcodify",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["py-solc-x", "matplotlib", "seaborn", "squarify"],
    entry_points={
        "console_scripts": ["opcodify=opcodify.cli:main"]
    },
)
