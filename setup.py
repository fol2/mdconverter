from setuptools import setup, find_packages

setup(
    name="mdconverter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "markitdown"
    ],
    entry_points={
        'console_scripts': [
            'mdconverter=mdconverter.cli:main',
        ],
    },
    author="James To",
    description="Convert documents to Markdown format",
    python_requires=">=3.7",
)
