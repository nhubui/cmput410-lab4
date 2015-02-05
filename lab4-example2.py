from flask import Flask, request, url_for, redirect # flask localhost port is default to 5000
app = Flask(__name__) #this name is used when you are using just 1 file, not package?
tasks = []

@app.route('/') 
def welcome():
    return '<h1> Welcome to Flask lab!</h1>'

@app.route('/task1', methods= ['GET', 'POST'])
def task():
    #POST:
    if request.method == 'POST':
        category = request.form['category']
        priority = request.form['priority']
        description= request.form['description']
        tasks.append({'category':category})
       # tasks.append({'priority':priority})
       # tasks.append({'description':description})
        #return redirect('/task1')
        return redirect(url_for('task'))
        
    #GET:
    resp = '''
    <form action="" method = post>
    <p>Category: <input type='text' name='category'></p>
    <p>Priority: <input type='text' name='priority'></p>
    <p>Description: <input type='text' name='description'></p>
    <p><input type='submit' value='Add'></p>
    </form>
    '''
            
    #Show the table:
    resp = resp + '''
    <table border="1" cellpadding="3">
    <tbody>
    <tr>
    <td>Category</td>
    <td>Priority</td>
    <td>Description</td>
    </tr>    
    '''
    for task in tasks:
            resp = resp + "<tr><td>%s</tr></td>" %(task['category'])
            #resp = resp + "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(task['category'],task['priority'],task['description'])
    resp = resp + '</tbody></table>'
    return resp


if __name__ == '__main__': #checks if this is run directly and not imported from elsewhere
    app.debug = True #for debugging purposes
    app.run()