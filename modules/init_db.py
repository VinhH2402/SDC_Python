import mysql.connector as mysql
import csv
import itertools

mydb = mysql.connect(host="localhost")
cur = mydb.cursor()

# create DB
cur.execute("DROP DATABASE reviewAPI")
cur.execute("CREATE DATABASE reviewAPI")
cur.execute('USE reviewAPI')

review_schema = open('./modules/query/review.sql').read()
photo_schema = open('./modules/query/photo.sql').read()
charac_schema = open('./modules/query/characteristic.sql').read()
charac_review_schema = open('./modules/query/charac_review.sql').read()

cur.execute(charac_schema)
cur.execute(review_schema)
cur.execute(photo_schema)
cur.execute(charac_review_schema)


with open('./csv/reviews.csv', 'r') as characteristic_review:
  reader = csv.reader(characteristic_review)
  header = next(reader)
  while True:
    records = list(itertools.islice(reader, 20000))
    if not records:
      break
    query = '''INSERT INTO review 
            (id, product_id, rating, date, summary, body,recommend, 
            reported,reviewer_name, reviewer_email, response, helpfulness) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.executemany(query, records)
    mydb.commit()

with open('./csv/characteristics.csv', 'r') as characteristic:
  reader = csv.reader(characteristic)
  header = next(reader)
  while True:
    records = list(itertools.islice(reader, 20000))
    if not records:
      break
    query = 'INSERT INTO characteristic (id, product_id, name) VALUES (%s, %s, %s)'
    cur.executemany(query, records)
    mydb.commit()

with open('./csv/characteristic_reviews.csv', 'r') as characteristic_review:
  reader = csv.reader(characteristic_review)
  header = next(reader)
  while True:
    records = list(itertools.islice(reader, 20000))
    if not records:
      break
    query = '''INSERT INTO characteristic_review 
            (id, characteristic_id, review_id, value) 
            VALUES (%s, %s, %s, %s)'''
    cur.executemany(query, records)
    mydb.commit()

with open('./csv/reviews_photos.csv', 'r') as characteristic_review:
  reader = csv.reader(characteristic_review)
  header = next(reader)
  while True:
    records = list(itertools.islice(reader, 20000))
    if not records:
      break
    query = '''INSERT INTO photo 
            (id, review_id, url) 
            VALUES (%s, %s, %s)'''
    cur.executemany(query, records)
    mydb.commit()
