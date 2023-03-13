from django.db import models

# contact section
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    



# video uploading section    
class Video(models.Model):
    video = models.FileField(upload_to="video")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    

#category   
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
#courses uploading section
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courseimages')
    price = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    

    
# signup form model
class Signup(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.firstname
    
    @staticmethod
    def get_customer_by_firstname(firstname=firstname):
        try:
            return Signup.objects.get(firstname=firstname)
        except:
            return False

    



