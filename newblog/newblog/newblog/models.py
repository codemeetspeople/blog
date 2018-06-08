from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True  # If no new field is added.


class Category(models.Model):
    title = models.CharField(
        max_length=50,
        null=False
        # verbose_name=_('Title of category')
    )
    image = models.ImageField(
        null=True
    )
    description = models.CharField(
        max_length=200,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=False
    )
    user = models.ForeignKey(
        to='CustomUser',
        null=False,
        on_delete='DO_NOTHING',
    )

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = _('Категория')
    #     verbose_name_plural = _('Категории')
    #     ordering = ('id',)


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False
        # verbose_name=_('Title of article')
    )
    description = models.CharField(
        max_length=200,
        null=False
    )
    content = models.TextField(
        null=False
    )
    image = models.ImageField(
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=False
    )
    # ?????
    publication_date = models.DateField(
        auto_now_add=True,
        null=False
    )
    # ?????????
    visible = models.BooleanField()
    category = models.ForeignKey(
        to='Category',
        null=False,
        on_delete='DO_NOTHING',
    )
    user = models.ForeignKey(
        to='CustomUser',
        null=False,
        on_delete='DO_NOTHING',
    )
    tags = models.ManyToManyField(
        to='Tag',
        through='ArticleTag',
        through_fields=('article', 'tag')
    )

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = _('Статья')
    #     verbose_name_plural = _('Статьи')


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        null=False
        # verbose_name=_('Title of tag')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=False
    )


class ArticleTag(models.Model):
    article = models.ForeignKey(
        to='Article',
        null=False,
        on_delete='DO_NOTHING'
    )
    tag = models.ForeignKey(
        to='Tag',
        null=False,
        on_delete='DO_NOTHING'
    )


class Comment(models.Model):
    content = models.TextField(
        null=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    article = models.ForeignKey(
        to='Article',
        null=False,
        on_delete='DO_NOTHING',
    )
    user = models.ForeignKey(
        to='CustomUser',
        null=False,
        on_delete='DO_NOTHING',
    )
