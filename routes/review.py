from flask_mysqldb import MySQL
from datetime import datetime
from flask import Flask

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reviewAPI'

mysql = MySQL(app)

# query
reviewQuery = '''SELECT  
                review.* , 
                group_concat(DISTINCT photo.url SEPARATOR ',') as 'photos'
                FROM review 
                LEFT JOIN photo ON review.id = photo.review_id
                WHERE product_id = %s
                GROUP BY review.id'''

reviewQuery2 = '''SELECT review.*,
                    group_concat(DISTINCT photo.url SEPARATOR ',') as 'photosURL',
                    group_concat(DISTINCT photo.id SEPARATOR ',') as 'photosID'
                    FROM review
                    LEFT JOIN photo 
                    ON review.id = photo.review_id
                    WHERE product_id = %s
                    GROUP BY review.id
                    '''

def sortList(data, sortBy):
    if sortBy == 'newest':
        data = sorted(data, key=lambda i: i['date'], reverse=True)
    elif sortBy == 'helpful':
        data = sorted(data, key=lambda i: i['helpfulness'], reverse=True)
    else:
        return 'invalid sort'
    return data


def transformPhoto(urls, ids):
    photos = []
    ids = ids.split(',')
    urls = urls.split(',')
    for i in range(len(ids)):
        photos.append({"id": ids[i], "url": urls[i]})
    return photos


def transform(data):
    results = []
    for r in data:
        date = str(datetime.fromtimestamp(int(r[3])/1000))
        photos = []
        if(r[12] != None):
            photos = transformPhoto(r[12], r[13])
        review = {
            'review_id': r[1],
            'rating': r[2],
            'date': date,
            'summary': r[4],
            'body': r[5],
            'recommend': r[6],
            'reviewer_name': r[8],
            'response': r[10],
            'helpfulness': r[11],
            'photos': photos
        }
        results.append(review)
    return results


def getReviews(request):
    cursor = mysql.connection.cursor()
    if request.method == 'GET':
        args = request.args.get
        product_id = args('product_id', default=1, type=str)
        page = args('page', default=1, type=int)
        count = args('count', default=5, type=int)
        sort = args('sort', default='newest', type=str)

        cursor.execute(reviewQuery2, (product_id,))
        data = cursor.fetchall()

        data = transform(data)
        data = sortList(data, sort)
        results = data[(page-1)*count : (page*count) + count]

        return {
            'product': product_id,
            'page': page,
            'count': count,
            'results': results
        }
    else:
        return 'post reviews'
