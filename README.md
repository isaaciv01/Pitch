# Baseball Pitching Game Report Generator

A professional Python tool that converts CSV baseball pitching data into comprehensive PDF reports with tables, statistics, and data visualizations.

## Features

- **CSV Data Processing**: Reads and validates baseball pitching statistics from CSV files
- **Professional PDF Reports**: Generates well-formatted PDF reports with tables and charts
- **Data Visualization**: Creates multiple charts including:
  - Strikeouts vs Walks scatter plot with trend line
  - ERA distribution histogram
  - Innings pitched vs ERA correlation
  - Top performers bar chart
- **Summary Statistics**: Calculates and displays key pitching metrics
- **Flexible Data Format**: Works with various CSV column formats

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**:
   ```bash
   python baseball_pitching_report.py --help
   ```

## Usage

### Basic Usage

```bash
python baseball_pitching_report.py your_pitching_data.csv
```

### Example with Sample Data

```bash
python baseball_pitching_report.py sample_pitching_data.csv
```

## Expected CSV Format

The program expects a CSV file with baseball pitching statistics. Here are the expected column names:

### Required Columns (for full functionality):
- `pitcher_name` - Name of the pitcher
- `team` - Team name
- `opponent` - Opposing team
- `date` - Game date
- `innings_pitched` - Number of innings pitched
- `hits` - Hits allowed
- `runs` - Runs allowed
- `earned_runs` - Earned runs allowed
- `walks` - Walks issued
- `strikeouts` - Strikeouts recorded
- `home_runs` - Home runs allowed
- `pitches_thrown` - Total pitches thrown
- `strikes` - Strikes thrown
- `balls` - Balls thrown
- `era` - Earned Run Average
- `whip` - Walks plus Hits per Inning Pitched

### Sample CSV Format:
```csv
pitcher_name,team,opponent,date,innings_pitched,hits,runs,earned_runs,walks,strikeouts,home_runs,pitches_thrown,strikes,balls,era,whip
Jacob deGrom,New York Mets,Washington Nationals,2023-04-15,7.0,3,1,1,2,12,0,98,72,26,1.29,0.71
```

## Output

The program generates:

1. **PDF Report** (`reports/baseball_pitching_report_YYYYMMDD_HHMMSS.pdf`):
   - Professional title page with metadata
   - Summary statistics table
   - Game data table (first 20 records)
   - Performance analysis charts

2. **Chart Images** (saved in `reports/` directory):
   - `strikeouts_vs_walks.png`
   - `era_distribution.png`
   - `innings_vs_era.png`
   - `top_pitchers.png`

## Report Contents

### 1. Summary Statistics
- Total pitchers and games
- Average and total statistics for all numeric columns
- Key performance metrics

### 2. Game Data Table
- Displays the first 20 games for readability
- Formatted with alternating row colors
- Professional table styling

### 3. Performance Analysis Charts
- **Strikeouts vs Walks**: Scatter plot with trend line showing correlation
- **ERA Distribution**: Histogram showing the spread of ERA values
- **Innings vs ERA**: Scatter plot showing relationship between innings and ERA
- **Top Performers**: Bar chart of top 10 pitchers by total strikeouts

## Customization

### Modifying Expected Columns
Edit the `expected_columns` list in the `validate_data()` method to match your CSV format.

### Adding New Charts
Add new chart generation code in the `create_performance_charts()` method.

### Customizing PDF Style
Modify the `create_pdf_report()` method to change colors, fonts, or layout.

## Error Handling

The program includes comprehensive error handling:
- Validates CSV file existence
- Checks for required columns
- Handles missing or invalid data gracefully
- Provides clear error messages

## Dependencies

- **pandas**: Data manipulation and analysis
- **reportlab**: PDF generation
- **matplotlib**: Chart creation
- **seaborn**: Enhanced chart styling
- **numpy**: Numerical operations
- **Pillow**: Image processing

## Troubleshooting

### Common Issues:

1. **Missing Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **CSV Format Issues**:
   - Ensure your CSV has the expected column names
   - Check for proper comma separation
   - Verify numeric data is properly formatted

3. **Chart Generation Errors**:
   - Ensure you have write permissions in the reports directory
   - Check that matplotlib backend is properly configured

4. **PDF Generation Issues**:
   - Verify reportlab is properly installed
   - Check file permissions for output directory

## Example Output

The generated PDF will include:
- Professional title with timestamp
- Summary statistics table
- Game data table with alternating row colors
- Multiple performance analysis charts
- Clean, readable formatting suitable for professional presentations

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the functionality.