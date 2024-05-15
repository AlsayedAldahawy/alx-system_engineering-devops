# 0x0A-configuration_management

## Overview

In this project, we explore Puppet—a powerful configuration management tool. We'll write Puppet manifest files to accomplish various tasks, including creating files, installing packages, and executing commands.

## Project Tasks

### 1. Create a File

- **Manifest:** 0-create_a_file.pp
- **Description:**
  - Creates a file named `school` in the `/tmp` directory.
  - File permissions: `0744`
  - File group: `www-data`
  - File owner: `www-data`
  - File content: "I love Puppet"

### 2. Install a Package

- **Manifest:** 1-install_a_package.pp
- **Description:**
  - Installs the `flask` package using `pip3`.

### 3. Execute a Command

- **Manifest:** 2-execute_a_command.pp
- **Description:**
  - Kills the process named `killmenow`
