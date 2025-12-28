# MOSFET Modeling Using X-Semi

## Objective
Design and analyze a MOSFET using the novel wide-bandgap semiconductor X-Semi
as the channel material, and predict its electrical behavior based on material
properties and device dimensions.

## Device Selection
An n-channel MOSFET (nMOS) structure was chosen using X-Semi as the channel
material due to its higher electron mobility. The source and drain regions are
heavily doped n-type, with a p-type substrate.

## Device Parameters
- Channel material bandgap: 1.8 eV
- Oxide thickness: 10 nm
- Oxide dielectric constant: 3.9
- Operating temperature: 300 K

## Analysis Performed
- Energy band diagram and device operation explanation
- Threshold voltage estimation
- Drain current modeling in linear and saturation regions
- Discussion of short-channel effects
- Comparison with silicon MOSFET behavior

## Numerical Results

Using the assumed oxide thickness = 10 nm and material parameters (e = 3.9), the following MOSFET
characteristics were estimated at 300 K:

- Flatband voltage = - 0.18 V
- Estimated threshold voltage (Vth): 0.928 V
- Expected region of operation:
  - Linear region for VDS < (VGS − Vth)
  - Saturation region for VDS ≥ (VGS − Vth)

The estimated threshold voltage reflects the influence of oxide thickness and
material properties on electrostatic control of the channel.


## Key Observations
The wide bandgap and moderate permittivity of X-Semi are expected to reduce
off-state leakage current and improve ON/OFF current ratio compared to silicon
MOSFETs.

## Comparison with Silicon MOSFETs

Compared to silicon MOSFETs, the X-Semi MOSFET is expected to exhibit lower
off-state leakage current and improved ON/OFF current ratio due to its wider
bandgap. However, short-channel effects may still arise depending on channel
length and oxide scaling.

