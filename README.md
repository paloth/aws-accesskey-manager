# AWS authentication CLI

## Project

The project will be completly refactored.
I will build a CLI with the click library.

You can use differents arguments like:

| argument  | shortcut | description                                      |
| --------- | -------- | ------------------------------------------------ |
| --help    | -h       | Show this help message and exit                  |
| --user    | -u       | A valid user name on aws                         |
| --token   | -t       | A valid token (Must be 6 digits)                 |
| --profile | -p       | A valid profile present in your .aws/credentials |

Example: `aws-mfa-cli -p MyProfile -u UserName -t 000000`

If one value is not valide in arguments, you will be prompted to enter a valid value

At the end, it will return the temporary credential and will write it into the aws credentials configuration file as `profile-tmp`

## Installation

To install the package, clone the repo then execute the following commands:

```shell
cd aws-accesskey-manager
pip install .
```

## To do list

- [ ] Add more error handling
- [ ] Add a valid CI for test
- [ ] Add test
- [x] Add arguments management
- [ ] Add options
  - [ ] Generate temporary key
  - [ ] Check and renew access key
  - [ ] Show Profile available
