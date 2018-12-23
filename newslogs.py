# "Database code" for the Logs Analysis Project
import psycopg2

DBNAME = "news"

# Most viewed articles
query1 = "select title, count(title) as article_views from articles,log where log.path = concat('/article/',articles.slug) group by title order by article_views desc limit 3;"

# Most viewed authors
query2 = "select authors.name, count(articles.author) as views from articles, log, authors where log.path = concat('/article/',articles.slug) and articles.author = authors.id group by authors.name order by views desc;"

# Days where error is more than 1
query3 = "select Date, (Error::float*100)/Total::float as Percent from (select time::timestamp::date as Date, count(status) as Total, sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error from log group by time::timestamp::date) as result where (Error::float*100)/Total::float > 1.0 order by Percent desc;"


# Method for each query
def most_viewed_articles():
     db = psycopg2.connect(database=DBNAME)
     c = db.cursor()
     c.execute(query1)
     articles = c.fetchall()
     db.commit()
     db.close()
     print("\nMost popular articles:\n")
     for x in range(0, len(articles)):
        print(articles[x][0] + " - " + str(articles[x][1]) + " views")
     return articles

def most_viewed_authors():
     db = psycopg2.connect(database=DBNAME)
     c = db.cursor()
     c.execute(query2)
     authors = c.fetchall()
     db.commit()
     db.close()
     print("\nMost popular authors:\n")
     for x in range(0, len(authors)):
        print(authors[x][0] + " - " + str(authors[x][1]))
     return authors

def error_in_day():
     db = psycopg2.connect(datab ase=DBNAME)
     c = db.cursor()
     c.execute(query3)
     errors = c.fetchall()
     db.commit()
     db.close()
     print("\nDays where error was more than %1:\n")
     for x in range(0, len(errors)):
        print(str(errors[x][0])+ " - "+str(round(errors[x][1], 4))+"% errors")
     return errors

# Calling methods
most_viewed_articles()
most_viewed_authors()
error_in_day()
