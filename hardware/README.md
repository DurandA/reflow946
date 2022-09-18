# Hardware

The Reflow946 hardware design is available on [https://easyeda.com/DurandA/reflow](https://easyeda.com/DurandA/reflow).

Contributions in converting the project to KiCad are welcome.

## Revision 1.0

### BOM

Ferrite beads (`L1`, `L2`) are not really required, you can make a solder joint.

In addition to the PCB components, you will need a uFL/IPEX antenna. I use [this one from AliExpress](https://fr.aliexpress.com/item/4000044880454.html).

### Errata

Zero-cross detection circuitry is not required with the use of the MOC3041 and will be removed in future revisions of the board. You do not need to populate `U5`, `R2`, `R21` and you can use a 0Ω resistor over `D2` footprint.  
