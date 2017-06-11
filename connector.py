from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import UserPassCredentials
from azure.graphrbac.models import UserCreateParameters, PasswordProfile

import random
import config


def get_password(password_length=13):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pw_length = password_length
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1, 5)):
        replace_index = random.randrange(len(mypw) // 2)
        mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index + 1:]

    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1, 5)):
        replace_index = random.randrange(len(mypw) // 2, len(mypw))
        mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1:]

    return mypw


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

    def add_user(self, username):
        user = self.client.users.create(
            UserCreateParameters(
                user_principal_name=str(username) + "@{}".format(self.tenant_id),
                account_enabled=True,
                display_name=str(username),
                mail_nickname=str(username),
                password_profile=PasswordProfile(
                    password=str(get_password()),
                    force_change_password_next_login=True
                )
            )
        )
        return user

    def delete_user(self, username):
        self.client.users.delete(str(username) + "@{}".format(self.tenant_id))


if __name__ == "__main__":
    connect = ActiveDirectoryDataBase()
    connect.add_user(9000)
    connect.delete_user(9000)