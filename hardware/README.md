# Hardware

The Reflow946 hardware design is available on [https://easyeda.com/DurandA/reflow](https://easyeda.com/DurandA/reflow).

Contributions in converting the project to KiCad are welcome.

## Revision 1.0

### BOM

| Name | Designator | Footprint | Quantity | Supplier |
|---|---|---|---|---|
| MOC3041M | U1 | DIP-6_L8.5-W6.4-P2.54-LS7.6-BL | 1 | [LCSC](https://lcsc.com/product-detail/C8921.html) |
| ESP32-WROOM-32U | U2 | WIFIM-SMD_39P-L19.2-W18.0-P1.27 | 1 | [LCSC](https://lcsc.com/product-detail/C3013938.html) |
| MAX31855KASA | U3 | SO-8_L4.9-W3.9-P1.27-LS5.9-BL | 1 | [LCSC](https://lcsc.com/product-detail/C52028.html) |
| AMS1117-3.3 | U4 | SOT-223-3_L6.5-W3.4-P2.30-LS7.0-BR | 1 | [LCSC](https://lcsc.com/product-detail/C6186.html) |
| ~EL817~ | U5 | SOP-4_L6.5-W4.6-P2.54-LS10.2-TL | ~1~ | ~[LCSC](lcsc.com/product-detail/C183799.html)~ |
| 100nF | CBB1 | CAP-TH_L13.0-W6.0-P10.00-D1.2 | 1 | [LCSC](https://lcsc.com/product-detail/C105712.html) |
| 1000uF/25V | C1 | CAP-D10.0×F5.0 | 1 |  |
| 10u | C2,C3 | C0805 | 2 |  |
| 0.01u | C4 | C0603 | 1 |  |
| 10u | C5 | C0603 | 1 |  |
| 0.1u | C6 | C0603 | 1 |  |
| MB6F | D1 | MBF_L4.8-W3.9-P2.50-LS6.7-BL | 1 | [LCSC](https://lcsc.com/product-detail/C2490.html) |
| SM4007PL | D2 | SOD-123F_L2.8-W1.8-LS3.7-RD | 1 | [LCSC](https://lcsc.com/product-detail/C64898.html) |
| HDR-M-2.54_2x3 | ESP-PROG | HDR-M-2.54_2X3 | 1 | [LCSC](https://lcsc.com/product-detail/C65114.html) |
| SMD0805-020-16V | F1 | F0805 | 1 | [LCSC](https://lcsc.com/product-detail/C70057.html) |
| ~CBG100505U260T~ | L1,L2 | L0402 | ~2~ | ~[LCSC](https://lcsc.com/product-detail/C668229.html)~ |
| FJ4301BH | LED1 | LED-SEG-TH_12P-L30.1-W16.0-P2.54-S12.70-BL | 1 | [LCSC](https://lcsc.com/product-detail/C10706.html) |
| VH-2A | P1 | CONN-TH_VH3.96-2A | 1 | [LCSC](https://lcsc.com/product-detail/C16728.html) |
| VH3.96-3P2 | P2,P3 | CONN-TH_VH3.96-3P2 | 2 | [LCSC](https://lcsc.com/product-detail/C18157.html) |
| XH-2A | P4 | CONN-TH_XH-2A | 1 | [LCSC](https://lcsc.com/product-detail/C20079.html) |
| BTA16-600BRG | Q1 | TO-220-3_L10.0-W4.5-P2.54-L | 1 | [LCSC](https://lcsc.com/product-detail/C9100.html) |
| MMBT3904 | Q2,Q3,Q4 | SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR | 3 | [LCSC](https://lcsc.com/product-detail/C20526.html) |
| 220 | R1,R10,R11,R12,R13,<br>R14,R15,R16,R17 | R0603 | 9 |  |
| ~1k~ | R2,R21 | R0603 | ~2~ |  |
| 30 | R3 | R_AXIAL-0.5 | 1 |  |
| 330 | R4 | R_AXIAL-0.5 | 1 |  |
| 100R/2W | R5 | R_AXIAL-0.6 | 1 |  |
| 10k | R6,R8 | R0603 | 2 |  |
| D6C40F1LFS | SW1,SW2,SW3 | | 3 | [LCSC](https://lcsc.com/product-detail/C2689630.html) |
| uFL antenna | | | 1 | [AliExpress](https://aliexpress.com/item/4000044880454.html) |

Ferrite beads (`L1`, `L2`) are not really required, you can make a solder bridge.

### Errata

Zero-cross detection circuitry is not required with the use of the MOC3041 and will be removed in future revisions of the board. You do not need to populate `U5`, `R2`, `R21` and you can use a 0Ω resistor over `D2` footprint.  
