from django.db import models

# Create your models here.

class Contact(models.Model):
     contact_name=models.CharField(max_length=50)
     contact_email=models.CharField(max_length=20)
     contact_phone=models.CharField(max_length=50)
     contact_subject=models.CharField(max_length=100)
     contact_message=models.CharField(max_length=500)
      
class Registration(models.Model):
     PROGRAM_CHOICE = (('ADCA(Advance Diploma in Computer Application)','ADCA(Advance Diploma in Computer Application)'),
                      ('CCA(Certificate in Computer Application)','CCA(Certificate in Computer Application)'),
                      ('CCC(Course on Computer Concepts)','CCC(Course on Computer Concepts)'),
                      ('DTP(Desktop Publication)','DTP(Desktop Publication)'),
                      ('(Tally ERP 9)computer Accounting Course','(Tally ERP 9)computer Accounting Course'),
                      ('IGD Bombay Art','IGD Bombay Art'),
                      ('Computerized Mobile Repairing','Computerized Mobile Repairing'),
                      ('AutoCad','AutoCad'),
                      ('Computer Hardware & Networking','Computer Hardware & Networking'),
                      ('MCA(Master of Computer Application)','MCA(Master of Computer Application)'),
                      ('PGDCA','PGDCA'),
                      ('BCA(Bachlors of Computer Application)','BCA(Bachlors of Computer Application)'),
                      ('Web Designing','Web Designing'),
                      ('DCA 1 Year(Diploma in Computer Application)','DCA 1 Year(Diploma in Computer Application)'),
                      ('DRA(Diploma in Refrigeration & Air Conditioning)','DRA(Diploma in Refrigeration & Air Conditioning)'))
     GENDER_CHOICE = (('male','male'),('female','female'),('others','others'))
     STATUS_CHOICE = (('married','married'),('unmarried','unmarried'),('others','others')) 
     CATEGORY_CHOICE = (('general','general'),('obc','obc'),('sc','sc'),('st','st')) 
     BRANCH_CHOICE = (('br','br'),('acc','acc'),('gr','gr'),('fips','fips'),('sknb','sknb')) 
     course=models.CharField(max_length=100,choices=PROGRAM_CHOICE)
     qualification=models.CharField(max_length=100)
     name=models.CharField(max_length=100)
     father_name=models.CharField(max_length=100)
     gender=models.CharField(max_length=10,choices=GENDER_CHOICE)
     mother_name=models.CharField(max_length=100)
     date=models.DateField()
     address=models.CharField(max_length=200)
     status=models.CharField(max_length=20,choices=STATUS_CHOICE)
     pin=models.CharField(max_length=7)
     category=models.CharField(max_length=10,choices=CATEGORY_CHOICE)
     mail=models.CharField(max_length=50)
     phone=models.CharField(max_length=12)
     branch=models.CharField(max_length=50,choices=BRANCH_CHOICE)
     photo=models.CharField(max_length=50)
     
class Details(models.Model):
     PROGRAM_CHOICE = (('ADCA(Advance Diploma in Computer Application)','ADCA(Advance Diploma in Computer Application)'),
                      ('CCA(Certificate in Computer Application)','CCA(Certificate in Computer Application)'),
                      ('CCC(Course on Computer Concepts)','CCC(Course on Computer Concepts)'),
                      ('DTP(Desktop Publication)','DTP(Desktop Publication)'),
                      ('(Tally ERP 9)computer Accounting Course','(Tally ERP 9)computer Accounting Course'),
                      ('IGD Bombay Art','IGD Bombay Art'),
                      ('Computerized Mobile Repairing','Computerized Mobile Repairing'),
                      ('AutoCad','AutoCad'),
                      ('Computer Hardware & Networking','Computer Hardware & Networking'),
                      ('MCA(Master of Computer Application)','MCA(Master of Computer Application)'),
                      ('PGDCA','PGDCA'),
                      ('BCA(Bachlors of Computer Application)','BCA(Bachlors of Computer Application)'),
                      ('Web Designing','Web Designing'),
                      ('DCA 1 Year(Diploma in Computer Application)','DCA 1 Year(Diploma in Computer Application)'),
                      ('DRA(Diploma in Refrigeration & Air Conditioning)','DRA(Diploma in Refrigeration & Air Conditioning)'))
     BRANCH_CHOICE = (('result','result'),('certificate','certificate'))
     c_course=models.CharField(max_length=100,choices=PROGRAM_CHOICE)     
     c_type=models.CharField(max_length=50,choices=BRANCH_CHOICE)
     c_roll=models.CharField(max_length=5)
     