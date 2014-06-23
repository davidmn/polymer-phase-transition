polymer-phase-transition
========================

simulation of the thermal expansion of polymers during phase transitions

Dependencies
------------
- python 2.blah
- numpy

Goals
-----
 - Incremental transitions, DeltaT_t constant
 - Incremental transitions, DeltaT_t not constant
  - random increments?
  - curve fitting?
 - Constant DeltaT_t constant, non incremental Pn(T) OR Pn
 - Non constant DeltaT_t, non incremental Pn(T) OR Pn
 - Non constant DeltaT_t, non incremental Pn(T,n)
 - Create a package of these simulations that can be run by other people

To Do
-----
 - check that code meets python style guide
 - give system alpha_g and alpha_a
 - define increase temp
 - define measure thickness