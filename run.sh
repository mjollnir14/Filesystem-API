#!/bin/bash

# empty db
rm content.db

# generate CSV
python list_directory_generate_csv.py

# inject CSV into db
cat inject_content.sql |sqlite3 content.db
