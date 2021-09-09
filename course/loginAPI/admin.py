from django.contrib import admin
from .models import Users, Book, Brands, Comment,Token
import jdatetime
import locale
from django.utils.translation import gettext_lazy as _


class UserAdmin(admin.ModelAdmin):
    # fields = ('id', 'user_name', 'user_photo')
    list_display = ('id', 'user_name', 'user_photo')


@admin.action(description='تایید کردن پست')
def make_confirmation(modeladmin, request, queryset):
    queryset.update(cofirm='T')


class BookListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('فیلتر نام خانوادگی')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('j', _('jouya')),
            ('h', _('haghani')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'j':
            return queryset.filter(author_fk__user_lastname="jouya")
        if self.value() == 'h':
            return None


class bookAdmin(admin.ModelAdmin):
    fields = (('name', 'photo'), 'manyfield', 'pages', ("cofirm"), "author_fk", "brand_one")
    list_display = ('image_tag', 'id', 'name', 'price', "cofirm", "custom", "brand_one")
    search_fields = ("name", "price")
    ordering = ("-id",)
    list_per_page = 10
    list_filter = ("author_fk",BookListFilter)
    actions = [make_confirmation]

    def custom(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.datetime).strftime("%a, %d %b %Y")

    custom.short_description = 'customfield'


admin.site.register(Users, UserAdmin)
admin.site.register(Book, bookAdmin)
admin.site.register(Brands)
admin.site.register(Comment)
admin.site.register(Token)
