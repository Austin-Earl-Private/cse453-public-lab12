########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...
from enum import Enum

# following the listing of known policy levels
class Control(Enum):
    PUBLIC = 1
    CONFIDENTIAL = 2
    PRIVILEGED = 3
    SECRET = 4

#bell-lapadula check for reading privileges
def securityConditionRead(assetControl, subjectControl):
   try:
      return int(subjectControl.value) >= int(assetControl.value)
   except:
      return False

#bell-lapadula check for writing privileges
def securityConditionWrite(assetControl, subjectControl):
   try:
      return int(subjectControl.value) <= int(assetControl.value)
   except:
      return False
