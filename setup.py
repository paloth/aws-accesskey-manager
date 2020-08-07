from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Paloth (https://github.com/paloth)",
    url="https://github.com/paloth/aws-accesskey-manager",
    name="aws-key-management",
    version="1.0",
    description="Manage your personnal access key on AWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test*"]),
    install_requires=["Click", "boto3", "botocore"],
    license="MIT License",
    entry_points="""
    [console_scripts]
    akm2=akm.main:run
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
