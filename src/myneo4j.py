from neo4j import GraphDatabase


class App:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(
                self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, params=None, db='dblpcopy'):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(
                database=db) if db is not None else self.__driver.session()
            response = list(session.run(query, params))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response
    
            
    
# delete all nodes that are NOT in the csv file
query_onlyKeepTopConferences = '''LOAD CSV 
                          FROM 'file:///'+$filecsv AS row 
                          WITH COLLECT(row[0]) AS list 
                          MATCH(v:Venue) 
                          WHERE NOT v.name IN list 
                          DETACH DELETE v'''

# alternative: add labels to the top conferences
query_addLabelsToTopConferences = '''LOAD CSV 
                             FROM $filecsv AS row 
                             WITH COLLECT(row[0]) AS list 
                             MATCH(v:Venue) 
                             WHERE v.name IN list 
                             SET v:Top200'''

query_createTopConfisGraph = '''CALL gds.graph.create('topVenues', ['Top200','Articles'], 'VENUE')'''

if __name__ == "__main__":
    topVenuesCSV = "file:///venues_top_conferences.csv"
    app = App(uri="bolt://localhost:7687", user="neo4j", pwd="frosch")
    # app.query(query=addLabelsToTopConferences, params={
    #                      "filecsv": topVenuesCSV}, db='dblp')
    app.query(query=query_createTopConfisGraph)
    app.close()