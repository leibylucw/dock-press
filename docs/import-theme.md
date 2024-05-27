# Import Theme
## Overview
If you are using dock-press to develop your WordPress site locally, you will need to import your site's theme.

## Steps
### 1. Obtain the Site's Theme
This largely depends on your setup and how comfortable you are using the command line. In general, you would log into the server where your site is hosted. You'd then create a zipped archive with something like tar using the following commands:

```shell
cd wp-content/themes
tar -czf <name of theme directory>.tar <name of theme directory>
```

You would then use something like SCP to copy `<name of theme directory>.tar` to your local machine:

```shell
scp <user>@<hostname/IP address>:<name of theme directory.tar> .
```

### 2. Import it with dock-press
You should now have your theme's tar file. Place it in a directory called `wp-content/themes`. Create it with:

```shell
mkdir -p wp-content/themes
```

If dock-press containers are running, take them down, using the `-v` flag to remove volumes to start fresh:

```shell
docker compose down -v
```

Modify `compose.yml` to mount your theme directory to the container:

```shell
      - ./wp-content/themes/<name of your theme directory>:/var/www/html/wp-content/themes/<name of your theme directory>
```

Then spin the containers back up:

```shell
docker compose up -d
```
