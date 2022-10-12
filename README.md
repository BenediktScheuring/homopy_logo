# HomoPy
*Your solution for stiffness problems*

HomoPy is a Python package to perform caluclations of effective stiffness properties in homogenized materials, with an emphasize on fiber reinforced polymers.
Currently, HomoPy offers two types of homogenization procedures:
- Halpin-Tsai with a Shear-Lag modification
- Mori-Tanaka

## Halpin-Tsai
The Halpin-Tsai method is an empirical approach to homogenize two isotropic materials. Our approach is modified with the Shear-Lag model after Cox (cf. [1]), which is also used in ___ (xxxx) and ___ (xxxx). Being a scalar homeginzation scheme, it allows to calculate the effective stiffness in the plane which is orthogonal to the isotropic plane within transverse isotropic materials, as it is the case for unidirectional reinforced polymers. The effective stiffness, or Young's modulus, is then a function of the angle to the reinforcing direction. A fiber distrubtion within the plane is recognized by volume averaging of imaginary plies of individual orientations in analogy to the laminate theory.

## Mori-Tanaka
The Mori-Tanaka scheme goes back to Mori and Tanaka (xxxx) and is a mean-field homogenization scheme based on Eshelby's solution (xxxx). The implementation so far only allows spheroidal inclusions, which in fact is an ellispoid with identical minor axes or ellipsoid of revolution, respectively. Our algorithm allows to homogenize materials with different types of fibers, each possibily having an individual fiber distrubtion. Being a tensorial homogenization scheme, the fiber orientation tensor is directly included in the calculation and the result is an effective stiffness tensor. The authors would like to emphasize that for multi-inclusion problems or non-isotropic inclusions, the effective stiffness tensor may violate thermodynamic requirements, such as a symmetric stiffness tensor. Further readings of this attribute are given in ___ (xxxx) and ___ (xxxx). It is in the remit of the user to keep this in mind and act accordingly.

***
Further topic related methods of the package:
- Closures to calculate orientation tensors of forth order from an orientation tensor of second order are implemented by a dependence on the package [fiberoripy](https://github.com/nilsmeyerkit/fiberoripy)
- Determining fiber orientation tensors from micrographs is possible by the implemented method of ellipses (yet to come)

***
[1] H. L. Cox, The elasticity and strength of paper and other fibrous materials, British Journal of Applied Physics 3 (3) (1952) 72–79. doi:10.1088/05083443/3/3/302.
