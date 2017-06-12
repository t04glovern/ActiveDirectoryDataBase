# ActiveDirectoryDataBase
The Active Directory based DB no one asked for

### Create an entry
~~~~
connect = ActiveDirectoryDataBase()
connect.add_entry("Entry_Name")
~~~~

### Delete an entry
~~~~
connect = ActiveDirectoryDataBase()
connect.delete_entry("Entry_Name")
~~~~

### List all entries
~~~~
connect = ActiveDirectoryDataBase()
entry_list = connect.list_entries()
print(entry_list)
~~~~

### List all collections
~~~~
connect = ActiveDirectoryDataBase()
collection_list = connect.list_collections()
print(collection_list)
~~~~

### Add Entry to collection (WIP)
~~~~
connect = ActiveDirectoryDataBase()
connect.add_to_collection("Collectio_Name")
~~~~