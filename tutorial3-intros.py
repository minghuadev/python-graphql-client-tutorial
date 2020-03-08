#!/usr/bin/env python
# tutorial3-intros.py
#    github.com/prisma-labs/python-graphql-client
#    github.com/palantir0/python-graphql-client
#    graphql-core-next.readthedocs.io/en/latest/usage/introspection.html

''' a graphql trial client demonstrating introspection

    This example constructs an introspection query, send the query to a server, 
    build a schema from the query result, and print the schema in SDL and pretty. 
    
    Then it pass the query into a local function tha also takes the built-schema 
    to return a result that is logically identical to the remote query, and 
    performe the same as from a remote query. 
    
    The remote query and local query should return the same result. 
    
    Dependency: It depends on the same packages as for tutorial2-client. 
    In addition, it uses the graphql-core 3.0.3 package from graphql-core-next. 

    To run against the tutorial1-server, start the server and run this file. 
    To run on swapi.graph.cool, uncomment the server_url and run. 
'''

from graphqlclient import GraphQLClient
from pprint import PrettyPrinter
import json

server_url = 'http://127.0.0.1:8051/'
#server_url = 'http://swapi.graph.cool/'
client = GraphQLClient(server_url)

from graphql import get_introspection_query
#from graphql import graphql_sync
from graphql import build_client_schema
from graphql import print_schema

def main():
    pp = PrettyPrinter(indent=4)

    # query over the network
    query_intros = get_introspection_query(descriptions=True)
    #introspection_query_result = graphql_sync(schema, query)
    intros_result = client.execute(query_intros, variables=None, operationName=None)
    client_schema = build_client_schema(intros_result.get('data', None))
    sdl = print_schema(client_schema)
    print(sdl)
    pp.pprint(sdl)
    print("\n")

    # query again using the graphql_sync()
    from graphql import graphql_sync
    introspection_query_result = graphql_sync(client_schema, query_intros)
    client_schema = build_client_schema(introspection_query_result.data)
    sdl = print_schema(client_schema)
    print(sdl)
    pp.pprint(sdl)
    print("\n")

if __name__ == '__main__':
    main()

