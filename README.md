# AWS authentication CLI

[![codecov](https://codecov.io/gh/paloth/aws-accesskey-manager/branch/master/graph/badge.svg)](https://codecov.io/gh/paloth/aws-accesskey-manager) [![Maintainability](https://api.codeclimate.com/v1/badges/440e2e5ab3eb7dad26b9/maintainability)](https://codeclimate.com/github/paloth/aws-accesskey-manager/maintainability)

## Installation

To install the package, download the latest release and execute the following commands:

```shell
pip install aws-key-manager-*.tar.gz
```

## How to use

## Commands

This is the list of the differents commands available:

- config  Create a configuration to manage your personnal access key
- mfa     Generate a temporary token with mfa
- rotate  Rotate your personnal access key

### MFA

The mfa command will request to aws a set of temporary credentials with mfa.

You can use differents arguments:

| argument  | shortcut | description                                      |
| --------- | -------- | ------------------------------------------------ |
| --help    | -h       | Show this help message and exit                  |
| --user    | -u       | A valid user name on aws                         |
| --token   | -t       | A valid token (Must be 6 digits)                 |
| --profile | -p       | A valid profile present in your .aws/credentials |

Example: `akm mfa -p MyProfile -u UserName -t 000000`

It will return the temporary credentials and will write it into the aws credentials configuration file as `profile-tmp`

If your token does not match the regex, you will be prompted to enter a valid token.

### Config

Not implemented yet

### Rotate

Not implemented yet
