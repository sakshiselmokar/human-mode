from setuptools import setup, find_packages

setup(
    name="human-mode",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "human=human_mode.cli:handle_command"
        ]
    },
    author="Sakshi Selmokar",
    description="A smart CLI tool to remind you to be human",
)