#  
#  DB Script Tool
#  Python - 2022-11-07 05:26:26
#  
#  MODEL CLASSES FOR METABIS DATABASE
#



# METABIaaS.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - METABIS.METABIaaS
# 2022-11-07 05:07:21
#
class METABIaaS(Object):

    #
    # Constructor
    #
    # Example: 
    # myMETABIaaS = METABIaaS( val1, val2,.. )
    #
    def __init__(self, _id = None, journalname = None, articletitle = None, publicationdate = None, articlerentcost = None, ArticleAnswer = None):
        self.___id = _id
        self.__journalname = journalname
        self.__articletitle = articletitle
        self.__publicationdate = publicationdate
        self.__articlerentcost = articlerentcost
        self.__ArticleAnswer = ArticleAnswer


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def journalname(self):
        return self.__journalname

    @journalname.setter
    def journalname(self, journalname):
        self.__journalname = journalname

    @property
    def articletitle(self):
        return self.__articletitle

    @articletitle.setter
    def articletitle(self, articletitle):
        self.__articletitle = articletitle

    @property
    def publicationdate(self):
        return self.__publicationdate

    @publicationdate.setter
    def publicationdate(self, publicationdate):
        self.__publicationdate = publicationdate

    @property
    def articlerentcost(self):
        return self.__articlerentcost

    @articlerentcost.setter
    def articlerentcost(self, articlerentcost):
        self.__articlerentcost = articlerentcost

    @property
    def ArticleAnswer(self):
        return self.__ArticleAnswer

    @ArticleAnswer.setter
    def ArticleAnswer(self, ArticleAnswer):
        self.__ArticleAnswer = ArticleAnswer



    #
    # Methods
    #

    def __str__ (self):
        return ""
