import sys
sys.path.append('/Users/attreyeem/Desktop/projects/covidclickapp/env/lib/python3.7/site-packages/django/db')
import models

class Hospital:
    rating : float
    name : str
    number : int
    price : int
    address :  str


    

    def __str__(self):
        return self.title



# Create your models here.