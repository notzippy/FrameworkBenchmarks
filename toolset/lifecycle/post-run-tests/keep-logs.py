#!/usr/bin/python
#
# Archives, to the specified folder, the logged output generated by a benchmark 
# run.  
#
# @author A. Shawn Bandy
import os
import zipfile
import datetime
# Follows closely from:
# http://stackoverflow.com/a/34153816
#
# Paths to the log folders are generated by TFB and where those files 
# should be archived.
#
path_in = os.path.abspath(os.path.normpath(os.path.expanduser(os.path.join( \
    os.environ['TFB_REPOPARENT'], os.environ['TFB_REPONAME'], \
    'results/latest/logs'))))
date_time = datetime.datetime.now()
dt_folder = date_time.strftime('%Y%m%d%H%M%S')
path_out = os.path.abspath(os.path.join(os.environ['TFB_LOGSFOLDER'], \
    dt_folder))
# Step through each folder in the TFB log folder...
for folder in os.listdir(path_in):
  if not os.path.exists(path_out):
    os.makedirs(path_out)
  zip_file = zipfile.ZipFile(path_out + '/' + folder + '.zip', 'w')
# ... walk the folder structure ...
  for root, directories, files in os.walk(os.path.join(path_in, folder), 'w', \
        zipfile.ZIP_DEFLATED):
# ... and add to the zip file.   
    for file in files:
      try:
        zip_file.write(os.path.abspath(os.path.join(root, file)), \
            arcname=file)
      except OSError as err:
        print "An OSError occurred while writing to a log zip file for {0}: \
            {1}".format(file, err)
  zip_file.close()
