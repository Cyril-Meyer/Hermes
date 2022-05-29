# Hermes
Send Discord DMs to your community

### Usage

**setup venv and install dependency**
```
python -m venv venv
# windows
.\venv\Scripts\activate.bat
pip install -U pip
pip install numpy
pip install discord.py
```

**get user list**

The bot running this command require 'SERVER MEMBERS INTENT'.

This command create one `.npy` file per server the bot is connected to
(and a merge file named `users_all.npy`).

```
# token = discord bot token
python get_users.py <token>
```

**send DM to user list**

This command send *<message.txt>* DM to all the user in the user list *<filename.npy>*

```
python send_dm.py <token> <filename.npy> <message.txt>
```

***optional :*** **split user list**

This command split the list of users between `N` equal splits.
This is interesting if you want to split your community message between moderators,
to be able to respond (your message need to contain a way to contact you back).

```
# filename = npy file created by get_users.py
# splits = number of splits
python split_users.py <filename.npy> <splits>
```

***optional :*** **view user list**

```
python view_users_list.py <filename.npy>
```
