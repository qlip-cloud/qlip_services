from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in qlip_services/__init__.py
from qlip_services import __version__ as version

setup(
	name='qlip_services',
	version=version,
	description='qlip Services',
	author='Mentum GROUP',
	author_email='aryrosa.fuentes@mentum.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
