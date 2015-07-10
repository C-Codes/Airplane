from setuptools import setup

APP = ['airplane/airplanebar.py']
DATA_FILES = [
    'Resources/airplane-mode-on.png',
    'Resources/airplane-mode-off.png',
    'Resources/blueutil'
    ]
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'Resources/airplane-logo-bw.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
 }
VERSION='0.1.1'

setup(
    name='airplane',
    version=VERSION,
    description='A little statusbar for to allow switching into an airplane mode under OS X written in Python.',
    license='MIT',
    author='Christoph Russ',
    author_email='chruss@gmx.de',
    url='https://github.com/C-Codes/Airplane',
    download_url='https://github.com/C-Codes/Airplane/tarball/v'+VERSION,
    packages=['airplane'],
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps', 'appdirs', 'dicttoxml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
 )