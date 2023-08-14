from flask import Flask

# Creating application instance for opertaions
FAI=Flask(__name__)

# Creating routing
@FAI.route('/wish')

# Creating view for string response
def wish():
    return '<center><h1><b> This is string response of Flask </b></h1></center>'

# Ruuning of server
if __name__=='__main__':
    FAI.run(debug = True)