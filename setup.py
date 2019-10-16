from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="jinjatex",
    version="0.0.1",
    author="Vincent Leroy",
    author_email="maelkoth2@hotmail.fr",
    description="LaTeX Jinja template expansion tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/momom4urice/jinjatex",
    packages=find_packages(),
    install_requires=["jinja2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
