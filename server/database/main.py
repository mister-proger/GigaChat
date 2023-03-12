import json
import datetime



def write_user_history(name, string):

    with open('database/users/' + name + '.hs', 'a+') as datafile:

        datafile.write('<' + str(datetime.datetime.now()) + '> ' + string + '\n')



def write_server_history(string):

    with open('database/server/server.hs', 'a+') as datafile:

        datafile.write('<' + str(datetime.datetime.now()) + '> ' + string + '\n')



def auth(id, password):

    with open('database/users/db.json', 'r') as datafile:

        database = json.load(datafile)

    if id in database.keys():

        if database[id]['password'] == password:

            return True

        else:

            return False

    else:

        return False



def get_mask(id, number = 0):

    return json.load(open('database/users/db.json', 'r'))[id]['masks'][number]



def add_mask(id, mask):

    file = open('database/users/db.json', 'r')

    database = json.loads(file, 'r')

    file.close()

    with open('database/users/db.json', 'w') as datafile:

        database[id]['masks'].insert(mask, 0)

        datafile.write(json.dumps(database))