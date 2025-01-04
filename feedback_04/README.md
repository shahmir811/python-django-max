# Feedback Project

Learned about the following topics in this project:

- Forms
- GET and POST requests
- CSRF protection in django template forms
- Handling form submission and extracting data
- Django form classes for form validations
- Simple `forms` and `model forms` and when to use which, as explain below
- Saving data with both simple forms and model forms
- Replace `function-based` views with `class-based` views
- Using the `TemplateView`, `ListView`, and `DetailView` in the class-based views
- Using `FormView`, and `CreateView` in the class-based views to get/post form data
- How to upload images using `FileField` and `ImageField`
- How to use models for file storage
- How to serve the uploaded files
- Sessions, storing, and retrieving session data

## Below explanation when to use Modelform or simple form in django application

In Django, the choice between using `forms.ModelForm` and `forms.Form` depends on whether your form is directly tied to a database model or not. Here's when to use each:

### Use `forms.ModelForm`

- **When Your Form is Tied to a Model:** Use `ModelForm` when the form's fields correspond to fields in a database model. This automatically handles creating and updating model instances.
- **Automated Field Management:** Fields in the form are automatically generated based on the model's fields, saving you the effort of defining them manually.
- **Validation:** Built-in validation is automatically applied based on the model field types.
- **Example Use Case:** Creating or editing a model instance (e.g., user registration form where data directly maps to a `User` model).

```
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2', 'field3']  # Specify fields to include

```

- **Pros:**
  - Faster and more concise for model-related forms.
  - Automatically integrates with the model's validation rules.
  - Easily saves the form data to the database with `form.save()`.

### Use `forms.Form`

- **When Your Form is Independent of a Model:** Use `Form` for custom forms that do not correspond directly to a database model.
- **Flexibility:** You can define fields that are completely independent of any model, giving you greater control.
- **Example Use Case:** Search forms, contact forms, or any scenario where the form data is not meant to be stored in a database.

```
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

```

- **Pros:**
  - Fully customizable for non-database-related forms.
  - Allows for non-standard field combinations or validations.

### Summary

| Criteria                | `ModelForm`                          | `Form`                               |
| ----------------------- | ------------------------------------ | ------------------------------------ |
| **Database Connection** | Tied to a model                      | Independent of a model               |
| **Field Definition**    | Automatic based on the model         | Manually defined                     |
| **Use Case**            | CRUD operations for models           | Custom forms (e.g., search, contact) |
| **Convenience**         | Automatically integrates with models | Greater flexibility                  |

### Decision

- Use **`ModelForm`** when you want to save time and your form's purpose aligns with creating or updating a model instance.
- Use **`Form`** when you need complete independence from your models or require fields that do not map to model fields.
