# Postmortem: ALX System Engineering & DevOps Project 0x19

## Incident Overview
Upon the release of ALX's System Engineering & DevOps project 0x19, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests to the server resulted in 500 Internal Server Errors, whereas the expected response was an HTML file defining a simple Holberton WordPress site.

## Debugging Process
Bug debugger Brennan (BDB) encountered the issue at approximately 19:20 PST and promptly began investigating.

1. **Process Check:**
   - Verified that two Apache processes (`root` and `www-data`) were running using `ps aux`.

2. **Server Configuration:**
   - Examined the `sites-available` folder in `/etc/apache2/` and confirmed that the web server served content from `/var/www/html/`.

3. **Strace Analysis:**
   - Ran `strace` on the PID of the `root` Apache process but found no useful information.
   - Repeated the process for the `www-data` process and discovered an `-1 ENOENT` (No such file or directory) error related to `/var/www/html/wp-includes/class-wp-locale.phpp`.

4. **File Inspection:**
   - Reviewed files in the `/var/www/html/` directory.
   - Located the erroneous `.phpp` file extension in the `wp-settings.php` file (Line 137: `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).
   - Removed the trailing `p` from the line.

5. **Testing:**
   - Tested another `curl` request on the server, which returned a successful `200 OK` response.

6. **Automation:**
   - Created a Puppet manifest to automate the error fix.

## Root Cause
The outage resulted from a simple typo. The WordPress app encountered a critical error in `wp-settings.php` while trying to load the file `class-wp-locale.phpp`. The correct file name, located in the `wp-content` directory of the application folder, was `class-wp-locale.php`.

## Prevention Measures
To prevent similar outages in the future:

1. **Thorough Testing:**
   - Always test the application thoroughly before deployment to catch issues early.

2. **Status Monitoring:**
   - Enable an uptime-monitoring service (e.g., UptimeRobot) to receive instant alerts in case of website outages.
