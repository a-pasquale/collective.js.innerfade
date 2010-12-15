Overview
========

collective.js.innerfade installs the `jQuery innerfade plugin <http://medienfreunde.com/lab/innerfade/>`_. On top of that, it adds an additional view to ATFolder which will activate the jQuery plugin for Image and Link instances that were added to it.

Compatibility
-------------

* Software was created and tested on Plone 4

Status
------

Stable; almost in production :)

Usage
-----

Use buildout, or a similar method to install collective.collage.innerfade, (re)start your Plone instance and use the quick installer to install the product.

#. Create a Folder.
#. Add Image instances. For best results, add four Images in total.
#. Select the Innerfade view of the Folder you just created.
#. Now, if you want the Images to contain links, add Link instances to the Folder. When you use the exact same id of an Image in the Folder and suffix it with ``.link``, the Link will attach itself to that particular Image.

Development
-----------

Please report issues to `Wietze Helmantel (main developer) <helmantel@gw20e.com>`_

Sponsors
--------

Work on this product has been sponsored by Milieudefensie (http://www.milieudefensie.nl)
