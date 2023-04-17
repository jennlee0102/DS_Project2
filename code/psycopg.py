import psycopg2

conn = psycopg2.connect(
    host="raja.db.elephantsql.com",
    database="xqxjxqed",
    user="xqxjxqed",
    password="LwwfpLIeUYIk-tDt-7DoKGESI1Gk3rp5")

print(conn)

cur = conn.cursor()

# SQL statement to create the "business" table
create_business_table = """CREATE TABLE business_table
    (business_id TEXT PRIMARY KEY,
     name TEXT,
     address TEXT,
     city TEXT,
     state TEXT,
     postal_code TEXT,
     latitude FLOAT,
     longitude FLOAT,
     stars FLOAT,
     review_count INTEGER,
     attributes JSON,
     categories TEXT[],
     hours JSON);
"""

create_review_table = """CREATE TABLE review_table (
    review_id TEXT PRIMARY KEY,
    user_id TEXT,
    business_id TEXT,
    stars REAL,
    useful INT,
    funny INT,
    cool INT,
    text TEXT,
    date TIMESTAMP);
"""

create_final_table = """CREATE TABLE final_table (
  business_id TEXT,
  name TEXT,
  state TEXT,
  stars_x FLOAT,
  is_open INTEGER,
  categories TEXT[],
  user_id TEXT,
  text TEXT,
  review_tokens TEXT[],
  useful INTEGER,
  funny INTEGER,
  cool INTEGER);
"""

# Execute the SQL statement to create the table
cur.execute(create_business_table)
cur.execute(create_review_table)
cur.execute(create_final_table)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()