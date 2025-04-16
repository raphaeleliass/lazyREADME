"""Configuração do pacote lazyREADME."""

from setuptools import setup, find_namespace_packages

setup(
    name="lazyreadme",
    version="1.0.5",
    description="Gerador automático de README para seus projetos",
    author="Raphael Elias",
    author_email="raphaeleliass@outlook.com",
    packages=find_namespace_packages(where="src", include=["lazyreadme*"]),
    package_dir={"": "src"},
    install_requires=[
        "questionary>=2.0.1",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "lazyreadme=lazyreadme.cli.interface:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Documentation",
    ],
)
