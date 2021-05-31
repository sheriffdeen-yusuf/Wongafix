from django.db import models

# Create your models here.
# If you don’t specify primary_key=True for any field in your model, Django will automatically add a field to hold the primary key,
# primary_key=True implies null=False and unique=True

class ConsumerLForm(models.Model):
    # personal information
    consumer_id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    dob = models.DateField()
    number = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField(null=False, blank=False, unique=True)
    hom_addr = models.CharField(max_length=200, blank=False)
    maritalS = models.BooleanField(null=False, blank=False)

    # office information
    emplym_info = models.TextField(null=False, blank=False)
    offc_email = models.EmailField(null=False, blank=False, unique=True)
    offc_numb = models.DecimalField(max_digits=11, decimal_places=0)
    monthly_income = models.DecimalField(max_digits=20, decimal_places=2)
    salary = models.DecimalField(decimal_places=2, max_digits=15)

    # Consumer bank information
    acct_name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    bank_name = models.CharField(max_length=200, null=False, blank=False)
    acct_no = models.DecimalField(max_digits=11, decimal_places=0)
    bvn = models.DecimalField(max_digits=10, null=False, decimal_places=0)
    acct_name2 = models.CharField(max_length=200, null=False, blank=False, unique=True)
    bank_name2 = models.CharField(max_length=200, null=False, blank=False)
    acct_no2 = models.DecimalField(max_digits=10, null=False, decimal_places=0)

    # loan information
    loan_words = models.CharField(max_length=200, blank=False, help_text="Please write amount in words")
    loan_figure = models.DecimalField(max_digits=9, decimal_places=2, help_text="Please write amount in figures")
    loan_descrp = models.TextField()
    signature = models.ImageField(upload_to='uploads/images', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    id_upload = models.ImageField(upload_to='uploads/images', null=False, blank=False)
    # The end of field for this table

    def __str__(self):
        return self.name




class BusinessLForm(models.Model):
    # personal information
    business_id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    dob = models.DateField()
    email = models.EmailField(null=False, blank=False, unique=True)
    number = models.DecimalField(max_digits=11, decimal_places=0)
    hom_addr = models.CharField(max_length=200, blank=False)
    maritalS = models.BooleanField(null=False, blank=False)

    # Business information
    busiz_name = models.TextField(null=False, blank=False)
    offc_addr = models.CharField(max_length=200, null=False, blank=False, unique=True)
    offc_email = models.EmailField(null=False, blank=False, unique=True)
    offc_numb = models.DecimalField(max_digits=11, decimal_places=0)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    busiz_regno = models.CharField(max_length=200, blank=False)
    busiz_nature = models.TextField()

    # Business/loan bank information 
    acct_no = models.DecimalField(max_digits=11, decimal_places=0)
    bank_name = models.CharField(max_length=200, null=False, blank=False)
    branch = models.CharField(max_length=200, null=False, blank=False, unique=False)
    bvn = models.DecimalField(max_digits=10, null=False, decimal_places=0)
    loan_amount = models.DecimalField(max_digits=20, decimal_places=2)
    loan_descrp = models.TextField()
    tenor_of_loan = models.CharField(max_length=200, null=False, blank=False)
    prev_loan = models.BooleanField(null=False, blank=False)    
    collecterials = models.TextField(null=False, blank=False, unique=True)

    # Guarantor's information 1
    guar_name = models.CharField(max_length=150, null=False, blank=False)
    house_addr = models.CharField(max_length=200, null=False, blank=False)
    offc_addr = models.CharField(max_length=200, null=False, blank=False)
    numb = models.DecimalField(max_digits=11, decimal_places=0)
    monthly_income = models.DecimalField(max_digits=15, decimal_places=2)
    guar_collecterials = models.TextField(null=False, blank=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    gur_id_1 = models.ImageField(upload_to='uploads/images', null=False, blank=False)

    # Gurantor's information 2
    guar_name2 = models.CharField(max_length=150, null=False, blank=False)
    house_addr2 = models.CharField(max_length=200, null=False, blank=False)
    offc_addr2 = models.CharField(max_length=200, null=False, blank=False)
    numb2 = models.DecimalField(max_digits=11, decimal_places=0)
    monthly_income2 = models.DecimalField(max_digits=15, decimal_places=2)
    guar_collecterials2 = models.TextField(null=False, blank=False, unique=True)
    date2 = models.DateTimeField(auto_now_add=True)
    gur_id_2 = models.ImageField(upload_to='uploads/images', null=False, blank=False)

    # The end of field for this table

    def __str__(self):
        return self.name



class Admins(models.Model):
    admin_id =  models.AutoField(primary_key=True, null=False, blank=False, unique=True)
    fullname =  models.CharField(max_length=100, null=False, blank=False)
    number =    models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField(null=False, blank=False, unique=True)
    password =  models.CharField(max_length=20,null=False, blank=False)

    # The end of field for this table

    def __str__(self):
        return self.fullname



class LoanGiven(models.Model):
    transac_id = models.IntegerField(null=False, unique=True)
    consumer_id = models.ForeignKey(ConsumerLForm, on_delete=models.CASCADE)
    date_given = models.DateTimeField(auto_now_add=True)
    amount_given = models.DecimalField(max_digits=15, decimal_places=2)
    admin_id = models.ForeignKey(Admins, on_delete=models.CASCADE)
        
    # The end of field for this table

    def __str__(self):
        return self.consumer_id



class PaymentFromConsumer(models.Model):
    transac_id = models.IntegerField(null=False, unique=True)
    consumer_id = models.ForeignKey(ConsumerLForm, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    laon_amount =  models.DecimalField(max_digits=20, decimal_places=2)
    amount_remains = models.DecimalField(max_digits=10, decimal_places=2)
    remark =  models.CharField(default='pending', max_length=20)

    # The end of field for this table



class PaymentFromBusiness(models.Model):
    transac_id = models.IntegerField(null=False, unique=True)
    business_id = models.ForeignKey(BusinessLForm, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    laon_amount = models.ForeignKey(ConsumerLForm, on_delete=models.CASCADE)
    amount_remains = models.DecimalField(max_digits=10, decimal_places=2)
    remark =  models.CharField(default='pending', max_length=20)

    # The end of field for this table
















  