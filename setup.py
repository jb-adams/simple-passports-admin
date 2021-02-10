import setuptools

NAME = "simple-passports-admin"
VERSION = "0.1.0"
AUTHOR = "Jeremy Adams"
EMAIL = "jeremy.adams@ga4gh.org"

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

with open("README.md", "r") as fh:
    long_description = fh.read()
install_requires = [
    "click"
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description="Command line admin utility for the lightweight passports implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jb-adams/simple-passports-admin",
    package_data={'': ['web/*/*', 'schemas/*']},
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        simple-passports-admin=ga4gh.passports.cli.entrypoint:main
    ''',
    classifiers=(
    ),
)
