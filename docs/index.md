# AKM (AWS Key Manager)

## Installation

To install the package, download the latest release and execute the following commands:

```shell
pip install aws-key-manager-*.tar.gz
```

## How to use

### Commands

This is the list of the differents commands available:

- **mfa**
  - Generate a temporary token with mfa
- **rotate**
  - Rotate your personnal access key

#### MFA

The **mfa** command will request to aws a set of temporary credentials with mfa.

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

#### Rotate

The **rotate** command check your current access key age, creates a new access key on AWS if the current expired and change it automatically on your local profile.

You can use differents arguments:

| argument     | shortcut | description                                                                          |
| ------------ | -------- | ------------------------------------------------------------------------------------ |
| --help       | -h       | Show this help message and exit                                                      |
| --expire     | -e       | Number of day before the access key must be change. **90 days** by default           |
| --user       | -u       | AWS user name to use                                                                 |
| --profile    | -p       | AWS profile to use. Take your **current active profile** or '**default**' by default |
| --deactivate | -d       | Deactivate the old Access Key instead of delete it. **False** by default             |
| --yes        | -y       | Validate action without prompt. **False** by default                                 |

Example: `akm rotate -p MyProfile -u UserName`
