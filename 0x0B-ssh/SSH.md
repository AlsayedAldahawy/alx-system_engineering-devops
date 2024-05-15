# SSH Key Management

## Generating an SSH Key Pair

- To generate an SSH key pair, use the `ssh-keygen` command.
- By default, it creates an RSA key with a length of 2048 bits.

### Options for Key Types

- Specify a different key type using `-t`:
  - RSA: `ssh-keygen -t rsa`
  - DSA: `ssh-keygen -t dsa`
  - ECDSA: `ssh-keygen -t ecdsa`

### Key Length Considerations

- Most servers support keys with a length of at least 4096 bits.
    - `ssh-keygen -b 4096`
- Longer keys may not be accepted due to DDoS protection policies.

## Passphrase Protection

- A passphrase is an additional layer of protection for your private key.
- You need to enter it every time you authenticate with the associated private key.
- If someone gains access to your private key, they can't use it without the passphrase.
- Losing the passphrase requires generating a new key pair.

### Changing the Passphrase

- To change the passphrase for an existing key:
    - `ssh-keygen -p`


## SSH Key Fingerprint

- Each SSH key pair has a unique cryptographic "fingerprint."
- The fingerprint helps uniquely identify the keys.
- It's easier to compare randomart images visually than long hexadecimal strings.
- Your client checks if the server's fingerprint matches the one you previously saved.

### Viewing the Fingerprint

- To view the fingerprint of an SSH key:
- Ask for the file location of the key:
    - `ssh-keygen -l`

- Show the fingerprint directly (if the file location is known):
    - `ssh-keygen -l -f ~/.ssh/id_rsa.pub`

- Additionally, use `-lv` to display the key's randomart image.
    - `ssh-keygen -lv`




### Copying your Public SSH Key to a Server with SSH-Copy-ID

- ` ssh-copy-id username@remote_host `

This will prompt you for the user account’s password on the remote system

### Copying your Public SSH Key to a Server Without SSH-Copy-ID
	- cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
	This will prompt you for the user account’s password on the remote system

## Basic Connection Instructions

### Connecting to a Remote Serve

	- ssh remote_host : if username on your local machine is the same as that on the remote server
	- ssh username@remote_host
    - ssh -i path/to/key_file username@remote_host : Connect to a remote server with a specific identity (private key):

### Running a Single Command on a Remote Server
	- ssh username@remote_host command_to_run

### Logging in to a Server with a Different Port
	- ssh -p port_num username@remote_host

### To avoid having to do this every time you log in to your remote server, you can create or edit a configuration file in the ~/.ssh directory within the home directory of your local computer.
	- nano ~/.ssh/config
and inside the config file we write:

		Host remote_alias
    		  HostName remote_host
    		  Port port_num
This will allow you to log in without specifying the specific port number on the command line.

### Adding your SSH Keys to an SSH Agent to Avoid Typing the Passphrase
	- eval $(ssh-agent) : running ssh agent
	- ssh-add : add the private key to the agent

### Forwarding your SSH Credentials to Use on a Server so you be able to access other servers from the within another one
	- eval $(ssh-agent) : running ssh agent
	- ssh-add : add the private key to the agent
	- ssh -A username@remote_host : This forwards your credentials to the server for this session

## Server-Side Configuration Options
### Disabling Password Authentication
    PasswordAuthentication no
After you have made the change, save and close the file. To implement the changes, you should restart the SSH service.

### Changing the Port that the SSH Daemon Runs On
Some administrators suggest that you change the default port that SSH runs on. This can help decrease the number of authentication attempts your server is subjected to from automated bots.
change the config file in remote server
```
    # Port 22   # commenting out the default port
	Port 4444   # adding the desired port
```
To implement the changes, you must restart the SSH daemon.

### Limiting the Users Who can Connect Through SSH
	add to config file: AllowUsers user1 user2
	add to config file: AllowGroups sshmembers

Now, you can create a system group (without a home directory) matching the group you specified by typing:

	-sudo groupadd -r sshmembers
* sshmembers is the group name, can be changed to whatever you want
Make sure that you add whatever user accounts you need to this group. This can be done by typing:

    sudo usermod -a -G sshmembers user1
	sudo usermod -a -G sshmembers user2
	sudo usermod -a -G sshmembers user2

### Disabling Root Login
It is often advisable to completely disable root login through SSH after you have set up an SSH user account that has sudo privileges.

	PermitRootLogin no

### Allowing Root Access for Specific Commands
1- copy the ssh key to the root user's autorized_keys in /root/.ssh/authorized_keys
		we can do this by any method, for example, using ssh-copy-id

		>>> ssh-copy-id root@remote_host : note we used here the root user.
2- At the beginning of the line with the key you uploaded, add a command= listing that
defines the command that this key is valid for. This should include the full path to the executable, plus any arguments

		command="/path/to/command arg1 arg2" ssh-rsa ...

3- edit the ssh configuration file of the root user > /etc/ssh/sshd_config

		PermitRootLogin forced-commands-only

### Forwarding X Application Displays to the Client
The SSH daemon can be configured to automatically forward the display of X applications on the server to the client machine. For this to function correctly, the client must have an X windows system configured and enabled.

edit /etc/ssh/sshd_config

    X11Forwarding yes

in client side use : `ssh -X username@remote_host`


## Client-Side Configuration Options
### Defining Server-Specific Connection Information
On your local computer, you can define individual configurations for some or all of the servers you connect to. These can be stored in the ~/.ssh/config file, which is read by your SSH client each time it is called.

Inside, you can define individual configuration options by introducing each with a Host keyword, followed by an alias. Beneath this and indented, you can define any of the directives found in the ssh_config man page
    
    man ssh_config

An example configuration would be:

```
                                    `~/.ssh/config`
Host testhost
    HostName your_domain
    Port 4444
    User demo
```

You could then connect to your_domain on port 4444 using the username demo by simply typing:

	>>> ssh testhost

You can also use wildcards to match more than one host. Keep in mind that later matches can override earlier ones. Because of this, you should put your most general matches at the top. For instance, you could default all connections to not allow X forwarding, with an override for your_domain by having this in your file:
~/.ssh/config
```
Host *
    ForwardX11 no

Host testhost
    HostName your_domain
    ForwardX11 yes
    Port 4444
    User demo
```


### Keeping Connections Alive to Avoid Timeout
If you find yourself being disconnected from SSH sessions before you are ready, it is possible that your connection is timing out.

```
Host *
    ServerAliveInterval 120
```
This should be enough to notify the server not to close the connection

### Disabling Host Checking
By default, whenever you connect to a new server, you will be shown the remote SSH daemon’s host key fingerprint.

This is configured so that you can verify the authenticity of the host you are attempting to connect to and spot instances where a malicious user may be trying to masquerade as the remote host.

In certain circumstances, you may wish to disable this feature. Note: This can be a big security risk, so make sure you know what you are doing if you set your system up like this.
Set the StrictHostKeyChecking directive to no to add new hosts automatically to the known_hosts file. Set the UserKnownHostsFile to /dev/null to not warn on new or changed hosts
```
Host *
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```
You can enable the checking on a case-by-case basis by reversing those options for other hosts. The default for StrictHostKeyChecking is ask:
```
Host *
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null

Host testhost
    HostName your_domain
    StrictHostKeyChecking ask
    UserKnownHostsFile /home/demo/.ssh/known_hosts
```
