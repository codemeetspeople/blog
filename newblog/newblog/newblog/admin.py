from django.contrib import admin
from newblog import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

