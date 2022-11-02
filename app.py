# PIRDDIQ Database

import grist
from functions import *
import math, datetime, re

@grist.UserTable
class Replicated_Pima_Indians_Dataset_for_Diabetes_PIRDDIIQ_Responses:
  Timestamp  = grist.Any()
  Email_Address = grist.Any()

