---
title: 'TIL Writing Django migrations'
date: 2022-12-14
permalink: /posts/2022/12/writing-django-migrations/
tags:
  - til
  - django
  - backend
---

[Today I learned](https://luisnatera.com/tag#til) about writing Django migrations to roll back some changes introduced in a previous migration. While working on connecting a form to the back end, I wrote a test to make sure that the view I was working on was working as it should. As with every good test, this one led us to discover a bug such that the tests were failing, but when fixing the code in the Django view to pass the test, the application got broken. The issue was in the data already in the database, which was introduced in a previous migration while populating the database.

One possible solution was to go into the Django admin panel and fix the data point, and also modify the original migration that was causing the issue. The problem with this approach was that we would need to go into the staging database and the production database to also change the data there. This approach might work, but it is not the best, as it involves modifying an already applied migration and requires us to go in manually to fix the issue. The preferred approach is to write a new migration to alter the data, and then have the migration applied.

The new migration looks like this:

```python
from django.db import migrations


def forwards_func(apps, schema_editor):
    User = apps.get_model("myapp", "User")

    for user in User.objects.filter(hair_color="brown", gender="FEMALE"):
        user.gender = "Female"
        user.save()


def reverse_func(apps, schema_editor):
    """Do nothing."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_some_other_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

```

What the migration is doing is applying a forward function that does as follows: 

1. Gets the `User` model from `myapp`.
2. Filter the objects in `User` by their `hair_color="brown"` and by `gender="FEMALE")`.
2. Iterates over the `user` and changes the gender from `FEMALE` to `Female`
3. Saves the `user` with the recent change.

After creating this migration, we were able to have the test pass and also fix the view. It was a good learning experience tracking the bug, thinking of possible solutions, and building a solution that can be applied to all the environments we are using at the moment.
