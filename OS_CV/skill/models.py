from django.db import models

class Skills(models.Model) :
    title = models.CharField(max_length=255 , blank=True , null=True , verbose_name="موضوع")
    description = models.TextField(blank=True , null=True , verbose_name="توضیحات")
    icon = models.ImageField(upload_to="skills/" , blank=True , null=True , verbose_name="آیکون مهارت")
    icon_url = models.URLField(blank=True , null=True , verbose_name="آدرس آیکون مهارت")
    color = models.CharField(blank=True , null=True , verbose_name="رنگ بدنه")

    def get_icon_url(self):
        if self.icon :
            return self.icon.url
        elif self.icon_url :
            return self.icon_url
        else:
            return "https://picsum.photos/200/200?blur"
        
    class Meta :
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"


    def __str__(self):
        return self.title


class resume(models.Model) :
    title = models.CharField(max_length=255 , blank=True , null=True , verbose_name="عنوان نمونه کار")
    description = models.TextField(blank=True , null=True , verbose_name="توضیحات نمونه کار")
    resume_url = models.URLField(blank=True , null=True , verbose_name="آدرس نمونه کار")
    resume_img = models.ImageField(upload_to="skills/resume" , blank=True , null=True , verbose_name="عکس نمونه کار")
    resume_img_url = models.URLField(blank=True , null=True , verbose_name="آدرس عکس نمونه کار")

    class Meta :
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه ها"

    def get_resume_img_url(self):
        if self.resume_img:
            return self.resume_img.url
        else:
            return self.resume_img_url
        
    def __str__(self):
        return self.title