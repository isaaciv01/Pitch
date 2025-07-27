#!/usr/bin/env python3
"""
Demo script for the Baseball Pitching Report Generator
Shows how to use the program programmatically.
"""

from baseball_pitching_report import BaseballPitchingReport
import os

def main():
    """Demo function showing how to use the baseball pitching report generator."""
    
    # Path to the sample CSV file
    csv_file = "sample_pitching_data.csv"
    
    if not os.path.exists(csv_file):
        print(f"Error: Sample CSV file '{csv_file}' not found.")
        print("Please ensure the sample_pitching_data.csv file exists in the current directory.")
        return
    
    print("=== Baseball Pitching Report Generator Demo ===\n")
    
    # Create the report generator
    print("1. Creating report generator...")
    report_generator = BaseballPitchingReport(csv_file)
    
    # Load and validate data
    print("2. Loading and validating data...")
    if not report_generator.load_data():
        print("Failed to load data!")
        return
    
    if not report_generator.validate_data():
        print("Warning: Some expected columns are missing. The report may be incomplete.")
    
    # Generate summary statistics
    print("3. Generating summary statistics...")
    summary = report_generator.create_summary_statistics()
    print(f"   - Total pitchers: {summary.get('total_pitchers', 'N/A')}")
    print(f"   - Total games: {summary.get('total_games', 'N/A')}")
    print(f"   - Average ERA: {summary.get('avg_era', 'N/A'):.2f}")
    print(f"   - Average strikeouts: {summary.get('avg_strikeouts', 'N/A'):.2f}")
    
    # Create performance charts
    print("4. Creating performance charts...")
    charts = report_generator.create_performance_charts()
    print(f"   - Generated {len(charts)} charts:")
    for chart in charts:
        print(f"     * {os.path.basename(chart)}")
    
    # Generate PDF report
    print("5. Generating PDF report...")
    output_path = report_generator.create_pdf_report()
    print(f"   - Report saved to: {output_path}")
    
    print("\n=== Demo Complete ===")
    print("Check the 'reports' directory for the generated files:")
    print("- PDF report with tables and statistics")
    print("- Performance analysis charts")
    print("- Professional formatting ready for presentation")

if __name__ == "__main__":
    main()