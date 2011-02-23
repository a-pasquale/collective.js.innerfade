Overview
========

collective.js.innerfade installs the `jQuery innerfade plugin <http://medienfreunde.com/lab/innerfade/>`_. On top of that, it adds an additional view to ATFolder which will activate the jQuery plugin for Image and Link instances that were added to it.

Compatibility
-------------

Software was created and tested on Plone 4.

Status
------

Stable; almost used in a production environment :)

Usage
-----

Use buildout, or a similar method to install collective.collage.innerfade, (re)start your Plone instance and use the quick installer to install the product.

#. Create a Folder.
#. Add Image instances. For best results, add four Images in total and use an aspect ratio of 16:9 
#. Select the Innerfade view of the Folder you just created.
#. Now, if you want the Images to contain links, add Link instances to the Folder. When you use the exact same id of an Image in the Folder and suffix it with ``.link``, the Link will attach itself to that particular Image, e.g.::

    Folder
        Image image-1
        Link image-1.link
        Image image-2
        Link image-2.link
        Image image-3
        Link image-3.link
        Image image-4
        Link image-4.link

Screenshot
----------

.. image:: http://plone.org/products/collective.js.innerfade/screenshot

Development
-----------

Created and maintained by Goldmund, Wyldebeast & Wunderliebe (http://www.gw20e.com).

Issues
------

Please report issues to `Wietze Helmantel (main developer) <helmantel@gw20e.com>`_

TODO
----

* Unit testing
* Similar view for Topic content types
* Configurable jQuery Innerfade parameters (maybe using a configlet)

Sponsors
--------

Work on this product was sponsored by Milieudefensie (http://www.milieudefensie.nl).
