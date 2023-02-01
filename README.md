# Treasure_hunters

CRUD web application that runs the Treasure Hunters app allowing you to plan and run treasure hunts 
with a play element incorporated into the app. It uses RESTful routes, a PostgreSQL database and Flask.

## Built With:

* HTML
* CSS
* Python
* Flask
* Postgresql

# Getting Started:

## Prerequisites

To run this app, you must install:

> psychopg

```pip3 install psycopg2```

> Flask

```pip3 install Flask```

> Postgresql

## Installation

Clone the repository

```git clone [https://github.com/Delfland/treasure_hunt.git]```

Navigate to the folder using terminal

Create the database
```psql -d treasure_hunt -f db/treasure_hunt.sql```

Seed the database with pre-set data by running the console.py file using python3 console.py

Run Flask:
```flask run```

Open in browser (Google Chrome is recommended): http://127.0.0.1:4999
To stop the server enter ctrl + c in your Terminal
