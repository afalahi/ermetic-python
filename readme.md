# Ermetic Python Collection

## Account Management

### Functions

#### AWS Accounts

`get_aws_accounts`'

This function will print out a csv report of either connected AWS accounts without issues, connected accounts with issues, or disconnected accounts. It will have the reason for why the account is disconnected, and issues for accounts with partial connection

Arguments:

```console
name:token
type:string
------------
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
get_aws_accounts(token=token, csv=True, status='invalid')
```

#### Okta Users

`get_okta_users_aws_roles`

This function will print out a csv report of Okta users with their AWS roles and which AWS account it belongs to. The only different from this query and our "Permissions Query" default output is it prints the account name as opposed to arn, and can be modified to include additional properties.

Arguments:

```console
name:token
type:string
------------
name:csv
type:boolean
default:True
------------
```

Output: csv or JSON

Example:

```console
get_okta_users_aws_roles(token=token, csv=True)
```
