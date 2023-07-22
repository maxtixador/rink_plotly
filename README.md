# Rink_Plotly

## Overview
Rink_Plotly is a Python library that provides a convenient and interactive way to plot hockey rinks using the Plotly graphing library. Whether you need to visualize full ice, offensive or defensive zones, or specific areas on the hockey rink, this package simplifies the process of creating customizable and visually appealing rink diagrams.

## Features
- Supports horizontal and vertical rink layouts to accommodate various visualization needs.
- Plot full ice, offensive and defensive zones, neutral zone, or any custom area on the rink.
- Draws key elements of a hockey rink, including the outer and inner circles, goal creases, faceoff circles, goal lines, and sidelines.
- Customizable appearance, such as colors, line widths, and transparency for different rink elements.
- Easily integrate with Plotly's extensive plotting capabilities for further customization and interactivity.

## Installation
You can install Your Package Name using pip:

```bash
pip install rink-plotly  
```

## Usage
To use Your Rink_Plotly, import the `rink_plot` module and call the `rink` function:
```bash
import rink-plotly.rink_plot as rink_plot

# Create a horizontal rink with full ice setting
fig = rink_plot.rink(setting="full", vertical=False)
fig.show()
```

## Requirements

- Python 3.6+
- numpy
- plotly

## License
Rink_Plotly is released under the MIT License. See the LICENSE file for details.

## Contributing
I welcome contributions from the community! If you have any bug fixes, feature suggestions, or improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## Contact
For any inquiries or questions, you can reach me at maxtixador@gmail.com. I'd love to hear your feedback and help with any concerns.


## Acknowledgments
I want to express our gratitude to the Plotly team for providing an excellent graphing library that makes interactive data visualization in Python a breeze.


