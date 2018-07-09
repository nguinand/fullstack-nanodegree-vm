from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi  # common gateway interface


# handler indicates what code to execute based on the type of http request that is sent to the server
class webServerHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      if self.path.endswith("/hello"):  # looks for URL that ends with /hello
        self.send_response(200)  # indicates successful get request
        self.send_header('Content-type', 'text/html')  # indicate that we are replying with text
        self.end_headers()

        output = ""
        output += "<html><body><h1>Hello World!<h1><p>Web server running</p> <a href ='/hola'> Back to " \
                  "Hello</a> "
        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>" \
                    "What would you like me to say?</h2><input name='message' type='text' >" \
                    "<input type='submit' value='Submit'></form>"
        output += "</body></html>"
        self.wfile.write(output)
        print output
        return

      if self.path.endswith("/hola"):  # looks for URL that ends with /hello
        self.send_response(200)  # indicates successful get request
        self.send_header('Content-type', 'text/html')  # indicate that we are replying with text
        self.end_headers()

        output = ""
        output += "<html><body><h1>&#16Hola Mundo!<h1><p>Web servico correndo</p> <a href ='/hello'> Back to " \
                  "Hello</a> "
        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>" \
                    "What would you like me to say?</h2><input name='message' type='text' >" \
                    "<input type='submit' value='Submit'></form>"
        output += "</body></html>"
        self.wfile.write(output)
        print output
        return

    except IOError:
      self.send_error(404, "File Not Found %s" % self.path)

  def do_POST(self):
    try:
      self.send_response(301)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      ctype, pdict = cgi.parse_header(
        self.headers.getheader('content-type'))
      if ctype == 'multipart/form-data':
        fields = cgi.parse_multipart(self.rfile, pdict)
        messagecontent = fields.get('message')
      output = ""
      output += "<html><body>"
      output += " <h2> Okay, how about this: </h2>"
      output += "<h1> %s </h1>" % messagecontent[0]
      output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to 
      say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form> '''
      output += "</body></html>"
      self.wfile.write(output)
      print output
    except:
      pass


# main--> instantiate our server and specify what port it will listen on
def main():
  try:
    port = 8080
    server = HTTPServer(('', port), webServerHandler)
    print "Web server running on port %s" % port
    server.serve_forever()

  except KeyboardInterrupt:
    print("^C entered, stopping web server...")
    server.socket.close()


if __name__ == '__main__':
  main()
