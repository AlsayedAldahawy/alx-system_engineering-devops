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