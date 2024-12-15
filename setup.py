from setuptools import setup, find_packages

setup(
    name="mdconverter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "markitdown",
        "click"
    ],
    entry_points={
        'console_scripts': [
            'mdconverter=mdconverter.cli:main',
        ],
    },
)
