from setuptools import setup

setup(
	name='PassMaster-web',
	version='',
	packages=['', 'chat', 'chat.migrations', 'venv.Lib.site-packages.pytz', 'venv.Lib.site-packages.django',
	          'venv.Lib.site-packages.django.db', 'venv.Lib.site-packages.django.db.models',
	          'venv.Lib.site-packages.django.db.models.sql', 'venv.Lib.site-packages.django.db.models.fields',
	          'venv.Lib.site-packages.django.db.models.functions', 'venv.Lib.site-packages.django.db.backends',
	          'venv.Lib.site-packages.django.db.backends.base', 'venv.Lib.site-packages.django.db.backends.dummy',
	          'venv.Lib.site-packages.django.db.backends.mysql', 'venv.Lib.site-packages.django.db.backends.oracle',
	          'venv.Lib.site-packages.django.db.backends.sqlite3',
	          'venv.Lib.site-packages.django.db.backends.postgresql',
	          'venv.Lib.site-packages.django.db.backends.postgresql_psycopg2',
	          'venv.Lib.site-packages.django.db.migrations', 'venv.Lib.site-packages.django.db.migrations.operations',
	          'venv.Lib.site-packages.django.apps', 'venv.Lib.site-packages.django.conf',
	          'venv.Lib.site-packages.django.conf.urls', 'venv.Lib.site-packages.django.conf.locale',
	          'venv.Lib.site-packages.django.conf.locale.ar', 'venv.Lib.site-packages.django.conf.locale.az',
	          'venv.Lib.site-packages.django.conf.locale.bg', 'venv.Lib.site-packages.django.conf.locale.bn',
	          'venv.Lib.site-packages.django.conf.locale.bs', 'venv.Lib.site-packages.django.conf.locale.ca',
	          'venv.Lib.site-packages.django.conf.locale.cs', 'venv.Lib.site-packages.django.conf.locale.cy',
	          'venv.Lib.site-packages.django.conf.locale.da', 'venv.Lib.site-packages.django.conf.locale.de',
	          'venv.Lib.site-packages.django.conf.locale.el', 'venv.Lib.site-packages.django.conf.locale.en',
	          'venv.Lib.site-packages.django.conf.locale.eo', 'venv.Lib.site-packages.django.conf.locale.es',
	          'venv.Lib.site-packages.django.conf.locale.et', 'venv.Lib.site-packages.django.conf.locale.eu',
	          'venv.Lib.site-packages.django.conf.locale.fa', 'venv.Lib.site-packages.django.conf.locale.fi',
	          'venv.Lib.site-packages.django.conf.locale.fr', 'venv.Lib.site-packages.django.conf.locale.fy',
	          'venv.Lib.site-packages.django.conf.locale.ga', 'venv.Lib.site-packages.django.conf.locale.gd',
	          'venv.Lib.site-packages.django.conf.locale.gl', 'venv.Lib.site-packages.django.conf.locale.he',
	          'venv.Lib.site-packages.django.conf.locale.hi', 'venv.Lib.site-packages.django.conf.locale.hr',
	          'venv.Lib.site-packages.django.conf.locale.hu', 'venv.Lib.site-packages.django.conf.locale.id',
	          'venv.Lib.site-packages.django.conf.locale.is', 'venv.Lib.site-packages.django.conf.locale.it',
	          'venv.Lib.site-packages.django.conf.locale.ja', 'venv.Lib.site-packages.django.conf.locale.ka',
	          'venv.Lib.site-packages.django.conf.locale.km', 'venv.Lib.site-packages.django.conf.locale.kn',
	          'venv.Lib.site-packages.django.conf.locale.ko', 'venv.Lib.site-packages.django.conf.locale.lt',
	          'venv.Lib.site-packages.django.conf.locale.lv', 'venv.Lib.site-packages.django.conf.locale.mk',
	          'venv.Lib.site-packages.django.conf.locale.ml', 'venv.Lib.site-packages.django.conf.locale.mn',
	          'venv.Lib.site-packages.django.conf.locale.nb', 'venv.Lib.site-packages.django.conf.locale.nl',
	          'venv.Lib.site-packages.django.conf.locale.nn', 'venv.Lib.site-packages.django.conf.locale.pl',
	          'venv.Lib.site-packages.django.conf.locale.pt', 'venv.Lib.site-packages.django.conf.locale.ro',
	          'venv.Lib.site-packages.django.conf.locale.ru', 'venv.Lib.site-packages.django.conf.locale.sk',
	          'venv.Lib.site-packages.django.conf.locale.sl', 'venv.Lib.site-packages.django.conf.locale.sq',
	          'venv.Lib.site-packages.django.conf.locale.sr', 'venv.Lib.site-packages.django.conf.locale.sv',
	          'venv.Lib.site-packages.django.conf.locale.ta', 'venv.Lib.site-packages.django.conf.locale.te',
	          'venv.Lib.site-packages.django.conf.locale.th', 'venv.Lib.site-packages.django.conf.locale.tr',
	          'venv.Lib.site-packages.django.conf.locale.uk', 'venv.Lib.site-packages.django.conf.locale.vi',
	          'venv.Lib.site-packages.django.conf.locale.de_CH', 'venv.Lib.site-packages.django.conf.locale.en_AU',
	          'venv.Lib.site-packages.django.conf.locale.en_GB', 'venv.Lib.site-packages.django.conf.locale.es_AR',
	          'venv.Lib.site-packages.django.conf.locale.es_CO', 'venv.Lib.site-packages.django.conf.locale.es_MX',
	          'venv.Lib.site-packages.django.conf.locale.es_NI', 'venv.Lib.site-packages.django.conf.locale.es_PR',
	          'venv.Lib.site-packages.django.conf.locale.pt_BR', 'venv.Lib.site-packages.django.conf.locale.sr_Latn',
	          'venv.Lib.site-packages.django.conf.locale.zh_Hans', 'venv.Lib.site-packages.django.conf.locale.zh_Hant',
	          'venv.Lib.site-packages.django.core', 'venv.Lib.site-packages.django.core.mail',
	          'venv.Lib.site-packages.django.core.mail.backends', 'venv.Lib.site-packages.django.core.cache',
	          'venv.Lib.site-packages.django.core.cache.backends', 'venv.Lib.site-packages.django.core.files',
	          'venv.Lib.site-packages.django.core.checks', 'venv.Lib.site-packages.django.core.checks.security',
	          'venv.Lib.site-packages.django.core.checks.compatibility', 'venv.Lib.site-packages.django.core.servers',
	          'venv.Lib.site-packages.django.core.handlers', 'venv.Lib.site-packages.django.core.management',
	          'venv.Lib.site-packages.django.core.management.commands',
	          'venv.Lib.site-packages.django.core.serializers', 'venv.Lib.site-packages.django.http',
	          'venv.Lib.site-packages.django.test', 'venv.Lib.site-packages.django.urls',
	          'venv.Lib.site-packages.django.forms', 'venv.Lib.site-packages.django.forms.extras',
	          'venv.Lib.site-packages.django.utils', 'venv.Lib.site-packages.django.utils.translation',
	          'venv.Lib.site-packages.django.views', 'venv.Lib.site-packages.django.views.generic',
	          'venv.Lib.site-packages.django.views.decorators', 'venv.Lib.site-packages.django.contrib',
	          'venv.Lib.site-packages.django.contrib.gis', 'venv.Lib.site-packages.django.contrib.gis.db',
	          'venv.Lib.site-packages.django.contrib.gis.db.models',
	          'venv.Lib.site-packages.django.contrib.gis.db.models.sql',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends.base',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends.mysql',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends.oracle',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends.postgis',
	          'venv.Lib.site-packages.django.contrib.gis.db.backends.spatialite',
	          'venv.Lib.site-packages.django.contrib.gis.gdal', 'venv.Lib.site-packages.django.contrib.gis.gdal.raster',
	          'venv.Lib.site-packages.django.contrib.gis.gdal.prototypes',
	          'venv.Lib.site-packages.django.contrib.gis.geos',
	          'venv.Lib.site-packages.django.contrib.gis.geos.prototypes',
	          'venv.Lib.site-packages.django.contrib.gis.admin', 'venv.Lib.site-packages.django.contrib.gis.forms',
	          'venv.Lib.site-packages.django.contrib.gis.geoip', 'venv.Lib.site-packages.django.contrib.gis.utils',
	          'venv.Lib.site-packages.django.contrib.gis.geoip2', 'venv.Lib.site-packages.django.contrib.gis.geometry',
	          'venv.Lib.site-packages.django.contrib.gis.geometry.backend',
	          'venv.Lib.site-packages.django.contrib.gis.sitemaps',
	          'venv.Lib.site-packages.django.contrib.gis.management',
	          'venv.Lib.site-packages.django.contrib.gis.management.commands',
	          'venv.Lib.site-packages.django.contrib.gis.serializers', 'venv.Lib.site-packages.django.contrib.auth',
	          'venv.Lib.site-packages.django.contrib.auth.tests', 'venv.Lib.site-packages.django.contrib.auth.handlers',
	          'venv.Lib.site-packages.django.contrib.auth.management',
	          'venv.Lib.site-packages.django.contrib.auth.management.commands',
	          'venv.Lib.site-packages.django.contrib.auth.migrations', 'venv.Lib.site-packages.django.contrib.admin',
	          'venv.Lib.site-packages.django.contrib.admin.views',
	          'venv.Lib.site-packages.django.contrib.admin.migrations',
	          'venv.Lib.site-packages.django.contrib.admin.templatetags', 'venv.Lib.site-packages.django.contrib.sites',
	          'venv.Lib.site-packages.django.contrib.sites.migrations',
	          'venv.Lib.site-packages.django.contrib.humanize',
	          'venv.Lib.site-packages.django.contrib.humanize.templatetags',
	          'venv.Lib.site-packages.django.contrib.messages',
	          'venv.Lib.site-packages.django.contrib.messages.storage',
	          'venv.Lib.site-packages.django.contrib.postgres', 'venv.Lib.site-packages.django.contrib.postgres.forms',
	          'venv.Lib.site-packages.django.contrib.postgres.fields',
	          'venv.Lib.site-packages.django.contrib.postgres.aggregates',
	          'venv.Lib.site-packages.django.contrib.sessions',
	          'venv.Lib.site-packages.django.contrib.sessions.backends',
	          'venv.Lib.site-packages.django.contrib.sessions.management',
	          'venv.Lib.site-packages.django.contrib.sessions.management.commands',
	          'venv.Lib.site-packages.django.contrib.sessions.migrations',
	          'venv.Lib.site-packages.django.contrib.sitemaps',
	          'venv.Lib.site-packages.django.contrib.sitemaps.management',
	          'venv.Lib.site-packages.django.contrib.sitemaps.management.commands',
	          'venv.Lib.site-packages.django.contrib.admindocs', 'venv.Lib.site-packages.django.contrib.flatpages',
	          'venv.Lib.site-packages.django.contrib.flatpages.migrations',
	          'venv.Lib.site-packages.django.contrib.flatpages.templatetags',
	          'venv.Lib.site-packages.django.contrib.redirects',
	          'venv.Lib.site-packages.django.contrib.redirects.migrations',
	          'venv.Lib.site-packages.django.contrib.staticfiles',
	          'venv.Lib.site-packages.django.contrib.staticfiles.management',
	          'venv.Lib.site-packages.django.contrib.staticfiles.management.commands',
	          'venv.Lib.site-packages.django.contrib.staticfiles.templatetags',
	          'venv.Lib.site-packages.django.contrib.syndication', 'venv.Lib.site-packages.django.contrib.contenttypes',
	          'venv.Lib.site-packages.django.contrib.contenttypes.management',
	          'venv.Lib.site-packages.django.contrib.contenttypes.management.commands',
	          'venv.Lib.site-packages.django.contrib.contenttypes.migrations', 'venv.Lib.site-packages.django.dispatch',
	          'venv.Lib.site-packages.django.template', 'venv.Lib.site-packages.django.template.loaders',
	          'venv.Lib.site-packages.django.template.backends', 'venv.Lib.site-packages.django.middleware',
	          'venv.Lib.site-packages.django.templatetags', 'venv.Lib.site-packages.rest_framework',
	          'venv.Lib.site-packages.rest_framework.utils', 'venv.Lib.site-packages.rest_framework.schemas',
	          'venv.Lib.site-packages.rest_framework.authtoken',
	          'venv.Lib.site-packages.rest_framework.authtoken.management',
	          'venv.Lib.site-packages.rest_framework.authtoken.management.commands',
	          'venv.Lib.site-packages.rest_framework.authtoken.migrations',
	          'venv.Lib.site-packages.rest_framework.templatetags', 'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.req',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.vcs',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.utils',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.compat',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.models',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib._backport',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.colorama',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib._trie',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.filters',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.lockfile',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.progress',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.chardet',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.util',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.contrib',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.packaging',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.webencodings',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.pkg_resources',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.commands',
	          'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.operations', 'server', 'server.migrations',
	          'server.templatetags', 'accounts', 'accounts.migrations', 'PassMaster'],
	url='',
	license='',
	author='Jared',
	author_email='',
	description=''
)
