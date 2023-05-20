# Ermetic Python Collection

## Setup

- Clone the repo to your local machine
- Rename the `.env.sample` file to `.env`
- Add the `ERMETIC_URL` and `ERMETIC_TOKEN` values to the `.env` file

## Methods

This package contains the following methods:

| Function                               | Parameters                                                                      | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `get_aws_accounts`                     | `csv_file: bool = False, json_file: bool = False`                               | Retrieves information about AWS accounts from the Ermetic platform. |
| `get_users_assignments`                | `csv_file: bool = False, json_file: bool = False`                               | Retrieves users assignment report.                                  |
| `get_okta_users`                       | `csv_file: bool = False, json_file: bool = False`                               | Retrieves a report on Okta users and AWS roles they assume.         |
| `get_findings_by_azure_resource_group` | `resource_group_id: str, status: str = 'Open', csv_file=False, json_file=False` | Retrieves Findings based on Azure Resource Group.                   |

## get_aws_accounts

Retrieves information about AWS accounts from the Ermetic platform.

### Parameters

#### csv_file

```yaml
Type: bool
Required: False
Default Value: False
```

#### status

```yaml
Type: str
Required: False
Default Value: 'All'
```

### Description

This function connects to the Ermetic platform and retrieves information about AWS accounts. The information can be saved to a CSV or JSON file if specified.

### Output

- CSV of AWS accounts based on the status argument.

### Returns

```python
List[Dict] | Literal | Any
```

## get_users_assignments

Get Tenant users and save to CSV or JSON.

### Parameters

#### csv_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

#### json_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

### Description

This function retrieves Tenant users and allows saving the information to a CSV or JSON file. It internally calls other functions to fetch user role assignments, AWS accounts, and folder information.

### Returns

```python
None
```

## get_okta_users

Retrieves information about Okta users and their AWS roles.

### Parameters

#### csv_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

#### json_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

### Description

This function connects to the Ermetic platform and retrieves information about Okta users and their assumed roles. It's useful when you have more than 10k Okta users, or need information not available from the UI

### Output

- JSON or CSV with Okta users.

### Returns

```python
List[Dict]
```

## get_findings_by_azure_resource_group

Retrieves findings based on Azure Resource Group Id
resource_group_id: str, status: str = 'Open', csv_file=False, json_file=False

### Parameters

#### resource_group_id

```yaml
Type: str
Required: True
Default Value: None
```

#### status

```yaml
Type: str
Required: False
Default Value: 'Open'
Accepted Values: 'Open, Snoozed, Resolved'
```

#### csv_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

#### json_file

```yaml
Type: bool
Required: False
Default Value: 'False'
```

### Description

This function connects to the Ermetic platform and retrieves Findings based on the given Azure Resource Group Id. It can support multiple filters in the future

### Output

- JSON or CSV with Findings users.

### Returns

```python
None
```
