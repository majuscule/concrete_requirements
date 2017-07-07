import os
import io
import re
import inspect


def concrete_requirements(source='requirements.txt'):
    with open(source, 'r') as f:
        return [
            match.group(1) for match in
            [re.search('^(?!-)([\w\.=-]+)', req) for req in f]
            if match
        ]


def _read(*names, **kwargs):
    global io, os
    frame = inspect.stack()[2]
    module = inspect.getmodule(frame[0])
    with io.open(
        os.path.join(os.path.dirname(module.__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    # Explicitly global references are required for pip-tools,
    # which requires distutils run_setup parsing.
    global read, re
    version_file = _read(*file_paths)
    version_match = re.search(r"^__version__ = ['\']([^'\']*)['\']",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')
