# Import Database
## Overview
If you are using dock-press to develop your WordPress site locally, you will need to import your site's database using the mysqldump tool.

## Steps
### 1. Obtain a Database Dump File
This largely depends on your setup and how comfortable you are using the command line. In general, you would log into the server where you have MySQL or MariaDB running and execute the following command:

```shell
mysqldump -p --databases <database name> > db.sql
```

NOTE: The above command uses the `--databases` flag to ensure only the database for your website is dumped. Drop, create, and use commands are inserted in the resulting dump file. Otherwise, only tables would be dumped.

You would then use something like SCP to copy `db.sql` to your local machine:

```shell
scp <user>@<hostname/IP address>:<path to db.sql> .
```

### 2. Import it with dock-press
You should now have the `db.sql` file. Place this at the root of the dock-press repository. If dock-press containers are running, take them down, using the `-v` flag to remove volumes to start fresh:

```shell
docker compose down -v
```

Then spin them back up:

```shell
docker compose up -d
```

The `compose.yml` config file maps `db.sql` to a specific directory on the MySQL container. The MySQL image imports any and all SQL files found in this particular directory, so you don't have to do it manually.

If you wish to add more SQL files to this directory, you may map them in `compose.yml`.
