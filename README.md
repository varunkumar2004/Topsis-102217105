# TOPSIS Analysis Tool

This project implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for multi-criteria decision making. The tool takes a decision matrix, applies weights and impacts for each criterion, and ranks the alternatives based on their relative performance. This python package was built under acronym topsis-varun-102217105 as University Student Project.

## Features
- Supports decision matrix input via CSV or Excel files (.xlsx, .xls).
- Allows customizable weights and impacts for each criterion.
- Outputs ranked results in a CSV file.

---

## Installation
1. Clone this repository or download the script file.
2. Ensure you have Python installed (version 3.6 or later).
3. Install the required dependencies using pip:

```bash
pip install numpy pandas openpyxl
```

---

## Usage

The script accepts command-line arguments to specify the input file, weights, impacts, and output file.

### Command
```bash
python topsis.py <input_file> <weights> <impacts> <output_file>
```

### Parameters
- **`<input_file>`**: Path to the input decision matrix file. Accepts `.csv`, `.xlsx`, or `.xls` files.
- **`<weights>`**: Comma-separated weights for each criterion (e.g., `0.3,0.4,0.3`).
- **`<impacts>`**: Comma-separated impacts for each criterion (`+` for beneficial, `-` for non-beneficial, e.g., `+,+,-`).
- **`<output_file>`**: Path to save the output CSV file containing ranks.

### Example
#### Input File (`data.csv`):
| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 |
|--------------|-------------|-------------|-------------|
| A1           | 250         | 16          | 12          |
| A2           | 200         | 20          | 10          |
| A3           | 300         | 18          | 15          |

#### Command:
```bash
python topsis.py data.csv "0.3,0.4,0.3" "+,+,-" output.csv
```

#### Output File (`output.csv`):
| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 | Rank |
|--------------|-------------|-------------|-------------|------|
| A1           | 250         | 16          | 12          | 2    |
| A2           | 200         | 20          | 10          | 3    |
| A3           | 300         | 18          | 15          | 1    |

---

## Functions

### `topsis(data, weights, impacts)`
Performs TOPSIS analysis and returns the ranks of the alternatives.

#### Parameters:
- **`data`**: 2D list or numpy array representing the decision matrix.
- **`weights`**: List of weights for each criterion.
- **`impacts`**: List of impacts (`+` or `-`) for each criterion.

#### Returns:
- List of ranks for the alternatives.

---

### `excel_to_csv(excel_file, csv_output)`
Converts an Excel file to a CSV file.

#### Parameters:
- **`excel_file`**: Path to the Excel file.
- **`csv_output`**: Path to save the converted CSV file.

#### Returns:
- The path to the converted CSV file.

---

## Notes
- Ensure that the weights and impacts match the number of criteria in the decision matrix.
- The decision matrix should not include the alternative names in the criteria columns (e.g., the first column in the input file should contain names like A1, A2, etc.).

---

## License
This project is licensed under the MIT License.