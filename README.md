# EB_AUTO - Python Release

This repository forms a Python implementation of the EB_AUTO Spreadsheet Energy Balance Model published by Brock and Arnold (2000). No changes have been made.

The model calculates each component of the surface energy balance and then, optionally, the amount of melting caused by each SEB component.

## Requirements

* Python >= 2.7
* NumPy

Additionally, to use the example `run_ebmodel_Samplmet.py`, you will need:

* Pandas
* Openpyxl

These dependencies will be met by all up-to-date releases of Anaconda Python.


## Installation and running the example

Either  `git clone` to your local environment or:
* download as a zip file
* extract it
* in a terminal window, change to the directory of the extracted zip file
* `python run_ebmodel_demo.py`


## Structure

The model is called using two main functions contained within the `ebmodel` module.

* `ebmodel.calculate_seb` returns the net shortwave, net longwave, sensible heat flux and latent heat flux components for the specified meteorology.
* `ebmodel.calculate_melt` returns the corresponding melt fluxes in millimetres water equivalent (mm w.e.).

Each of these main functions contains calls to several other functions defined in `ebmodel`.


## Making modifications and extensions

You may create your own driver scripts for your own purposes. For example, one of the reasons for porting the model to Python was to couple this model to an albedo model, thereby solving for time-evolving albedo.


## Referencing

This module implements the point-based glacier surface energy balance model
originally developed as a spreadsheet application by:

Brock, B. W., and Arnold, N. (2000) Technical Communication: A spreadsheet-
based (Microsoft Excel) point surface energy balance model for glacier and
snow melt studies. Earth Surface Processes and Landforms, 25, p 649-658.

Use of this model in a publication should be accompanied by a citation to 
the aforementioned reference and to this repository.







