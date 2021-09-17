# -*- coding: utf-8 -*-
import glob
import json
import csv
import os

os.chdir("./code/import")
srcPath_glob = "./dblp-ref/transformed/dblp-ref-0_cut.json"

articles = {}
authors = set()
venues = set()


def write_header(file, fields):
    csv.writer(file, delimiter=",").writerow(fields)


with open("./data/xxs/article_REFERENCES_article.csv", "w", encoding="utf-8") as article_references_article_file, \
        open("./data/xxs/article_REFERENCES_article_header.csv", "w", encoding="utf-8") as article_references_article_header_file, \
        open("./data/xxs/article_AUTHOR_author.csv", "w", encoding="utf-8") as article_author_author_file, \
        open("./data/xxs/article_AUTHOR_author_header.csv", "w", encoding="utf-8") as article_author_author_header_file, \
        open("./data/xxs/article_VENUE_venue.csv", "w", encoding="utf-8") as article_venue_venue_file, \
        open("./data/xxs/article_VENUE_venue_header.csv", "w", encoding="utf-8") as article_venue_venue_header_file:

    write_header(article_references_article_header_file, [
                 ":START_ID(Article)", ":END_ID(Article)"])
    write_header(article_author_author_header_file, [
                 ":START_ID(Article)", ":END_ID(Author)"])
    write_header(article_venue_venue_header_file, [
                 ":START_ID(Article)", ":END_ID(Venue)"])

    articles_references_article_writer = csv.writer(
        article_references_article_file, delimiter=",")
    article_author_author_file_writer = csv.writer(
        article_author_author_file, delimiter=",")
    article_venue_venue_file_writer = csv.writer(
        article_venue_venue_file, delimiter=",")

    for file_path in glob.glob(srcPath_glob):
        print(file_path)
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                item = json.loads(line)
                articles[item["id"]] = {"abstract": item.get("abstract", ""),
                                        "title": item["title"], "year": item["year"]}

                venue = str(item["venue"]).replace("\"", "")
                if venue:
                    venues.add(venue)
                    article_venue_venue_file_writer.writerow(
                        [item["id"], venue])

                for reference in item.get("references", []):
                    reference = str(reference).replace("\"", "")
                    articles_references_article_writer.writerow(
                        [item["id"], reference])

                for author in item.get("authors", []):
                    author = str(author).replace("\"", "")
                    authors.add(author)
                    article_author_author_file_writer.writerow(
                        [item["id"], author])

                line = file.readline()

with open("./data/xxs/articles.csv", "w", encoding="utf-8") as articles_file, \
        open("./data/xxs/articles_header.csv", "w", encoding="utf-8") as articles_header_file, \
        open("./data/xxs/authors.csv", "w", encoding="utf-8") as authors_file, \
        open("./data/xxs/authors_header.csv", "w", encoding="utf-8") as authors_header_file, \
        open("./data/xxs/venues.csv", "w", encoding="utf-8") as venues_file, \
        open("./data/xxs/venues_header.csv", "w", encoding="utf-8") as venues_header_file:
    write_header(articles_header_file, [
                 "index:ID(Article)", "title:string", "abstract:string", "year:int"])
    write_header(authors_header_file, ["name:ID(Author)", ])
    write_header(venues_header_file, ["name:ID(Venue)"])

    articles_writer = csv.writer(articles_file, delimiter=",")
    for article_id in articles:
        article = articles[article_id]
        articles_writer.writerow(
            [article_id, str(article["title"]).replace("\"", ""), str(article["abstract"]).replace("\"", ""), article.get("year")])

    authors_writer = csv.writer(authors_file, delimiter=",")
    for author in authors:
        # replacing quotes -> there are still quotes in the output but only in the beginning and end.
        # IDK why this is the behaviour
        author = str(author).replace("\"", "")
        authors_writer.writerow([author])

    venues_writer = csv.writer(venues_file, delimiter=",")
    for venue in venues:
        venue = str(venue).replace("\"", "")
        venues_writer.writerow([venue])
