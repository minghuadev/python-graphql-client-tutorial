
see the pydoc for tutorials:

  python -m pydoc tutorial1-server
  python -m pydoc tutorial2-client
  python -m pydoc tutorial3-intros


===========================================================
Help on module tutorial1-server:

NAME
    tutorial1-server - a graphql server on ariadne wsgi simple server

DESCRIPTION
    Dependency: At writing of this code, it's installed ariadne 0.10.0 from master,
    and graphql-core 3.0.3, starlette 0.13.2, typing-extensions 3.7.4.1 from pypi.

    The graphql part of the code is from ariadne doc intro page.

    How to run: Run this file. Point a browser to the port. Send a request
    from the built-in playground in the browser. See the main() function.

FUNCTIONS
    main()
        send a query in playground:
            query { hello }

        or send a query via curl:
            curl 'http://localhost:8051/graphql' \
                   -H 'Accept-Encoding: gzip, deflate, br' \
                   -H 'Content-Type: application/json' \
                   -H 'Accept: application/json' -H 'Connection: keep-alive' \
                   -H 'DNT: 1' -H 'Origin: http://localhost:8051' \
                   --data-binary '{"query":"{hello}"}' --compressed

    resolve_hello(_, info)

DATA
    application = <ariadne.wsgi.GraphQL object>
    query = <ariadne.objects.QueryType object>
    schema = <graphql.type.schema.GraphQLSchema object>
    type_defs = '\n    type Query {\n        hello: String!\n       ...\n ...

===========================================================
Help on module tutorial2-client:

NAME
    tutorial2-client - a graphql trial client using http requests

DESCRIPTION
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

FUNCTIONS
    main()

DATA
    client = <graphqlclient.client.GraphQLClient object>
    queries_tested_ok = ['\n{\n    __schema {\n        types {\n          ...
    query_meta_raw1 = '{"operationName":"IntrospectionQuery","variables......
    query_meta_raw1m = r'{"operationName":"IntrospectionQuery","variables....
    query_meta_raw_ok1 = '\n{\n    __schema {\n        types {\n          ...
    query_meta_raw_ok2 = '\n{\n    __schema {\n        types { name }, que...
    query_meta_raw_ok3 = '{\n    __type(name: "Query"){ name, kind }\n}'
    query_meta_raw_ok4 = '{\n    __type(name: "Query"){ name, kind, \n    ...
    query_sample = '\n{\n    hello\n}\n'
    server_url = 'http://127.0.0.1:8051/'

===========================================================
Help on module tutorial3-intros:

NAME
    tutorial3-intros - a graphql trial client demonstrating introspection

DESCRIPTION
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

FUNCTIONS
    main()

DATA
    client = <graphqlclient.client.GraphQLClient object>
    server_url = 'http://127.0.0.1:8051/'

===========================================================

