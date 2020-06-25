# AWS authentication CLI

## Installation

To install the package, clone the repo then execute the following commands:

```shell
cd aws-accesskey-manager
pip install .
```

## How to use

### Generate

The generate command will request to aws a set of temporary credentials with mfa.

You can use differents arguments:

| argument  | shortcut | description                                      |
| --------- | -------- | ------------------------------------------------ |
| --help    | -h       | Show this help message and exit                  |
| --user    | -u       | A valid user name on aws                         |
| --token   | -t       | A valid token (Must be 6 digits)                 |
| --profile | -p       | A valid profile present in your .aws/credentials |

Example: `akm generate -p MyProfile -u UserName -t 000000`

It will return the temporary credentials and will write it into the aws credentials configuration file as `profile-tmp`

If your token does not match the regex, you will be prompted to enter a valid token.
