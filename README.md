# Vidyut: Power Generation Using Renewable Sources for Sustainability

## Overview
This is a final-year engineering project focused on generating electricity from sewage waste as a renewable resource. It addresses issues like coal depletion, environmental pollution, and improper sewage treatment by converting sewage into biogas (methane) for power generation. Key components include:
- **Mechanical Setup**: Digester for biogas production, boiler for steam generation, turbine and dynamo for electricity conversion.
- **Smart Automation**: Sensors (e.g., temperature, gas, voltage) and microcontrollers (ATMEGA328) for boiler safety, with wireless monitoring via HC-12 module.
- **Smart Monitoring**: Algorithm to track waste across multiple plants and suggest transfers to optimize usage and prevent wastage.

The project promotes sustainability, reduces human risk in sewage handling, and supports India's Swachh Bharat Mission.

## Hardware Requirements
- ATMEGA328 Microcontroller (x2)
- Sensors: MQ4 (gas), DS18B20 (temperature)
- Displays: LCD (16x2)
- Motors: Stepper, water pump
- Wireless: HC-12 module
- Other: Cooker (boiler), stove, dynamo, LEDs, buzzers, etc.
- See Chapter 5.2 in the report for full cost breakdown (~Rs. 4720).

## Software Requirements
- Arduino IDE for microcontroller code (not provided here; refer to report for boiler automation logic).
- Python 3.x for monitoring script (see monitoring/README.md).
- Java (optional, for alternative monitoring as in report).

## Setup and Installation
1. Assemble hardware as per block diagrams (Figures 3.1–3.3 in report).
2. Program microcontrollers for boiler automation (transmitter/receiver sides).
3. For monitoring: See monitoring subfolder.
4. Collect sewage waste, filter, and process in digester (as described in Chapter 5).

## Running the Project
1. Power on hardware setup.
2. Monitor boiler via wireless indicators.
3. Run monitoring script daily to input plant data and get transfer suggestions.
4. Generate electricity: Burn methane to produce steam, rotate turbine.

## Results and Analysis
- Methane yield: ~68% from sewage (vs. 72.5% from biogas plants; see Figures 5.6–5.7).
- Payback: Similar to case studies (1–2 years; Chapter 2).
- Future Scope: Convert methane to ethanol, integrate with waste water management.

## Contributors
- Ms. Shreya Mani
- Ms. Tanaya Mandhare
- Mr. Ashutosh Sonar
- Supervisor: Dr. Sharad Jadhav

## License
This project is for educational purposes. Cite the report if using.

For issues, refer to the report or contact contributors.
