# Ermetic Python Collection

## Setup

- Clone the repo to your local machine
- Rename the `.env.sample` file to `.env`
- Add the `ERMETIC_URL` and `ERMETIC_TOKEN` values to the `.env` file
- Ensure you add the directory to the `PYTHONPATH` environment variable. Instructions [here](https://www.simplilearn.com/tutorials/python-tutorial/python-path)
- It's recommended to setup a venv:
  - [Vscode](https://code.visualstudio.com/docs/python/environments#_creating-environments)
  - [CLI](https://docs.python.org/3/library/venv.html)

## CLI Commands

### Account Management

#### AWS Accounts

`get_aws_accounts`'

This function will print out a csv report of either connected AWS accounts without issues, connected accounts with issues, or disconnected accounts. It will have the reason for why the account is disconnected, and issues for accounts with partial connection

Arguments:

```console
name:csv
type:boolean
default:True
------------
name:status
type:string
default:All
values: [invalid, valid]
```

Output: csv or JSON

Example:

```console
get_aws_accounts(csv=True, status='invalid')
```

#### Okta Users

`get_okta_users_aws_roles`

This function will print out a csv report of Okta users with their AWS roles and which AWS account it belongs to. The only different from this query and our "Permissions Query" default output is it prints the account name as opposed to arn, and can be modified to include additional properties.

Arguments:

```console
name:csv
type:boolean
default:True
------------
```

Output: csv or JSON

Example:

```console
get_okta_users_aws_roles(csv=True)
```
