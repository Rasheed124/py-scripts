# Stdlib imports

from math import sqrt
from os.path import abspath

# Core Django imports

from django.db import models
from django.utils.translation import ugettext*lazy as *

# Third-party app imports

from django_extensions.db.models import TimeStampedModel

# Imports from your apps

from splits.models import BananaSplit

----------------------------------------------PROPER STRUCTURED IMPORTS PATTERN-

1.Standard library imports.
2 Imports from core Django.
3 Imports from third-party apps including those unrelated to Django.
4 Imports from the apps that you created as part of your Django project. (You’ll read more about
apps in Chapter 4: Fundamentals of Django App Design.)

----------------------------------------------------explicit relative
imports is a good habit for any Python programmer to develop.

# Relative imports of the 'cones' package

from .models import WaffleCone
from .forms import WaffleConeForm

----------------------------------------------------------Other Python Naming Collisions

from django.db.models import CharField
from django.forms import CharField

<!-- Example 1.7: Using Aliases to Avoid Python Module Collisions -->

from django.db.models import CharField as ModelCharField
from django.forms import CharField as FormCharField

---------------------------------------------------------- The Optimal Django Environment Setup

- Django+PostgreSQL Rocks

PostgreSQL may take some work to get running locally on some operating systems, but we
find that it’s well worth the effort.

Use Pip and Virtualenv + virtualenvwrapper

We also highly recommend virtualenvwrapper for Mac OS X and Linux or
virtualenvwrapper-win for Windows.

Rasheed12345
Rasheed1245


---------------------------------------------------------------------------

Okay before we dive into using the postgress Db and the likes

I wants to understand some few things highlighted in this book am reading.

Base on folder structure explained, using that structured attached is the best apprach







You did not explicitly define a primary key, but Django automatically creates one.

With this configuration, it uses a BigAutoField.

----it uses a BigAutoField.



--------------------------------------------------------------------

Fundamentals of Django App
Design
---------------------------------------------------------------------

The Golden Rule of Django App Design

‘Write programs that do one
thing and do it well'