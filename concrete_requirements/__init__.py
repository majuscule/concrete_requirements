def concrete_requirements():
    with open('requirements.txt', 'r') as f:
        return [
            match.group(1) for match in
            [re.search('^(?!-)([\w\.=-]+)', req) for req in f]
            if match
        ]


def _read(*names, **kwargs):
    global io, os
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    global read, re
    version_file = _read(*file_paths)
    version_match = re.search(r'^__version__ = ['\']([^'\']*)['\']',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')
