ERISXdl - Nirmal Lab Documentation
=============================================

This is documentation for getting started with computing at Mass General Brigham. It is based on the
`Texas Advanced Computing Center <https://docs.tacc.utexas.edu/hpc/lonestar6/>`_ computing documentation (hook 'em horns). It is part self-written, part collection of documents from the associated `knowledge base <https://rc.partners.org/kb>`_. 

These documents are meant to guide you on the ERISXdl system from getting an account, to submitting a job, to effectively writing code. ERIS stands for enterprise research infrastructure services, and Xdl stands for extreme deep learning. Eris is also the Greek goddess of strife and discord, but hopefully this compiled documentation will eliminate a bit of discord in your own life.

.. note::

   This guide is written assuming you are familiar with using a UNIX based command line system. It tries to not assume that
   you understand the way that ERISXdl is structured, the specific software stack it uses, or that you have any background
   in the niche environment of high-performance computing. 

These documents:

- Focus on ERISXdl, the GPU computing cluster.
- Aim to be more up to date. They will only use :code:`SLURM`, etc.
- Guide users succesively, starting with information about the available partitions, modules, and development.
- Are displayed on one page such that a user can navigate forwards and backwards through without refreshing a new page.



.. warning::

   This project is under active development. Good documentation is rare/non-existent. If you have questions please email me at tjost@bwh.harvard.edu.
   
   Additionally, this project is open-source and hosted on GitHub at `www.github.com/tylerjost/erisDocs <https://www.github.com/tylerjost/erisDocs/>`_.  

.. toctree::
   :maxdepth: 7
   :titlesonly:
   :hidden:



.. usage
.. --------
.. .. include:: usage.rst

Getting Started
---------------
.. include:: nirmalLabStart.md
   :parser: myst_parser.sphinx_

Running Code on ERISXdl
--------------------------------------
.. include:: containers.md
   :parser: myst_parser.sphinx_

Submitting Jobs on ERISXdl
--------------------------------------
.. include:: slurmJobs.md
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

