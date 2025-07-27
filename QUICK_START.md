# Quick Start Guide

## Get Started in 3 Steps

### 1. Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Install required packages
pip install -r requirements.txt
```

### 2. Prepare Your CSV Data
Your CSV file should have columns like:
- `pitcher_name` - Name of the pitcher
- `team` - Team name
- `opponent` - Opposing team
- `date` - Game date
- `innings_pitched` - Number of innings pitched
- `hits`, `runs`, `earned_runs` - Basic stats
- `walks`, `strikeouts` - Pitching stats
- `era`, `whip` - Advanced metrics

### 3. Generate Your Report
```bash
# Using the command line
python baseball_pitching_report.py your_data.csv

# Or using the demo script
python demo.py
```

## Example Usage

```bash
# Generate report from sample data
python baseball_pitching_report.py sample_pitching_data.csv

# Check the generated files
ls reports/
```

## What You'll Get

1. **Professional PDF Report** with:
   - Summary statistics table
   - Game data table (first 20 records)
   - Performance analysis charts

2. **Individual Chart Images**:
   - Strikeouts vs Walks scatter plot
   - ERA distribution histogram
   - Innings pitched vs ERA correlation
   - Top performers bar chart

## Customization

- **Modify expected columns**: Edit the `expected_columns` list in `validate_data()`
- **Add new charts**: Add chart generation code in `create_performance_charts()`
- **Change PDF styling**: Modify colors, fonts, or layout in `create_pdf_report()`

## Troubleshooting

- **Missing dependencies**: Run `pip install -r requirements.txt`
- **CSV format issues**: Check column names match expected format
- **Permission errors**: Ensure write access to the reports directory

## Need Help?

- Check the full `README.md` for detailed documentation
- Review the sample CSV file `sample_pitching_data.csv` for format reference
- Run the demo script `python demo.py` to see the program in action