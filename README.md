# ActiveDirectoryDataBase (ADDB)
ADDB - The Active Directory based DB no one asked for

## Example
```python
connect = ActiveDirectoryDataBase()

# This will serve as the AD group (collection)
DB_COLLECTION = "collection"

# Create entries
for item in range(1300, 1350):
    connect.add_entry(item)

# For all entries, add to collection
for item in range(1300, 1350):
    connect.add_to_collection(DB_COLLECTION, connect.get_entry_id(item))

# Clean up all entries
for item in range(1300, 1350):
    connect.delete_entry(str(item))
```
## API Usage

### Create an entry
```python
connect = ActiveDirectoryDataBase()
connect.add_entry("Entry_Name")
```

### Delete an entry
```python
connect = ActiveDirectoryDataBase()
connect.delete_entry("Entry_Name")
```

### Create a collections
```python
connect = ActiveDirectoryDataBase()
connect.create_collection("Collection_Name")
```

### List all entries
```python
connect = ActiveDirectoryDataBase()
entry_list = connect.list_entries()
print(entry_list)
```

### List all collections
```python
connect = ActiveDirectoryDataBase()
collection_list = connect.list_collections()
print(collection_list)
```

### Add Entry to collection
```python
connect = ActiveDirectoryDataBase()
connect.add_to_collection("Collection_Name", "Entry_ID)
```
