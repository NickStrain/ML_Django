from django.db import models
from django.apps import AppConfig

class Endpoint(models.Model):
    '''
    The Endpoint object represents ML API endpoint.

    Attributes:
        name: The name of the endpoint, it will be used in API URL,
        owner: The string with owner name,
        created_at: The date when endpoint was created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represent the ML algoritm object.
    
    Attributes:
        name:The name of the algorithm 
        description: The short description of how the algorithm works
        code: the code of the algorithm
        versrion: The version of the algorithm similar to software versioning
        ower: The name of the ower.
        created_at: The data whem MLAlgorithm was added
        parent_endpoints: The reference to the Endpoint.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    created_at = models.CharField(max_length=128)
    parent_endpoint = models.ForeignKey(Endpoint,on_delete=models.CASCADE)
    
class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgoritnStatus represent status of the MLAgorithm which can change during the time 
    
    Attributes:
        status: The status of algorithm in the endpoints. Can be: testing,staging,production,ab_testing.
        active: The boolean flag which points to currently actuve status.
        created_by: The name of creator.
        created_at: The date of status creation 
        parent_mlalgorithm: The refrence to coreresponding MLAlgorithm
    '''
    
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_on  = models.DateTimeField(auto_created=True,blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete=models.CASCADE,related_name="status")
    
class MLRequest(models.Model):
    '''
    The MLRequest will keep information about all request to ML algorithms.
    
    Attributes:
        input_data: The input data to ML algorithm in JSON format.
        full_response: The response of the ML algorithm in JSON format.
        response: The response of the ML algorithm in JSON format
        feedback : The feedback about the responce in JSON format 
        created_at: The date when request was created.
        parent_mlalgorithm: The reference to MLAlgorithm used to compute responce 
    '''
    
    input_data = models.CharField(max_length=10000)
    full_response= models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback =  models.CharField(max_length=10000,blank=True,null=True)
    created_at = models.DateTimeField(auto_created=True,blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete=models.CASCADE)
    
    