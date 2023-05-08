---
title: 'TIL setting up database constraints with sqlalchemy'
date: 2023-05-08
permalink: /posts/2023/05/til-setting-up-database-constraints-with-sqlalchemy/
tags:
  - til
  - sqlalchemy
  - python
---

Long time wihtout a [TIL](https://luisnatera.com/tag#til). Today I learn about how to set up constraints between two fields in a database with [sqlalchemy](https://www.sqlalchemy.org/).

## The task

We had a table in the database, that for one column that stores the name of a post, the name has to be unique, however, it has to be unique within the user, thus multiple users can have a post with the same name.

## The solution

To solve it is needed to have a unique constraint on the name of the project, for example:

```python
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String, nullable=False, unique=True)
```

However in the previous code, the constraint only applies to the name of the post, but not to the combiantion of the `name` and the `user_id`. To make the constraint to work we can modify the class as follows:

```python
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String, nullable=False, unique=True)
    __table_args__ = (UniqueConstraint('name', 'user_id', name='_name_user_uc'),)
```

Now, by setting the `__table_args__` it is possible to set the Unique Constraint with the combination of `name` and `user_id` in the database.

## More resources

- [sqlalchemy documentation on Constraints and Indexes](https://docs.sqlalchemy.org/en/20/core/constraints.html#table-args)
- [sqlalchemy documentation on Unique Constraint](https://docs.sqlalchemy.org/en/20/core/constraints.html#sqlalchemy.schema.UniqueConstraint)
