from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jinjatex",
    version="1.0.0",
    author="Vincent Leroy",
    author_email="maelkoth2@hotmail.fr",
    description="LaTeX Jinja template expansion tools",
    long_description=fh,
    packages=find_packages(),
    install_requires=["jinja2"]
)
