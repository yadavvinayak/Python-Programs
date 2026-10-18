
# In this example we will see how to use pickle module for storing the data efficiently!
# The pickle module translates an in-memory Python object into a serialized byte stream—a string of bytes
# that can be written to any file-like object.

import pickle

def storeData():
    # initializing data to be stored in db
    VinayakYadav = {'key' : 'VinayakYadav', 'name' : 'VinayakYadav', 'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Yadav', 'age' : 50, 'pay' : 50000}

    # database
    db = {}
    db['VinayakYadav'] = VinayakYadav
    db['Jagdish'] = Jagdish

    dbfile = open('examplePickle', 'ab')        # Its important to use binary mode
    pickle.dump(db, dbfile)                     # source, destination
    dbfile.close()

def loadData():
    dbfile = open('examplePickle', 'rb')        # for reading also binary mode is important
    db = pickle.load(dbfile)
    for keys in db:
        print(keys,'=>',db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()
