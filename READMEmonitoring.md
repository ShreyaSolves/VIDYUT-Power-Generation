# Smart Monitoring System for Vidyut

## Overview
This module monitors sewage waste across multiple power plants, calculates balances (load - capacity), and suggests transfers from surplus to deficit plants. It optimizes waste distribution to maximize efficiency and minimize wastage. This is a Python implementation (different from the report's Java code) using dictionaries and greedy matching for better handling of partial transfers and priorities.

Purpose: Serves the smart monitoring described in Chapter 4 (Figure 4.1) and Chapter 5 (Figures 5.8–5.10) of the report.

## Requirements
- Python 3.x (no external libraries needed).

## Files
- `monitoring.py`: Main script.

## Setup
1. Clone or copy the script.
2. Edit `plant_names` list in the code to add/remove plants (assumes order by proximity).

## Running
1. Run `python monitoring.py` in a terminal.
2. Input capacities and loads for each plant when prompted.
3. View balances and transfer suggestions.

## Logic Explanation
- Inputs: Plant capacities and loads.
- Balances: load - capacity (positive = surplus, negative = deficit).
- Sorting: Surplus by largest amount descending; deficits by largest need descending.
- Matching: Greedy algorithm - Fill largest deficits first using largest surpluses, allowing partial transfers.
- Outputs: Console logs with suggestions (e.g., "Transfer X units from A to B").

## Example
See inline in the response above.

## Customization
- Add distances: Modify sorting to use a distance matrix.
- Integration: Extend to read from files/DB or automate via cron jobs.
- Edge Cases: Handles no surpluses/deficits, partial fills.

## Limitations
- Console-based; no GUI.
- Assumes manual daily input (can be automated).

For the full project context, see the main README.md.
