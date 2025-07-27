#!/usr/bin/env python3
"""
Baseball Pitching Game Report Generator
Converts CSV pitching data into a professional PDF report with tables and visualizations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os
import sys
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class BaseballPitchingReport:
    def __init__(self, csv_file_path):
        """Initialize the report generator with CSV file path."""
        self.csv_file_path = csv_file_path
        self.data = None
        self.output_dir = "reports"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def load_data(self):
        """Load and validate CSV data."""
        try:
            self.data = pd.read_csv(self.csv_file_path)
            print(f"Successfully loaded {len(self.data)} records from {self.csv_file_path}")
            return True
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return False
    
    def validate_data(self):
        """Validate that required columns exist in the data."""
        # Common baseball pitching statistics columns
        expected_columns = [
            'pitcher_name', 'team', 'opponent', 'date', 'innings_pitched', 
            'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'home_runs',
            'pitches_thrown', 'strikes', 'balls', 'era', 'whip'
        ]
        
        missing_columns = [col for col in expected_columns if col not in self.data.columns]
        if missing_columns:
            print(f"Warning: Missing columns: {missing_columns}")
            print(f"Available columns: {list(self.data.columns)}")
        
        return len(missing_columns) == 0
    
    def create_summary_statistics(self):
        """Create summary statistics for the report."""
        if self.data is None:
            return {}
        
        summary = {}
        
        # Basic statistics
        if 'pitcher_name' in self.data.columns:
            summary['total_pitchers'] = self.data['pitcher_name'].nunique()
            summary['total_games'] = len(self.data)
        
        # Pitching statistics
        numeric_columns = ['innings_pitched', 'hits', 'runs', 'earned_runs', 
                          'walks', 'strikeouts', 'home_runs', 'pitches_thrown', 
                          'strikes', 'balls', 'era', 'whip']
        
        for col in numeric_columns:
            if col in self.data.columns:
                summary[f'avg_{col}'] = self.data[col].mean()
                summary[f'total_{col}'] = self.data[col].sum()
        
        return summary
    
    def create_performance_charts(self):
        """Create performance visualization charts."""
        charts = []
        
        # Set style for better looking charts
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # 1. Strikeouts vs Walks scatter plot
        if 'strikeouts' in self.data.columns and 'walks' in self.data.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(self.data['walks'], self.data['strikeouts'], alpha=0.7)
            ax.set_xlabel('Walks')
            ax.set_ylabel('Strikeouts')
            ax.set_title('Strikeouts vs Walks')
            ax.grid(True, alpha=0.3)
            
            # Add trend line
            z = np.polyfit(self.data['walks'], self.data['strikeouts'], 1)
            p = np.poly1d(z)
            ax.plot(self.data['walks'], p(self.data['walks']), "r--", alpha=0.8)
            
            chart_path = os.path.join(self.output_dir, "strikeouts_vs_walks.png")
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.close()
            charts.append(chart_path)
        
        # 2. ERA distribution histogram
        if 'era' in self.data.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(self.data['era'], bins=15, alpha=0.7, edgecolor='black')
            ax.set_xlabel('ERA')
            ax.set_ylabel('Frequency')
            ax.set_title('ERA Distribution')
            ax.grid(True, alpha=0.3)
            
            chart_path = os.path.join(self.output_dir, "era_distribution.png")
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.close()
            charts.append(chart_path)
        
        # 3. Innings pitched vs ERA
        if 'innings_pitched' in self.data.columns and 'era' in self.data.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(self.data['innings_pitched'], self.data['era'], alpha=0.7)
            ax.set_xlabel('Innings Pitched')
            ax.set_ylabel('ERA')
            ax.set_title('Innings Pitched vs ERA')
            ax.grid(True, alpha=0.3)
            
            chart_path = os.path.join(self.output_dir, "innings_vs_era.png")
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.close()
            charts.append(chart_path)
        
        # 4. Top performers bar chart
        if 'pitcher_name' in self.data.columns and 'strikeouts' in self.data.columns:
            top_pitchers = self.data.groupby('pitcher_name')['strikeouts'].sum().sort_values(ascending=False).head(10)
            
            fig, ax = plt.subplots(figsize=(12, 6))
            top_pitchers.plot(kind='bar', ax=ax)
            ax.set_xlabel('Pitcher')
            ax.set_ylabel('Total Strikeouts')
            ax.set_title('Top 10 Pitchers by Total Strikeouts')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            chart_path = os.path.join(self.output_dir, "top_pitchers.png")
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.close()
            charts.append(chart_path)
        
        return charts
    
    def create_pdf_report(self, output_filename=None):
        """Generate the PDF report."""
        if output_filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"baseball_pitching_report_{timestamp}.pdf"
        
        output_path = os.path.join(self.output_dir, output_filename)
        
        # Create PDF document
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        story = []
        
        # Get styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.darkblue
        )
        
        # Title page
        story.append(Paragraph("Baseball Pitching Game Report", title_style))
        story.append(Spacer(1, 20))
        
        # Report metadata
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", styles['Normal']))
        story.append(Paragraph(f"Data source: {os.path.basename(self.csv_file_path)}", styles['Normal']))
        story.append(Paragraph(f"Total records: {len(self.data)}", styles['Normal']))
        story.append(Spacer(1, 30))
        
        # Summary Statistics
        story.append(Paragraph("Summary Statistics", heading_style))
        summary = self.create_summary_statistics()
        
        if summary:
            summary_data = []
            for key, value in summary.items():
                if isinstance(value, float):
                    summary_data.append([key.replace('_', ' ').title(), f"{value:.2f}"])
                else:
                    summary_data.append([key.replace('_', ' ').title(), str(value)])
            
            summary_table = Table(summary_data, colWidths=[3*inch, 1.5*inch])
            summary_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(summary_table)
            story.append(Spacer(1, 20))
        
        # Data Table
        story.append(Paragraph("Game Data", heading_style))
        
        # Select columns to display in the table
        display_columns = ['pitcher_name', 'team', 'opponent', 'date', 'innings_pitched', 
                          'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'era']
        
        available_columns = [col for col in display_columns if col in self.data.columns]
        
        if available_columns:
            # Prepare table data
            table_data = [available_columns]  # Header
            
            # Add data rows (limit to first 20 rows for readability)
            for _, row in self.data.head(20).iterrows():
                table_row = []
                for col in available_columns:
                    value = row[col]
                    if isinstance(value, float):
                        table_row.append(f"{value:.2f}")
                    else:
                        table_row.append(str(value))
                table_data.append(table_row)
            
            # Create table
            data_table = Table(table_data, colWidths=[1.2*inch] * len(available_columns))
            data_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            story.append(data_table)
            story.append(Spacer(1, 20))
        
        # Charts
        story.append(Paragraph("Performance Analysis", heading_style))
        charts = self.create_performance_charts()
        
        for chart_path in charts:
            if os.path.exists(chart_path):
                img = Image(chart_path, width=6*inch, height=4*inch)
                story.append(img)
                story.append(Spacer(1, 20))
        
        # Build PDF
        doc.build(story)
        print(f"PDF report generated successfully: {output_path}")
        return output_path

def main():
    """Main function to run the baseball pitching report generator."""
    if len(sys.argv) != 2:
        print("Usage: python baseball_pitching_report.py <csv_file_path>")
        print("Example: python baseball_pitching_report.py pitching_data.csv")
        sys.exit(1)
    
    csv_file_path = sys.argv[1]
    
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found.")
        sys.exit(1)
    
    # Create report generator
    report_generator = BaseballPitchingReport(csv_file_path)
    
    # Load and validate data
    if not report_generator.load_data():
        sys.exit(1)
    
    if not report_generator.validate_data():
        print("Warning: Some expected columns are missing. The report may be incomplete.")
    
    # Generate PDF report
    output_path = report_generator.create_pdf_report()
    print(f"\nReport generated successfully!")
    print(f"Output file: {output_path}")
    print(f"Check the 'reports' directory for the generated PDF.")

if __name__ == "__main__":
    main()