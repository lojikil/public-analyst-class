from bottle import route, run, request, template, response

user_data = []
strdtmp = """
<html>
  <head>
    <title>Stored XSS</title>
  </head>
  <body>
    <h2>Welcome to my Guestbook!</h2>
    Previous guests:<br />
    {{!previous_entries}}
    <hr />
    <form method="POST" action="/stored-xss">
      <label>Please enter your name for the guest book:</label>
      <input type="text" name="name">
      <input type="submit" value="Sign Guestbook">
    </form>
  </body>
</html>
"""

# idea 0: find the stored XSS here
# idea 1: use this for CSRF => Stored XSS
@route('/stored-xss', method=['get', 'post'])
def stored_xss():
    response.set_header('X-XSS-PROTECTION', '0')
    if request.method == "POST":
        user_data.append(request.POST.get('name', ''))

    previous_entries = '<br />'.join(user_data)
    return template(strdtmp, previous_entries=previous_entries)

@route('/reflected-xss')
def reflected_xss():
    response.set_header('X-XSS-PROTECTION', '0')
    errmsg = request.query.get("errmsg", "No Error Occurred")
    return "<b>Error: {0}</b>".format(errmsg)

run(host='0.0.0.0', port=8085)
