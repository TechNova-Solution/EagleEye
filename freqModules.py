############################################################################
# """
#
#     project: EagleEye -> This python project allows us to check whether a
#             given set of numerical data obeys the "Benford Law" or not
#             and also generate data based on the "Benford Law".
#
#             ReadMore: https://en.wikipedia.org/wiki/Benford%27s_law
#
#     Deccription: This module makes up of the frequently used fuctions
#                 and Constants in this app. see 'app.py' for implementation
# """
###########################################################################

import os
# get the upload folder in the current working directory/server
UPLOAD_FOLDER = os.getcwd()+'/upload'
# upload extension supported
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    """ Returns 'True' if a file is part of the supported extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def file_to_list(file):
    """ It takes a .csv file as a parameter and returns a list """
    temp = open('upload/'+file, 'r+')
    data = temp.read()
    values = data.split(',')
    temp.close()
    for v in range(len(values)):
        values[v] = int(values[v])
    return values
