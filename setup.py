from setuptools import setup

setup(
    author="Paloth (https://github.com/paloth)",
    url="https://github.com/paloth/aws-accesskey-manager",
    name="aws-key-management",
    version="1.0",
    description="Manage your personnal access key on AWS",
    packages=["src", "src.cmd", "src.internal"],
    # py_module=["mfa"],
    install_requires=["Click", "boto3", "botocore"],
    license="MIT License",
    entry_points="""
    [console_scripts]
    akm=main:run
    """,
)
