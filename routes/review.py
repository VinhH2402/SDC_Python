import mysql.connector as mysql
from datetime import datetime

mydb = mysql.connect(host="localhost")
cur = mydb.cursor()

cur.execute('USE reviewAPI')

#query
findReviews = 'SELECT * FROM review WHERE product_id = %s'
findPhotos = 'SELECT * FROM photo WHERE review_id = %s'

def transform(data):
    results = []
    for r in data:
        date = datetime.fromtimestamp(int(r[3])/1000)
        review = {
        'review_id': r[1],
        'rating': r[2],
        'data': date,
        'summary': r[4],
        'body': r[5],
        'recommend': r[6],
        'reported': r[7],
        'reviewer_name': r[8],
        'response': r[10],
        'helfulness': r[11],
        'photo': []
        }
        results.append(review)
    return results


def getReviews(request):
    if request.method == 'GET':
        product_id = request.args.get('product_id', default=1)
        page = request.args.get('page', default=1)
        count = request.args.get('count', default=5)
        cur.execute(findReviews, (product_id,))
        reviews = cur.fetchall()
    
        print(product_id, page, count)
        data = transform(reviews)
        return {'results': data}
    else:
        return 'post reviews'