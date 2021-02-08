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

### Default variables

 * Packages to install for each OS:

   ```yaml
   apache2_packages:
     - apache2
   ```

 * Default port used for HTTP: `apache2_default_http_port: 80`

 * Default port used for HTTPS: `apache2_default_https_port: 443`

 * Extra ports to listen on: `apache2_extra_ports: []`

 * Create/enable default site: `apache2_create_default: false`

 * Create/enable default SSL site: `apache2_create_default: false`

 * SSL certificate file to use in for the default SSL site (undefined by default): `apache2_certificate_file: `

 * SSL certificate key file to use in for the default SSL site (undefined by default): `apache2_certificate_key_file: `

 * Other Apache 2 modules to install: `# apache2_modules: []`

 * Default production configuration values:

   ```yaml
   apache2_config_default:
     - 'ServerSignature Off'
     - 'ServerTokens Prod'
   ```

 * Enable HTTP to HTTPS for all sites: `apache2_https_redirect: false`


### OS specific variables

 * Available sites configuration path: `apache2_sites_available_path: "{{apache2_config_path}}/sites-available"`

 * Available modules configuration path: `apache2_modules_available_path: "{{apache2_config_path}}/mods-available"`

 * Available configurations path: `apache2_config_available_path: "{{apache2_config_path}}/conf-available"`

 * Default host configuration path: `apache2_default_host_path: "{{apache2_sites_available_path}}/000-default.conf"`

 * Default SSL host configuration path: `apache2_default_ssl_host_path: "{{apache2_sites_available_path}}/000-default_ssl.conf"`

 * Enabled sites configuration path: `apache2_sites_enabled_path: "{{apache2_config_path}}/sites-enabled"`

 * Enabled modules configuration path: `apache2_modules_enabled_path: "{{apache2_config_path}}/mods-enabled"`

 * Enabled configurations path: `apache2_config_enabled_path: "{{apache2_config_path}}/conf-enabled"`

 * Custom configuration to deploy: `apache2_config: "{{apache2_config_default}}"`

 * Apache2 package for the given OS: `apache2_packages_default`

 * Service name in each OS: `apache2_service: apache2`

 * User used to run the server: `apache2_user`

 * Group used to run the server: `apache2_group`

 * Apache 2 configuration path: `apache2_config_path: "/etc/{{apache2_service}}"`

 * Apache 2 main configuration file path: `apache2_config_file`

 * Apache 2 library path: `apache2_lib_path`

 * Apache 2 logs path: `apache2_log_path`

 * Base path used to serve files: `apache2_base_path`

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
