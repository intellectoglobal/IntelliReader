from django.db import models
from users.models import NewUsers

class Documents(models.Model):
    DocID = models.AutoField(primary_key=True)
    DocName = models.CharField(max_length= 255)
    DocType = models.CharField(max_length = 50, blank= True)
    DocExtn = models.CharField(max_length= 10, null = True, blank = True)
    DocLang = models.CharField(max_length= 50, null = True, blank = True)
    DocPath = models.CharField(max_length = 255)
    UploadData = models.DateTimeField(auto_now_add = True)
    LastAccessed = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.DocName
    
class MasterTools(models.Model):
    ToolID = models.AutoField(primary_key=True)
    ToolName = models.CharField(max_length = 255)
    Description = models.TextField()

    def __str__(self):
        return self.ToolName
    
class ToolsUsage(models.Model):
    TaskID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(NewUsers, on_delete=models.DO_NOTHING)
    ToolID = models.ForeignKey(MasterTools, on_delete= models.DO_NOTHING)
    DocID = models.ForeignKey(Documents, on_delete= models.DO_NOTHING)
    Os = models.CharField(max_length= 100)
    Input_Path = models.CharField(max_length= 255)
    Output_Path = models.CharField(max_length = 255)

    def __str__(self):
        return self.TaskID

class ActivityLogs(models.Model):
    LogID = models.AutoField(primary_key=True)
    TaskID = models.ForeignKey(ToolsUsage, on_delete= models.DO_NOTHING)
    UserID = models.ForeignKey(NewUsers, on_delete=models.DO_NOTHING)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    ExecutionTime = models.IntegerField()
    Location = models.CharField(max_length = 255)
    Status = models.BooleanField(default=False)
    Comments = models.TextField()

