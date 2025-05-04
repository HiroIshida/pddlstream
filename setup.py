from setuptools import find_packages, setup

setup_requires = []

install_requires = []

setup(
    name="pddlstream",
    version="0.0.0",
    description="",
    author="",
    author_email="",
    install_requires=install_requires,
    packages=find_packages(exclude=("tests", "docs")),
)
