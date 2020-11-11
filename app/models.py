from django.db import models
from enum import Enum

class MandalLocation(Enum):
    ''' 
        It refers to the location of the eight topics around the central topic.  
    '''
    LOCATION_0 = 0
    LOCATION_1 = 1
    LOCATION_2 = 2
    LOCATION_3 = 3
    LOCATION_4 = 4
    LOCATION_5 = 5
    LOCATION_6 = 6
    LOCATION_7 = 7
    LOCATION_8 = 8

class MandalWithSection:
    pass

class MandalCoreManager(models.Manager):
    def create_mandalart_with_sections(self, mandal_with_sections):
        '''
            @param mandal_with_section 

        '''
        pass

class MandalCore(models.Model):
    objects = MandalCoreManager()
    descr = models.CharField(unique=True, max_length=200, null=False, blank=False)
    location = models.CharField(max_length=20, default=MandalLocation.LOCATION_0.value)

    class Meta:
        db_table = "mandal_core"

    pass


class MandalDetail(models.Model):
    pass


class MandalSection(models.Model):
    """
    [  section_1  ] [  section_2  ] [  section_3  ]
    [  section_8  ] [  section_0  ] [  section_4  ]
    [  section_7  ] [  section_6  ] [  section_5  ]
    """

    core = models.ForeignKey("MandalCore", on_delete=models.CASCADE)
    location = models.CharField(max_length=20, default=MandalLocation.LOCATION_0.value)
    descr = models.CharField(max_length=200, blank=True, null=False)

    class Meta:
        db_table = "mandal_section"

    def __str__(self):
        return f"SECTION = ( {self.location} : {self.descr} )"
