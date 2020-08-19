# Rotate

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

Example:

```shell
akm rotate -p MyProfile -u UserName
```
