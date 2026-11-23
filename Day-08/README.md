# Lists and Tuples

## Filtering unhealthy servers

A list can represent a collection of infrastructure resources, such as servers.
Each dictionary in the list stores a server record with its name and status. A
list comprehension filters those records to find only unhealthy servers. This
is useful for monitoring and automation because a script can quickly identify
resources that need attention.

Run the example from the repository root:

```bash
python Day-08/03-filter-unhealthy-servers.py
```
