apache2
=======

This role installs and configures the [Apache HTTP server](https://httpd.apache.org/).

Requirements
------------

No special requirements;

Note, however that this role requires root access, so either run it in a playbook with a global `become: yes`, or invoke the role in your playbook like:

    - hosts: webserver
      roles:
        - role: bithium.apache2
          become: yes

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml` and `vars/main.yml`):

 * Packages to install for each OS:

   ```yaml
   apache2_packages:
     - apache2
   ```

 * Service name in each OS: `apache2_service: apache2`

 * User used to run the server: `apache2_user: www-data`

 * Group used to run the server: `apache2_group: www-data`

 * Apache 2 configuration path: `apache2_config_path: "/etc/{{apache2_service}}"`

 * Path to the available sites:

   `apache2_sites_available_path: "{{apache2_config_path}}/sites-available"`

 * Path to the available modules:

   `apache2_modules_available_path: "{{apache2_config_path}}/sites-available"`

 * Path to the default host file:

   `apache2_default_host_path: "{{apache2_sites_available_path}}/000-default.conf"`

 * Path to the default ssl host file:

   `apache2_default_ssl_host_path: "{{apache2_sites_available_path}}/default-ssl.conf"`

 * Base path used to serve files: `apache2_base_path: "/var/www/html/"`

 * Default port used for HTTP: `apache2_default_http_port: 80`

 * Default port used for HTTPS: `apache2_default_https_port: 443`

 * Extra ports to listen on: `apache2_extra_ports: []`

 * If the default ssl host should be enabled: `apache2_enable_ssl: false`

 * If the default hosts (HTTP and HTTPS) should be removed: `apache2_remove_default: false`

 * Apache 2 modules to install: `# apache2_modules: []`

Dependencies
------------

No dependencies.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: apache2, x: 42 }

License
-------

Apache 2.0

Author Information
------------------

[Bithium S.A.](https://www.bithium.com/)
