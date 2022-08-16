from setuptools import setup

setup(
    name='rotations',
    version='1.0.0',
    packages=["rotations"],
    install_requires=["numpy", "astropy"],
    tests_require=["nose","coverage"],
)