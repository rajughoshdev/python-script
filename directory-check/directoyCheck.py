#!/usr/bin/env python

import os 
import os.path

if os.path.isdir("/raju"):
    print "yeah is a directory"
else: 
    print "/tmp is not a directory"

if os.path.isfile("/raju/ddd"):
    print "this is a file"
else: print "its not a file"

if os.path.exists("/raju/abcd"):
   print"yeah the file is exists"

else: 
    print "no not exist "