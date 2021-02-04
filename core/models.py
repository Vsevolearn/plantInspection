from django.db import models
from datetime import date
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


#Категория угрозы
class Category(models.Model):
    Name = models.CharField(max_length=200, verbose_name='name')
    Signature = models.CharField(max_length=200, verbose_name='signature')
    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Name

#Род растения
class Genus(models.Model):
    Name = models.CharField(max_length=200, verbose_name='name')

    class Meta():
        verbose_name = 'genus'
        verbose_name_plural = 'genus'
    
    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Name



#Экземпляр библиотеки угроз
class Exemplar(models.Model):
    Name = models.CharField(max_length=200, verbose_name='name', null=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Genus = models.ForeignKey(Genus,on_delete=models.CASCADE)
    Description = models.CharField(max_length=50000, verbose_name='description')
    Model = models.FileField( verbose_name='model')
    image = models.ImageField(verbose_name='image')

    class Meta():
        verbose_name = 'exemplar'
        verbose_name_plural = 'exemplar'

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Name

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        new_img = img.convert('RGB')

        basewidth = 800
        wpercent = (basewidth/float(new_img.size[0]))
        hsize = int((float(new_img.size[1])*float(wpercent)))
        new_img = new_img.resize((basewidth,hsize), Image.ANTIALIAS)

        resized_new_img = new_img.crop((0,0,400,400)) 
        filestream = BytesIO()
        resized_new_img.save(filestream, 'JPEG', quality = 90)
        filestream.seek(0)
        name = '{}.{}'.format(*self.image.name.split('.'))
        self.image = InMemoryUploadedFile(
            filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None
        )
        super().save(*args, **kwargs)

#Угроза экземпляра
class ThreatExemplar(models.Model):
    Exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, verbose_name='name')
    

    class Meta():
        verbose_name = 'ThreatExemplar'
        verbose_name_plural = 'ThreatExemplar'
    
    def __str__(self):
        return self.Exemplar.Name +"|"+self.Name

    def __unicode__(self):
        return self.Exemplar.Name +"|"+self.Name


#Изображения угрозы экземпляра
class ThreatExemplarImage(models.Model):
    ThreatExemplar = models.ForeignKey(ThreatExemplar, on_delete=models.CASCADE)
    Image = models.ImageField(verbose_name='image')

    class Meta():
        verbose_name = 'ThreatExemplarImage'
        verbose_name_plural = 'ThreatExemplarImage'

    def __str__(self):
        return self.ThreatExemplar.Exemplar.Name +"|"+self.ThreatExemplar.Name

    def __unicode__(self):
        return self.ThreatExemplar.Exemplar.Name +"|"+self.ThreatExemplar.Name
    

#Пользователь
class User(models.Model):
    Name = models.CharField(max_length=200, verbose_name='name')
    Email = models.CharField(max_length=200, verbose_name='email', default="", blank=True )
    Password = models.CharField(max_length=50, verbose_name='password', default="", blank=True )

    class Meta():
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Name



#Протокол
class Protocol(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    Address = models.CharField(max_length=200, verbose_name='address', default="", blank=True)
    Сoordinates = models.CharField(max_length=200, verbose_name='coordinates', default="", blank=True)
    Description = models.CharField(max_length=50000, verbose_name='description', default="", blank=True)
    
    Archive = models.FileField( verbose_name='archive', blank=True, null=True)
    Genus = models.ForeignKey(Genus,on_delete=models.CASCADE, blank=True, null=True)
    Note = models.CharField(max_length=50000, verbose_name='comments', default="", blank=True)
    Made = models.CharField(max_length=200, verbose_name='made', default="", blank=True)

    class Meta():
        verbose_name = 'protocol'
        verbose_name_plural = 'protocols'

    def __str__(self):
        return self.User.Name+"|"+ self.Date.strftime("%m/%d/%Y") +"|"+self.Address

    def __unicode__(self):
        return self.User.Name+"|"+ self.Date.strftime("%m/%d/%Y") +"|"+self.Address


#Экземпляр протокола (выбранный)
class ProtocolExemplarChoice(models.Model):
    Protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    Exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)

#Экземпляр протокола (найденный)
class ProtocolExemplarFind(models.Model):
    Protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    Exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)


class ProtocolFindImage(models.Model):
    ProtocolExemplarFind = models.ForeignKey(ProtocolExemplarFind, on_delete=models.CASCADE)
    Image = models.ImageField(verbose_name='image')
