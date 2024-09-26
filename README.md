# ERISXdl - Nirmal Lab Documentation
Check out our documentation online from anywhere at https://erisdocs.readthedocs.io/en/latest/!

This is internal documentation for the Massachusets General Brigham high-performance computing (HPC) cluster ERISXdl. Documentation was created with [sphinx](https://www.sphinx-doc.org/en/master/). It is themed with sphinx [book theme](https://sphinx-book-theme.readthedocs.io/en/stable/). 

To get started create a development environment with conda:

```
conda env create -f environment.yml
```

Navigate into the `docs` folder then call:

```
make html
```

The home page is then built/updated and located in `docs/build/html/index.html`. 

Note: It is not necessary to build the document. You can simply open `index.html` in your browser of choice.