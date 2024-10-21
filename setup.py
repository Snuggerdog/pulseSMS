from setuptools import setup
import pulsesmsreboot
setup_requires = ['setuptools']
try:
    setup(
        name=pulsesmsreboot.__appname__.lower(),
        version=pulsesmsreboot.__version__,
        author=pulsesmsreboot.__author__,
        author_email=pulsesmsreboot.__email__,
        description=pulsesmsreboot.__comment__,
        url=pulsesmsreboot.__website__,
        license='GPLv3+',
        packages=['pulsesmsreboot',
                  'pulsesmsreboot.controllers',
                  'pulsesmsreboot.controllers.main_window_components',
                  'pulsesmsreboot.controllers.settings_pages',
                  'pulsesmsreboot.engine',
                  'pulsesmsreboot.services',
                  'pulsesmsreboot.theme',
                  'pulsesmsreboot.theme.style_components',
                  'pulsesmsreboot.view',
                  'pulsesmsreboot.model'],
        include_package_data=True,
        package_data={'pulsesmsreboot': ['assets/icons/app/*/*.svg',
                                 'assets/icons/app/*/*.png',
                                 'assets/icons/titlebar_buttons/*/*/*.svg',
                                 'assets/icons/banners/*.svg',
                                 'assets/icons/banners/*.png',
                                 'assets/icons/tray/*.svg',
                                 'po/*/LC_MESSAGES/*.mo']},
        setup_requires=setup_requires,
        entry_points={'gui_scripts': ['pulsesmsreboot = pulsesmsreboot.__main__:main']},
        keywords='pulsesmsreboot pulsesms client web app',
        classifiers=[
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Office/Business',
            'Programming Language :: Python :: 3 :: Only'
        ]
    )
except Exception as e:
    print(e)
