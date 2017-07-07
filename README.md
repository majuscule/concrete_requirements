# concrete-requirements

Python package package version sourcing is... complicated. Instead of copying the [single-sourcing reference implementations](https://packaging.python.org/guides/single-sourcing-package-version/), allow a single package to handle the various incantations.

Python dependency management is... unclear. Support abstract/concrete dependency groups through your package metadata and enjoy reduced-worry deployment of application code.


### Usage:


MANIFEST.ini:
```
include requirements.txt
```

setup.py:
```python

#!/usr/bin/env python

from setuptools import setup, find_packages
from concrete_requirements import concrete_requirements


setup(
    name='myapp',
    use_scm_version=find_version(),
    description='myapp with concrete production requirements',
    url='https://github.com/majuscule',
    author='Dylan Lloyd',
    author_email='dylan@disinclined.org',
    packages=find_packages(),
    install_requires=[
        'mydependency~=1.0.0'
    ],
    extras_require={
        'production': concrete_requirements()
    },
)
```

### Recommended workflow:

[pip-tools](https://github.com/jazzband/pip-tools)
