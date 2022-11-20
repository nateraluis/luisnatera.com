---
title: 'TIL Connecting html forms to Django forms'
date: 2022-11-17
permalink: /posts/2022/11/til-connecting-html-forms-to-django-forms/
tags:
  - til
  - django
  - html
---

I am starting to write TIL -Today I Learned- posts following Simon Willson's [What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/). Here is the first one.

Today at work I was having issues connecting an html template that has a form on it with the Python view that was processing the form. I asked [Jochen](https://wersdoerfer.de/blogs/ephes_blog/) about it and he pointed me that I was missing the `name` attribute in the html form, thus when getting the `form` from the request and validating it it was not valid.

A simple working example for this would be the following: lets take the example from [Django documentation](https://docs.djangoproject.com/en/4.1/topics/forms/), the template we want to connect is as follows:

```html
<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>
```

And the Django form as:

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

The html form has, in the `input` tag, the `name` attribute specified. My mistake was that I was not specifying it, thus when in the view I was retrieving and validating the form it was not being a valid form because the input was not being assigned to the correct field in the form.

The view for this form is:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # the form was not being populated as I was missing
        # the name attribute
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
		        # Of course my form was not valid
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
```

After adding the `name` attribute I was able to start processing my form and keep connecting all the different inputs needed. It was a good learning.