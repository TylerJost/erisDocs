Mass General Brigham Computing Guide
=============================================

This is documentation for getting started with computing at Mass General Brigham. It is based on the
`Texas Advanced Computing Center <https://docs.tacc.utexas.edu/hpc/lonestar6/>`_ 
computing documentation. It is part self-written, part collection of documents from the associated `knowledge base <https://rc.partners.org/kb>`_. 

.. note::

   This guide is written assuming you are familiar with using a UNIX based command line system. It tries to not assume that
   you understand the way that ERISXdl is structured, the specific software stack it uses, or that you have any background
   in the niche environment of high-performance computing. 


There are several key differences between this documentation and the "official" knowledge base:

- These documents focus on ERISXdl, the GPU computing cluster.
- These documents are (arguably) more up to date. They will only use :code:`SLURM`, etc.
- These documents are meant to guide users succesively, starting with information about the available partitions, modules, and development.
- These documents are meant to be displayed in a coherent manner, meaning that a user can see where they are in each section (notably this is missing from the knowledge base).



.. warning::

   This project is under active development. Good documentation is rare/non-existent. If you have questions please email me at tjost@bwh.harvard.edu.
   
   Additionally, this project is open-source and hosted on GitHub at `www.github.com/tylerjost/erisDocs <https://www.github.com/tylerjost/erisDocs/>`_.  

.. toctree::
   :maxdepth: 7
   :titlesonly:
   :hidden:


   knowledgeBaseLinks
   nirmalLabStart


.. usage
.. --------
.. .. include:: usage.rst

Getting Started
---------------
.. include:: nirmalLabStart.md
   :parser: myst_parser.sphinx_

Developing and Running Code on ERISXdl
--------------------------------------
.. include:: development.md
   :parser: myst_parser.sphinx_

Important Links
---------------
.. include:: knowledgeBaseLinks.md
   :parser: myst_parser.sphinx_


.. answers
.. ---------
.. .. include:: answers.md
..    :parser: myst_parser.sphinx_

.. Section 2
.. ---------

.. .. include:: code.rst

.. Section 3
.. ---------

.. .. include:: answers.md

