#!/usr/bin/env python
# tutorial1-server.py
# run an ariadne wsgi simple server

''' a graphql server on ariadne wsgi simple server 

    Dependency: At writing of this code, it's installed ariadne 0.10.0 from master, 
    and graphql-core 3.0.3, starlette 0.13.2, typing-extensions 3.7.4.1 from pypi. 
    
    The graphql part of the code is from ariadne doc intro page. 
    
    How to run: Run this file. Point a browser to the port. Send a request 
    from the built-in playground in the browser. See the main() function. 
'''

from ariadne import gql, QueryType, make_executable_schema
from ariadne.wsgi import GraphQL

# the schema
type_defs = gql("""
    type Query {
        hello: String!
        who: String
        howMany: Int!
        howOld: Int
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    # the two lines below does not work. use HTTP_USER_AGENT.
    ##request = info.context["request"]
    ##user_agent = request.headers.get("user-agent", "guest")
    user_agent = info.context["HTTP_USER_AGENT"]
    return "Hello, %s!..." % user_agent #

schema = make_executable_schema(type_defs, query)
application = GraphQL(schema, debug=True)

def main():
    '''
        send a query in playground:
            query { hello }
            
        or send a query via curl:
            curl 'http://localhost:8051/graphql' \\
                   -H 'Accept-Encoding: gzip, deflate, br' \\
                   -H 'Content-Type: application/json' \\
                   -H 'Accept: application/json' -H 'Connection: keep-alive' \\
                   -H 'DNT: 1' -H 'Origin: http://localhost:8051' \\
                   --data-binary '{"query":"{hello}"}' --compressed
    '''
    do_single, do_loop = False, True

    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    if do_single:
        # Wait for a single request, serve it and quit.
        httpd.handle_request()
    elif do_loop:
        while True:
            httpd.handle_request()
            import time
            time.sleep(0.5)
    else:
        httpd.serve_forever(.5)

if __name__ == '__main__':
    main()

