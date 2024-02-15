from django.db.models import Model, CharField, TextField, ImageField, EmailField,DateTimeField




class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(Model):
    image = ImageField(upload_to='user_image/', default='user_image_default/user.png')
    username = CharField(max_length=255)
    firstname = CharField(max_length=255)
    lastname = CharField(max_length=255)
    email = EmailField()
    website = CharField(max_length=255)
    description = TextField()

    def __str__(self):
        return self.username


class Email(CreatedBaseModel):
    email = EmailField(max_length=255, unique=True)