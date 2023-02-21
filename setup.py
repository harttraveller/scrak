from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="kamaji",
    version="0.0.0",
    author="Hart Traveller",
    url="https://github.com/harttraveller/kamaji",
    license="MIT",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["rich", "requests"],
    entry_points={"console_scripts": ["kamaji=kamaji.cli:cli"]},
)