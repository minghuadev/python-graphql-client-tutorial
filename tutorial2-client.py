#!/usr/bin/env python
# tutorial2-client.py
#    github.com/prisma-labs/python-graphql-client
#    github.com/palantir0/python-graphql-client

''' a graphql trial client using http requests

    This example runs a series of queries and prints the result for each of them. 

    Dependency: At writing of the code, it's installed the following packages 
    as shown by `pip-compile --output-file=requirements.txt setup.py` command
    when adding only the `requests` to the setup.py file instead of `six`: 

        certifi==2019.11.28       # via requests
        chardet==3.0.4            # via requests
        idna==2.9                 # via requests
        requests==2.23.0          # via graphqlclient (setup.py)
        urllib3==1.25.8           # via requests
        
    The graphqlclient module from python-graphql-client also needs to be in the path.
        
    To run against the tutorial1-server, start the server and run this file. 
    To run on swapi.graph.cool, uncomment the server_url and run. 
    
    To run the last two queries, uncomment them in the code. 
'''

from graphqlclient import GraphQLClient
from pprint import PrettyPrinter
import json

server_url = 'http://127.0.0.1:8051/'
#server_url = 'http://swapi.graph.cool/'
client = GraphQLClient(server_url)

# raw query dump from playground
query_meta_raw1 = '''{"operationName":"IntrospectionQuery","variables":{},"query":"query IntrospectionQuery {\n  __schema {\n    queryType {\n      name\n    }\n    mutationType {\n      name\n    }\n    subscriptionType {\n      name\n    }\n    types {\n      ...FullType\n    }\n    directives {\n      name\n      description\n      locations\n      args {\n        ...InputValue\n      }\n    }\n  }\n}\n\nfragment FullType on __Type {\n  kind\n  name\n  description\n  fields(includeDeprecated: true) {\n    name\n    description\n    args {\n      ...InputValue\n    }\n    type {\n      ...TypeRef\n    }\n    isDeprecated\n    deprecationReason\n  }\n  inputFields {\n    ...InputValue\n  }\n  interfaces {\n    ...TypeRef\n  }\n  enumValues(includeDeprecated: true) {\n    name\n    description\n    isDeprecated\n    deprecationReason\n  }\n  possibleTypes {\n    ...TypeRef\n  }\n}\n\nfragment InputValue on __InputValue {\n  name\n  description\n  type {\n    ...TypeRef\n  }\n  defaultValue\n}\n\nfragment TypeRef on __Type {\n  kind\n  name\n  ofType {\n    kind\n    name\n    ofType {\n      kind\n      name\n      ofType {\n        kind\n        name\n        ofType {\n          kind\n          name\n          ofType {\n            kind\n            name\n            ofType {\n              kind\n              name\n              ofType {\n                kind\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"}'''
query_meta_raw1m = query_meta_raw1.replace('\n', '\\n') # modified so that can be sent to a server.

# a first query
# got: Query, String, __Schema, __Type, __TypeKind, Boolean,
#      __Field, __InputValue, __EnumValue, __Directive, __DirectiveLocation
query_meta_raw_ok1 = '''
{
    __schema {
        types {
            name
        }
    }
}
'''

query_meta_raw_ok2 = '''
{
    __schema {
        types { name }, queryType { name }, mutationType { name }, subscriptionType { name }
    }
}
'''

# got:  {'data': {'__type': {'kind': 'OBJECT', 'name': 'Query'}}}
# OBJECT is a value of __TypeKind enum returned by kind
query_meta_raw_ok3 = '''{
    __type(name: "Query"){ name, kind }
}'''

# got:
# fields for an OBJECT
query_meta_raw_ok4 = '''{
    __type(name: "Query"){ name, kind, 
        fields { name, description, type { name, kind } }
    }
}'''

query_sample = '''
{
    hello
}
'''

queries_tested_ok = [
    query_meta_raw_ok1, query_meta_raw_ok2, query_meta_raw_ok3, query_meta_raw_ok4,
    query_sample,

    # remove the leading empty element below and uncomment the rest of line:
    '',  #json.loads(query_meta_raw1m).get("query", None),
    None, #json.loads(query_meta_raw1m)
]

def main():
    for n,q in enumerate(queries_tested_ok):
        print("\nQuery n %d " % n)
        query_meta = q
        tq = type(query_meta)
        if tq is str:
            query = query_meta
            vars = None
            oper = None
            if len(q.strip()) < 2:
                continue
        elif tq is dict:
            query = query_meta.get('query', None)
            vars = query_meta.get('variables', None)
            oper = query_meta.get('operationName', None)
            if query is None or vars is None:
                continue
        else:
            query = ""
            vars = None
            oper = None
            continue
        result = client.execute(query, variables=vars, operationName=oper)

        pp=PrettyPrinter(indent=4)
        pp.pprint(result)

if __name__ == '__main__':
    main()

