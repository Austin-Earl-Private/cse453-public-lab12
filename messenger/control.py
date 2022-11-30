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


class Control(Enum):
    UNCLASSIFIED = 1
    PUBLIC = 2
    CONFIDENTIAL = 3
    SECRET = 4
    TOP_SECRET = 5


def securityConditionRead(assetControl: Control, subjectControl: Control):
    return subjectControl >= assetControl


def securityConditionWrite(assetControl: Control, subjectControl: Control):
    return subjectControl <= assetControl
