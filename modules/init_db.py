import mysql.connector
import pandas as pd
import s3

#file = s3.get_files()


mydb = mysql.connector.connect(host="localhost")
cur = mydb.cursor()

# create DB
cur.execute("DROP DATABASE reviewAPI")
cur.execute("CREATE DATABASE reviewAPI")
cur.execute('USE reviewAPI')

review_schema = open('./modules/query/review.sql').read()
reviewer_schema = open('./modules/query/reviewer.sql').read()
photo_schema = open('./modules/query/photo.sql').read()
charac_schema = open('./modules/query/characteristic.sql').read()
charac_review_schema = open('./modules/query/charac_review.sql').read()
cur.execute(reviewer_schema)
cur.execute(charac_schema)
cur.execute(review_schema)
cur.execute(photo_schema)
cur.execute(charac_review_schema)


# review = file


# cache = {}
# cur.execute('INSERT INTO reviewer (name, email) VALUEs (%s, %s)', ("funtime", "first.last@gmail.com"))

# for row in review.itertuples():
#     cur.execute('SELECT id FROM reviewer WHERE name = %s', (row.reviewer_name,))
#     reviewerId = cur.fetchone()
#     if not reviewerId:
#         cur.execute('INSERT INTO reviewer (name, email) VALUES (%s, %s)', (row.reviewer_name, row.reviewer_email))
#         mydb.commit()
#         reviewerId = cur.lastrowid
#     else:
#         reviewerId = reviewerId[0]
   
#     sql = '''INSERT INTO review 
#             (id, product_id, rating, date, summary, body, recommend, reported, response, helpfulness, reviewer)
#             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)'''
#     value =  (row.id, row.product_id, row.rating, row.date, row.summary, row.body,
#                  row.recommend, row.reported, row.response, row.helpfulness, reviewerId)        
#     cur.execute(sql,value)


# mydb.commit()

# cur.execute('SELECT * FROM review')
# print(cur.fetchall())

