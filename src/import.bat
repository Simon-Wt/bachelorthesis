cd C:\Users\simon\.Neo4jDesktop\relate-data\dbmss\dbms-bee63272-46b9-44e9-8306-8da4f2d6d037

set DATA_DIR=C:\Users\simon\Documents\BA\code\import\data\xxs

.\bin\neo4j-admin import ^
  --database=dblp10k ^
  --nodes=Author=%DATA_DIR%\authors_header.csv,%DATA_DIR%\authors.csv ^
  --nodes=Article=%DATA_DIR%\articles_header.csv,%DATA_DIR%\articles.csv ^
  --nodes=Venue=%DATA_DIR%\venues_header.csv,%DATA_DIR%\venues.csv ^
  --relationships=REFERENCES=%DATA_DIR%\article_REFERENCES_article_header.csv,%DATA_DIR%\article_REFERENCES_article.csv ^
  --relationships=AUTHOR=%DATA_DIR%\article_AUTHOR_author_header.csv,%DATA_DIR%\article_AUTHOR_author.csv ^
  --relationships=VENUE=%DATA_DIR%\article_VENUE_venue_header.csv,%DATA_DIR%\article_VENUE_venue.csv ^
  --multiline-fields=true ^
  --skip-duplicate-nodes=true ^
  --skip-bad-relationships=true