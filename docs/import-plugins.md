# Import Plugins
## Overview
If you are using dock-press to develop your WordPress site locally, you will need to import your site's plugins.

## Steps
### 1. Obtain the Site's Plugins
This largely depends on your setup and how comfortable you are using the command line. In general, you would log into the server where your site is hosted. You'd then create a zipped archive with something like tar using the following commands:

```shell
cd wp-content/plugins
tar -czf plugins.tar *
```

You would then use something like SCP to copy `plugins.tar` to your local machine:

```shell
scp <user>@<hostname/IP address>:<plugins.tar> .
```

### 2. Import it with dock-press
You should now have the `plugins.tar` file. Place it in a directory called `wp-content`. Create it with:

```shell
mkdir -p wp-content
```

If dock-press containers are running, take them down, using the `-v` flag to remove volumes to start fresh:

```shell
docker compose down -v
```

Then rebuild the image and spin them back up:

```shell
docker compose build
docker compose up -d
```

NOTE: Add the `--no-cache` flag to the `docker compose build` command if you encounter issues.
