# Book Store

Learned about:

- Database models
- `get_absolute_url` method in the models
- slug fields, and storing it at the time of creation
- Adding secondary index in the slug field
- Aggregations sql methods like count, average, order by etc
- How to use django admin panel
- How to create super user for admin
- How to show models in the admin panel

Learned the following different topics focusing on CRUD operations on the database:

#### Opening the python shell

Following command is used to open the python shell:

```
python3 manage.py shell
```

#### Inserting records to the DB:

```
from book_outlet.models import Book

harry_potter = Book(title=“Harry Potter 1 - The Philosopher’s Stone”, rating=5)
harry_potter.save()

lord_of_the_rings = Book(title=“Lord of the rings”, rating=4)
lord_of_the_rings.save()
```

#### Fetching all records from the DB:

```
from book_outlet.models import Book

Book.objects.all()
```

#### Updating records from the DB: [Bulk Update](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#bulk-update)

```
from book_outlet.models import Book

harry_potter = Book.objects.all()[0]
harry_potter.author = “J.K Rowling”
harry_potter.is_bestselling = True
harry_potter.save()

lotr = Book.objects.all()[1]
lotr.author = "J.R.R. Tolkien"
lotr.is_bestselling = True
lotr.save()
```

#### Deleting records from the DB: [Bulk delete](https://docs.djangoproject.com/en/5.1/topics/db/queries/#deleting-objects)

```
from book_outlet.models import Book

harry_potter = Book.objects.all()[0]
harry_potter.delete()
```

#### Creating records from the DB: [Bulk create](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#bulk-create)

Using the create method instead of save method for inserting records in the DB:

```
from book_outlet.models import Book

Book.objects.create(title="Python for Beginners", rating="4", author="John Smith", is_bestselling=True);

```

#### Querying and filtering data: [Reference](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#field-lookups)

```
from book_outlet.models import Book

Book.objects.get(id=1) # Returns a single record
Book.objects.get(title="Python for Beginners") # Returns a single record

Book.objects.filter(is_bestselling=True) # Returns a list of multiple records
Book.objects.filter(is_bestselling=False, rating=5)  # Returns a list of multiple records
Book.objects.filter(rating__lt=4) # Return all the books whose rating is lower than 4
Book.objects.filter(rating__lte=4) # Return all the books whose rating is lower than equal to 4
Book.objects.filter(rating__lte=4, title__contains=“Story”) # Title is case sensitive
Book.objects.filter(rating__lte=4, title__icontains=“Story”) # Title is case-insensitive
```

#### Using `or` `and` in the query:

```
from django.db.models import Q

# Bring all the records where the rating is less than equal to 3 or is_bestselling = True
Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True))

# Bring all the records where the rating is less than equal to 3 or is_bestselling = True and the author name contains case-insensitive “rowling”
Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True), Q(author__icontains=“rowling”))

# We can remove Q for the AND part of the query, but remember
# if you use the AND query without the Q keyword, then it must be placed at the end,
# not at the start, else it will throw an error
Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True), author__icontains=“rowling”)
```

#### one-to-many relationship:

Inserting records to the DB using one-to-many relationships:

```
from book_outlet.models import Book, Author

jk_rowling = Author(first_name="J.K.", last_name="Rowling")
jk_rowling.save()

hp1 = Book(title="Harry Potter 1 - The Philosopher's Stone", rating=5, is_bestselling=True, author=jk_rowling)
hp1.save()
```

To query relationship data, we can use the following queries:

```
from book_outlet.models import Book, Author

harry_potter = Book.objects.get(title__icontains="harry")
harry_potter.author.first_name
harry_potter.author.last_name
```

#### Cross model queries:

1. Get all the books written by an author whose last_name is “Rowling”

```
from book_outlet.models import Book, Author

rowling_books = Book.objects.filter(author__last_name="Rowling")
rowling_books = Book.objects.filter(author__last_name__icontains=“rowling") # icontains is a modifier
```

2. Get all the books written by rowling:

```
jkr = Author.objects.get(first_name=“J.K.”)
jkr.books.all() # books is the related_model name written in the Books class in models.py
jkr.books.get(title__icontains=“philosopher”) # Returns single record
jkr.books.filter(ratings__gte=4) # Returns an array of records
```

#### One-to-one relationship:

Inserting records to the DB using one-to-one relationships:

```
from book_outlet.models import Book, Author, Address

address1 = Address(street="Street # 07", postal_code="54000", city="Lahore")
address1.save()

address2 = Address(street="101 Bunting Lane", postal_code="65343", city="Miami")
address2.save()

jkr1 = Author.objects.get(first_name="J.K.")
jkr1.address = address1
jkr1.save()

jkr1.address.street # returns ‘Street # 07’

jkr_address = Address.objects.all()[0].author
jkr_address # Returns <Author: J.K. Rowling>
jkr_address.first_name # Returns J.K.
```

#### many-to-many relationship:

Inserting records to the DB using many-to-many relationships:

```
from book_outlet.models import Book, Author, Address, Country

hp = Book.objects.get(title__icontains="philosopher")

germany = Country(name="Germany", code="DE")
germany.save()

hp.published_countries.add(germany)
hp.published_countries.all()
hp.published_countries.get(code=“DE”)
hp.published_countries.filter(code=“DE”)
```
