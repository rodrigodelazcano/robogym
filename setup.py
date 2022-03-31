#!/usr/bin/env python3
from setuptools import find_packages, setup


def setup_robogym():
    setup(
        name="robogym",
        version=open("ROBOGYM_VERSION").read(),
        packages=find_packages(),
        install_requires=[
        ],
        python_requires=">=3.7.4",
        description="OpenAI Robogym Robotics Environments",
        include_package_data=True,
    )


setup_robogym()
