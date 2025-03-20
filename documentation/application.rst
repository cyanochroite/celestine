Application
###########

.. toctree::
    :maxdepth: 2
    :caption: Contents:

- Demo_
- Translator_
- Viewer_


An application is any module or directory found in the ``celestine/application`` directory.
For example, your application could either be ``demo.py`` or ``demo/__init__.py``

This module must have at least one public ("no ``_`` prefix") function.

You must also have a ``Session`` class, which is used to define command line argumentns and application attributes.
For now its probably easiest to just copy an existing application.

Demo
****

Change screens with two whole buttons.

``celestine -a demo``

Translator
**********

``celestine -a translator``

This uses `Microsoft Azure`_ to translate text found in the ``language`` files into the official languages of the European Union.
There are `other languages`_ available, but managing 24 is already a lot!

+------+-------------+-----------+----------------------------------------------------+
| Flag | Long Flag   | Argument  | Information                                        |
+======+=============+===========+====================================================+
| -k   | --key       | KEY       | Your Translator service key from the Azure portal. |
+------+-------------+-----------+----------------------------------------------------+
| -r   | --region    | REGION    | The region where your resource was created.        |
+------+-------------+-----------+----------------------------------------------------+
| -u   | --url       | URL       | The location of the translation service.           |
+------+-------------+-----------+----------------------------------------------------+

.. _`Microsoft Azure`: https://learn.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=python
.. _`other languages`: https://learn.microsoft.com/en-us/azure/cognitive-services/translator/language-support

Viewer
******

``celestine -a viewer``

Secondary goals:
- Advanced tag searching. (Most websites have really lousy topic filters.)

What this is not:
- This is not a photo editor.
- This is not a photo downloader.
- This is not a mobile application.

View a very small amount of pictures at once. 

+------+-------------+-----------+-------------------------------+
| Flag | Long Flag   | Argument  | Information                   |
+======+=============+===========+===============================+
| -d   | --directory | DIRECTORY | A system path to a directory. |
+------+-------------+-----------+-------------------------------+

