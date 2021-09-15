from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Contact



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
    llist_display_links = ('user',)
    list_filter = ('user', 'city',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Contact, ContactAdmin)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass


# @admin.register(ProductInfo)
# class ProductInfoAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Parameter)
# class ParameterAdmin(admin.ModelAdmin):
#     pass


# @admin.register(ProductParameter)
# class ProductParameterAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     pass


# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     pass



