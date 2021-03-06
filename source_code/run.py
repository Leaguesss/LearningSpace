#-----------------------------------------------------------------------------
# Get our components
# You may eventually wish to put these in their own directories and then load
from bottle import run
import controller
# import populate_data # import to generate db

# It might be a good idea to move the following settings to a config file and then load them
host = 'localhost' # Change this to your IP address or 0.0.0.0 when actually hosting
port = 8081 # change to the appropriate port to host

# Turn this off for production
debug = True
reloader = True
#-----------------------------------------------------------------------------

#Run the server if using this file directly
if __name__ == '__main__':
    run(host=host, port=port, debug=debug, reloader=reloader)

# http://localhost:8080/
