# Stdlib imports
from math import sqrt
from os.path import abspath

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

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


