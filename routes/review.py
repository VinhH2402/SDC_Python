import mysql.connector as mysql
from datetime import datetime

mydb = mysql.connect(host="localhost")
cur = mydb.cursor()

cur.execute('USE reviewAPI')

# query
reviewQuery = '''SELECT  
                review.* , 
                group_concat(DISTINCT photo.url) as 'photos'
                FROM review 
                LEFT JOIN photo ON review.id = photo.review_id
                WHERE product_id = %s
                GROUP BY review.id'''


def transform(data):
    results = []
    for r in data:
        date = datetime.fromtimestamp(int(r[3])/1000)
        print(type(r[12]))
        photo = []
        if(r[12] is not None):
            photo = r[12].split(',')
        review = {
            'review_id': r[1],
            'rating': r[2],
            'date': date,
            'summary': r[4],
            'body': r[5],
            'recommend': r[6],
            'reviewer_name': r[8],
            'response': r[10],
            'helfulness': r[11],
            'photos': photo
        }
        results.append(review)
    return results


def getReviews(request):
    if request.method == 'GET':
        product_id = request.args.get('product_id', default=1)
        page = request.args.get('page', default=1)
        count = request.args.get('count', default=5)
        cur.execute(reviewQuery, (product_id,))
        reviews = cur.fetchall()

        data = transform(reviews)

        return {
            'product': product_id,
            'page': page,
            'count': count,
            'results': data
        }
    else:
        return 'post reviews'
