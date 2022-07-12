from setuptools import setup, find_packages

setup(
    name="improved-diffusion",
    packages=find_packages(),
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
    license=("LICENSE"),
    version="0.0.1",
)
