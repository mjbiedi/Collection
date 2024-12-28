#!/usr/bin/python3

import os

###########################################################
def remove_bad_characters(file_name):
    bad_characters = [ ' ', '"', '#', '/', '\'' ]
    for c in bad_characters:
        file_name = file_name.replace(c, '')
    return file_name
    
###########################################################
def get_key_file_name(file_name):
    base_name = os.path.basename(file_name)
    return remove_bad_characters(base_name)

###########################################################
def get_files(collection, base_dir, extension):

    d = os.listdir(base_dir)
    for name in d:
        new_name = os.path.join(base_dir, name)
        if os.path.isdir(new_name):
            get_files(collection, new_name, extension)
        elif os.path.isfile(new_name):
            name, ext = os.path.splitext(new_name)
            if ext == extension:
                key_file = get_key_file_name(name)
                collection.update({key_file : new_name})


###########################################################
if __name__ == '__main__':

    movies = {}
    path = '/mnt/Data/Movies'
    get_files(movies, path, '.iso')
    count = 0
    for key in movies:
        count += 1
        print("[%4d] %35s : %s" %(count, key, movies[key]))

