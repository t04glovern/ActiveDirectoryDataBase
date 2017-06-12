from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import UserPassCredentials
from azure.graphrbac.models import UserCreateParameters, PasswordProfile

from passgen import get_password

import config


class ActiveDirectoryDataBase:
    def __init__(self):
        self.credentials = UserPassCredentials(
            config.AD_LOGIN_USER,
            config.AD_LOGIN_PASS,
            resource="https://graph.windows.net"
        )
        self.tenant_id = config.AD_TENANT_ID
        self.client = GraphRbacManagementClient(
            self.credentials,
            self.tenant_id
        )

    def create_collection(self, collection_name):
        collection = self.client.groups.create(
            display_name=collection_name,
            mail_nickname=collection_name
        )
        return collection

    def add_to_collection(self, collection_name, entry_id):
        for collection in self.list_collections():
            if collection['display_name'] == collection_name:
                self.client.groups.add_member(
                    group_object_id=collection['object_id'],
                    url="https://graph.windows.net/" + config.AD_TENANT_ID +
                        "/directoryObjects/" + entry_id
                )
            else:
                new_collection = self.create_collection(collection_name)
                self.client.groups.add_member(
                    group_object_id=new_collection.object_id,
                    url="https://graph.windows.net/" + config.AD_TENANT_ID +
                        "/directoryObjects/" + entry_id
                )

    def add_entry(self, entry_id):
        new_entry = self.client.users.create(
            UserCreateParameters(
                user_principal_name=str(entry_id) + "@{}".format(self.tenant_id),
                account_enabled=True,
                display_name=str(entry_id),
                mail_nickname=str(entry_id),
                password_profile=PasswordProfile(
                    password=str(get_password()),
                    force_change_password_next_login=True
                )
            )
        )
        return new_entry

    def get_entry_id(self, entry_name):
        for entry_item in self.list_entries():
            if entry_item['display_name'] == str(entry_name):
                return entry_item['object_id']
        return 0

    def delete_entry(self, entry_id):
        self.client.users.delete(str(entry_id) + "@{}".format(self.tenant_id))

    def list_entries(self):
        entry_list = []
        entries = self.client.users.list()
        for entry in entries:
            entry_list.append(
                {
                    'object_id': entry.object_id,
                    'object_type': entry.object_type,
                    'user_principal_name': entry.user_principal_name,
                    'display_name': entry.display_name,
                    'sign_in_name': entry.sign_in_name,
                    'mail': entry.mail,
                    'mail_nickname': entry.mail_nickname
                }
            )
        return entry_list

    def list_collections(self):
        collection_list = []
        collections = self.client.groups.list()

        for collection in collections:
            collection_list.append(
                {
                    'object_id': collection.object_id,
                    'object_type': collection.object_type,
                    'display_name': collection.display_name,
                    'security_enabled': collection.security_enabled,
                    'mail': collection.mail
                }
            )
        return collection_list


if __name__ == "__main__":
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