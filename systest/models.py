from django.db import models
from django.utils import timezone


class System(models.Model): 
    systemcode = models.CharField(max_length=10)
    system = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')
    
    def __str__(self):
        return self.system

    
class Version(models.Model): 
    version_name = models.CharField(max_length=100)
    system_id = models.ForeignKey(System, on_delete=models.CASCADE)
    test_start_date = models.DateTimeField(blank=True, null=True)
    test_end_date = models.DateTimeField(blank=True, null=True)
    install_live_date = models.DateTimeField(blank=True, null=True)
    go_live_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')
    
    def __str__(self):
        return self.version_name
    
    
class Module(models.Model): 
    system_id = models.ForeignKey(System, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')
    
    def __str__(self):
        return self.module_name
    
class TestOverview(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    Description = models.TextField()
    expected_outcome = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')
    
    def __str__(self):
        return self.title
    

    
    
    
    
    


