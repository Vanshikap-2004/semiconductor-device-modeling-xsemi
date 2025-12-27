# PN Junction Design Using X-Semi

## Objective
Design and analyze a p–n junction diode using a novel wide-bandgap semiconductor
(X-Semi), starting from fundamental material parameters and predicting its electrical
behavior.

## Material Parameters
The semiconductor material is characterized by the following base parameters:

- Bandgap (Eg): 1.8 eV
- Relative permittivity (εr): 10
- Electron effective mass (mn*): 0.25 m0
- Hole effective mass (mp*): 0.5 m0
- Electron mobility (μn): 800 cm²/V·s
- Hole mobility (μp): 400 cm²/V·s
- Temperature: 300 K
- Vbi between 0.5 V and 1 V
- Width less than or equal to 1 um
- minority carrier concentration non-degenerate

## Approach
The device design was carried out by first deriving intrinsic carrier statistics from
effective mass theory, followed by junction electrostatics and current transport analysis.
Doping concentrations were chosen to satisfy constraints on built-in potential and
depletion width while avoiding degenerate carrier conditions.

## Key Analyses Performed
- Density of states and intrinsic carrier concentration derivation
- Doping selection for desired built-in potential
- Depletion width and electric field estimation
- Ideal diode current derivation and I–V prediction
- Temperature and doping variation analysis

## Theory Reference
Detailed analytical derivations for carrier statistics, electrostatics, and current
transport are provided in the [theory/derivations.pdf](theory/derivations.pdf) file.


## Numerical Results

Using the derived carrier statistics and electrostatic relations, the following
device parameters were obtained at 300 K:

- Intrinsic carrier concentration (ni): 4194.59 cm⁻³
- Built-in potential (Vbi): 0.99 V
- Total depletion width (W): 0.66 μm
- Depletion width on p-side (xp): 0.33 μm
- Depletion width on n-side (xn): 0.33 μm
- Maximum electric field (Emax): 30000 V/cm
- Saturation current (Is) for 1 mm² area: 1.047 x 10^(-17) A

These results satisfy the design constraints of moderate built-in potential,
sub-micron depletion width, and non-degenerate carrier concentrations.

## Temperature Dependence

When the temperature is increased to 400 K, the intrinsic carrier concentration
increases significantly, leading to a reduction in built-in potential and an
increase in saturation current. This behavior highlights the improved thermal
stability of wide-bandgap semiconductors compared to silicon.

## Key Observations
The wide bandgap of X-Semi leads to a significantly lower intrinsic carrier concentration
compared to silicon, resulting in reduced reverse leakage current and improved thermal
stability.

## Comparison with Silicon
Compared to silicon diodes, the designed junction exhibits higher turn-on voltage,
lower leakage current, and potentially faster switching behavior due to higher carrier
mobility.



