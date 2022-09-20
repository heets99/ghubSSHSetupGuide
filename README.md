# Using SSH keys for Authentication with Github

## Getting your SSH Key
### On Windows

1. Open command prompt
2. Run the following command
```
cat %USERPROFILE%\.ssh\id_rsa.pub
```
You should see something like this:
![cmd_run](/cmd_run.png)
_It should look like this_
3. Copy the output

## Updating your SSH keys in Github
1. Go to https://github.com/settings/ssh/new
2. Give your key a name, be funky "WoodyBookRefree"
3. Paste the previously copied key in"Key" Section
![adding key to github](/add_key_ghub.png)
4. Click "Add SSH Key"