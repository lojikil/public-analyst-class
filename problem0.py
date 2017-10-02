from bottle import run, route, request

# a simple example to show where 
# sensitive data can end up
# idea: issue a request with a SSN, such as
# localhost:8081/search-users?ssn=some-ssn
# Look in your browser's history, as well as
# the console that is running logs the results 
# which would normally end up on the file 
# system

@route('/search-users')
def search_users():
    ssn = request.GET.get('ssn')
    return ssn

run(host='0.0.0.0', port=8081)
