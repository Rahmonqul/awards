from django.db import models

# Model for Awards
class Award(models.Model):
    name = models.CharField(max_length=100, verbose_name="Award Name")
    bio = models.TextField(blank=True, null=True, verbose_name="Award Description")
    image = models.ImageField(upload_to='awards/', blank=True, null=True, verbose_name="Award Image")
    count = models.IntegerField(verbose_name="Award Count")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"
        ordering = ['name']


# Model for Users
class User(models.Model):
    fio = models.CharField(max_length=200, verbose_name="Full Name")
    position = models.CharField(max_length=100, verbose_name="Position")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    image = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name="User Image")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['fio']


# Model for Year Order
class PresidentDecree(models.Model):
    number_president_decree=models.IntegerField(verbose_name='Number president decree')
    year = models.DateField(verbose_name="Year date")


    @property
    def formatted_date(self):
        return self.year.strftime("%Y-%m-%d")  # Formatni kerakli ko‘rinishga moslang

    def __str__(self):
        return f'{self.formatted_date} -decree of {self.number_president_decree}'

    class Meta:
        verbose_name = "Presiden Decree"
        verbose_name_plural = "President Decrees"
        ordering = ['year']
#
# # Model for Award Orders (Orders of awarding)
class AwardOrder(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name="award_orders", verbose_name="Award")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="award_orders", verbose_name="Recipient")
    choice_type=(
        ("Unvon", "Unvon"),
        ("Mukofot", "Mukofot"),
        ("Orden", "Orden"),
        ("Medal", "Medal")
    )
    order_type = models.CharField(max_length=100, verbose_name="Order Type", choices=choice_type)
    number_president_decree = models.ForeignKey(PresidentDecree, on_delete=models.CASCADE, related_name="award_orders", verbose_name="Number decree")

    def __str__(self):
        return f"{self.award.name} - {self.user.fio} - {self.number_president_decree.year}-president decree of {self.number_president_decree.number_president_decree}-"

    class Meta:
        verbose_name = "Award Order"
        verbose_name_plural = "Award Orders"
        ordering = ['number_president_decree', 'award']


