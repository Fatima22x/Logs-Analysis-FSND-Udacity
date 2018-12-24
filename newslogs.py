#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# Most viewed articles
query1 = "select title, count(title) as article_views from articles,log "
query1 += "where log.path = concat('/article/',articles.slug) "
query1 += "group by title order by article_views desc limit 3;"

# Most viewed authors
query2 = "select authors.name, "
query2 += "count(articles.author) as views from articles, log, authors "
query2 += "where log.path = concat('/article/',articles.slug) "
query2 += "and articles.author = authors.id group by authors.name "
query2 += "order by views desc;"

# Days where error is more than 1
query3 = "select Date, (Error*100.0)/Total as Percent "
query3 += "from (select time::timestamp::date as Date, "
query3 += "count(status) as Total, sum(case when status = '404 NOT FOUND' "
query3 += "then 1 else 0 end) as Error from log "
query3 += "group by time::timestamp::date) as result "
query3 += "where (Error*100.0)/Total > 1.0 order by Percent desc;"


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


def most_viewed_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query2)
    authors = c.fetchall()
    db.commit()
    db.close()
    print("\nMost popular authors:\n")
    for x in range(0, len(authors)):
        print(authors[x][0] + " - " + str(authors[x][1]) + " views")


def error_in_day():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query3)
    errors = c.fetchall()
    db.commit()
    db.close()
    print("\nDays where error was more than %1:\n")
    for x in range(0, len(errors)):
        print(str(errors[x][0]) + " - " + str(round(errors[x][1], 4)) + "%")


# Calling methods
most_viewed_articles()
most_viewed_authors()
error_in_day()
