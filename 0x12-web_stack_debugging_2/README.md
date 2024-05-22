# NGINX Configuration Scripts

This directory contains three bash scripts related to NGINX configuration. Here's a brief overview of each script:

1. **0-iamsomeoneelse**
   - Purpose: Run the `whoami` command under a specific user passed as an argument.
   - Usage: `./run_as_user.sh <username>`
   - Example: `./run_as_user.sh alsayed`

2. **1-run_nginx_as_nginx**
   - Purpose: Configure NGINX to listen on port 8080 instead of the default port 80.
   - Steps:
     1. Replace occurrences of "80" with "8080" in the default NGINX site configuration.
     2. Set ownership of the NGINX configuration file to the 'nginx' user.
     3. Adjust permissions for the NGINX configuration file.
     4. Restart the NGINX service.
   - Usage: `./nginx_config.sh`
   - Note: Run this script with appropriate privileges (e.g., using `sudo`).

3. **100-fix_in_7_lines_or_less**
   - Purpose: Quickly fix NGINX configuration issues.
   - Steps:
     - Replace the user from "www-data" to "nginx" in the NGINX configuration.
     - Change port "80" to "8080" in the default NGINX site configuration.
     - Set ownership and permissions for the NGINX configuration file.
     - Restart the NGINX service.
