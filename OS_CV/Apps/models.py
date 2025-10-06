from django.db import models

class webApp():
    name = models.CharField(max_length=100 , verbose_name="نام اپلیکیشن")
    icon = models.ImageField(upload_to='app_icons/', verbose_name="آیکون اپلیکیشن")
    icon_url = models.URLField(blank=True , null=True , verbose_name="آدرس آیکون اپلیکیشن")
    color = models.CharField(max_length=7 , verbose_name="رنگ اپلیکیشن")
    html_content = models.TextField(blank=True , null=True , verbose_name="محتوای HTML اپلیکیشن")
    css_content = models.TextField(blank=True , null=True , verbose_name="محتوای CSS اپلیکیشن")
    js_content = models.TextField(blank=True , null=True , verbose_name="محتوای JS اپلیکیشن")
    description = models.TextField(blank=True , null=True , verbose_name="توضیحات اپلیکیشن")
    is_active = models.BooleanField(default=True , verbose_name="فعال/غیرفعال")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="تاریخ بروزرسانی")
    def __str__(self):
        return self.name
    
    def get_icon_url(self):
        if self.icon_url:
            return self.icon_url
        elif self.icon:
            return self.icon.url
    class Meta():
        verbose_name = "اپلیکیشن وب"
        verbose_name_plural = "اپلیکیشن‌های وب"
        ordering = ['-created_at']