# Nginx configurations

### Step 1 — Setting Up New Document Root Directories
1. **Default Server Block**:
   - Nginx on Ubuntu 16.04 serves documents from `/var/www/html` by default.
   - This directory is used when the client request doesn't match any other configured sites.

2. **Creating Additional Directories**:
   - To serve multiple sites, create a directory structure within `/var/www` for each site.
   - Place the actual web content in an `html` directory within these site-specific directories.

3. **Flexibility and Sibling Directories**:
   - This approach allows flexibility to create other directories alongside `html` if needed.
   - For example, you can have additional directories associated with your sites.

4. **Creating Directories**:
   - Use the `-p` flag with `mkdir` to create necessary parent directories:
     ```
     sudo mkdir -p /var/www/example.com/html
     sudo mkdir -p /var/www/test.com/html
     ```
   - Reassign ownership of the web directories to your normal user account to allow writing without `sudo`.
   - Ensure correct permissions (e.g., `sudo chmod -R 755 /var/www`).

### Step 2 — Creating Sample Pages for Each Site
   - Create an `index.html` file in each domain's `html` directory.
   - Customize the content to indicate the site (e.g., "Welcome to Example.com!").
    <html>
        <head>
            <title>Welcome to Example.com!</title>
        </head>
        <body>
            <h1>Success!  The Example.com server block is working!</h1>
        </body>
    </html>

### Step 3 — Creating Server Block Files for Each Domain
   - Copy the default server block config file as a template:
     ```
     sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com
     ```
   - Edit the new file (`sudo nano /etc/nginx/sites-available/example.com`) to configure your domain-specific settings.
   - Pay attention to the `listen` directives and choose the default server block if needed.

1. **Configuring Server Blocks**:
   - By default, Nginx contains one server block called `default`, which serves as a template for other configurations.
   - We'll leave the `default` server block in place to handle non-matching requests.
   - Remove the `default_server` option from this and any additional server blocks you create.
   - You can choose to designate one of your sites as the "default" by including the `default_server` option in the `listen` directive.

2. **Adjusting Document Root**:
   - Modify the `root` directive in your server block configuration to point to the site's document root that you created:
     ```
     server {
         listen 80;
         listen [::]:80;
         root /var/www/example.com/html;
         # Other configuration settings...
     }
     ```
3. **Modify the server_name**
    - we need to modify the `server_name` to match requests for our first domain. We can additionally add any aliases that we want to match. We will add a `www.example.com` alias to demonstrate.

file should look something like this:

/etc/nginx/sites-available/example.com

    server {
            listen 80;
            listen [::]:80;

            root /var/www/example.com/html;
            index index.html index.htm index.nginx-debian.html;

            server_name example.com www.example.com;

            location / {
                    try_files $uri $uri/ =404;
            }
    }

Certainly! Here's a summarized version of the remaining steps for setting up Nginx server blocks (virtual hosts) on Ubuntu 16.04:

### Step 4: Enabling Server Blocks and Restarting Nginx

1. **Create Symbolic Links**:
   - Enable your server block files by creating symbolic links from `sites-available` to `sites-enabled`:
     ```
     sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
     sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/
     ```
   - These files are now linked into the `enabled` directory.

2. **Configure Server Blocks**:
   - You have three server blocks enabled:
     - `example.com`: Responds to requests for `example.com` and `www.example.com`.
     - `test.com`: Responds to requests for `test.com` and `www.test.com`.
     - `default`: Responds to any requests on port 80 that do not match the other two blocks.

3. **Avoid Hash Bucket Memory Issues**:
   - To prevent hash bucket memory problems, adjust the `server_names_hash_bucket_size` directive in `/etc/nginx/nginx.conf`.
   - Uncomment the line (remove the `#` symbol):
     ```
     server_names_hash_bucket_size 64;
     ```

4. **Test Configuration**:
   - Check for syntax errors in your Nginx files:
     ```
     sudo nginx -t
     ```
   - If no issues are found, proceed to the next step.

5. **Restart Nginx**:
   - Apply your changes by restarting Nginx:
     ```
     sudo systemctl restart nginx
     ```

### Step 5: Modifying Your Local Hosts File for Testing (Optional)

- If you've been using placeholder domain names instead of actual domains you own, you can modify your local computer's configuration to test your Nginx server block setup.
- This won't allow other visitors to view your site correctly, but it lets you test each site independently.
- By intercepting requests that would normally go to DNS, you can set the IP addresses your local computer should use when requesting domain names.
- Ensure you're operating on your local computer (not a remote server) and have the necessary permissions to edit system files.

#### On Mac or Linux:

1. Open the hosts file:
   ```
   sudo nano /etc/hosts
   ```

2. Add lines like this (assuming your server's public IP address is 203.0.113.5):
   ```
   127.0.0.1   localhost
   ...
   203.0.113.5 example.com www.example.com
   203.0.113.5 test.com www.test.com
   ```

3. Save and close the file.

#### On Windows:

- Follow instructions for altering the hosts file specific to Windows.

### Step 6: Testing Your Results

1. Visit the domains in your web browser:
   - [http://example.com](http://example.com): You should see a page similar to the "Nginx first server block" example.
   - [http://test.com](http://test.com): You should see a slightly different site (the "Nginx second server block").

2. If both sites work, you've successfully configured two independent server blocks with Nginx.

3. If you adjusted your hosts file for testing, consider removing the added lines.

4. For public-facing access, consider purchasing domain names for your sites.
