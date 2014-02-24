from setuptools import setup

setup(
    name='django-foundation-statics',
    version='5.1.1',
    url='https://github.com/benbacardi/django-foundation-statics',
    description='Zurb Foundation (http://foundation.zurb.com) static files packaged in a django app to speed up new applications and deployment.',
    author='Ben Cardy',
    author_email='benbacardi@gmail.com',
    license='MIT',
    keywords='django zurb foundation staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['foundation', 'foundation_scss'],
    package_data={'foundation': ['static/js/*.js', 'static/js/foundation/*.js', 'static/js/vendor/*.js', 'static/css/*.css',], 'foundation_scss': ['static/js/*.js', 'static/js/foundation/*.js', 'static/js/vendor/*.js', 'static/scss/*.scss', 'static/scss/foundation/*.scss', 'static/scss/foundation/components/*.scss'],},
    include_package_data=True,
)
