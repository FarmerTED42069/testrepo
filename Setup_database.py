#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3
import os

# Step 1: Set up the SQLite database
# This function will create tables for different branches of your projects

def create_database():
    # Set the database path to your new SQL directory, easily accessible from Windows
    db_path = "/mnt/c/SQL/projects.db"

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Create the connection to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Create table for general conversations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY,
            topic TEXT,
            content TEXT,
            category TEXT,
            timestamp TEXT,
            tags TEXT
        )
    ''')

    # Create table for Ponzi Algo data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ponzi_algo_data (
            id INTEGER PRIMARY KEY,
            data_type TEXT,
            data TEXT,
            timestamp TEXT
        )
    ''')

    # Create table for Sheeple social media data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sheeple_social_media (
            id INTEGER PRIMARY KEY,
            post_type TEXT,
            content TEXT,
            engagement_metrics TEXT,
            timestamp TEXT
        )
    ''')

    # Create table for Mechanical Darwinism notes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mechanical_darwinism (
            id INTEGER PRIMARY KEY,
            concept TEXT,
            content TEXT,
            timestamp TEXT
        )
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    # Print the absolute path of the database file
    print(f"Database created at: {db_path}")

# Example usage to create the framework without adding data
if __name__ == "__main__":
    create_database()


# In[ ]:




