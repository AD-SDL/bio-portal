import os
from setuptools import setup, find_packages

version_ns = {}
with open(os.path.join("bio_portal", "version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns["__version__"]

install_requires = []
with open("requirements.txt") as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith("#"):
            continue
        install_requires.append(req)


setup(
    name="bio_portal",
    description="A portal for RPL",
    url="https://github.com/AD-SDL/bio-portal",
    maintainer="The Gladier Team",
    maintainer_email="",
    version=version,
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[],
    license="Apache 2.0",
    classifiers=[],
)
