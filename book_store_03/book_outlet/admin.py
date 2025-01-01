from django.contrib import admin

from .models import Book, Author, Address, Country

class AddressAdmin(admin.ModelAdmin):
  list_display = ('street', 'postal_code', 'city')
  search_fields = ('street', 'postal_code', 'city')

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'address')
  search_fields = ('first_name', 'last_name', 'address__street', 'address__postal_code', 'address__city')

class BookAdmin(admin.ModelAdmin):
  # readonly_fields = ('slug',)
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'author', 'rating', 'is_bestselling', 'countries_display')
  list_filter = ('author', 'rating')
  search_fields = ('title', 'author__first_name', 'author__last_name')

  def countries_display(self, obj):
      return ", ".join(country.code for country in obj.published_countries.all())
  countries_display.short_description = "Countries"  

class CountryAdmin(admin.ModelAdmin):
  list_display = ('name', 'code', 'books_display',)
  search_fields = ('name', 'code',)

  def books_display(self, obj):
      return ", ".join(book.title for book in obj.books.all())
  books_display.short_description = "Books"

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)