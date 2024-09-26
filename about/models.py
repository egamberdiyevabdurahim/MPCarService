from django.db import models


class UsefulModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarouselModel(UsefulModel, models.Model):
    background_image = models.ImageField(upload_to='carousel')
    car_image = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousels"


class ServicesAboutModel(UsefulModel, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Services About"
        verbose_name_plural = "Services About"


class AboutModel(UsefulModel, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='about/')
    experience = models.IntegerField(default=0)
    full_experience = models.IntegerField(default=0)
    expert_technicians = models.IntegerField(default=0)
    satisfied_clients = models.IntegerField(default=0)
    complete_projects = models.IntegerField(default=0)
    services = models.ManyToManyField(ServicesAboutModel, related_name="about")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class TickedModel(UsefulModel, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


class ServicesModel(UsefulModel, models.Model):
    main_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='services/')

    def __str__(self):
        return f"{self.main_name}/{self.title}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class SocialsModel(UsefulModel, models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"


class InfoModel(UsefulModel, models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    brand_name = models.CharField(max_length=255)
    socials = models.ManyToManyField(SocialsModel, related_name="info")

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Info"


class ExpertTechniciansModel(UsefulModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='expert_technicians/')
    is_pinned = models.BooleanField(default=False)
    socials = models.ManyToManyField(SocialsModel, related_name="expert_technicians")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Expert Technician"
        verbose_name_plural = "Expert Technicians"
