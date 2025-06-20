#!/usr/bin/env python
# src/jd_summarizer/main.py
import os
from jd_summarizer.crew import JDSummarizerCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the JD Summarizer crew.
    """
    inputs = {
        'job_title': 'Data Scientist',
        'companies_str': 'Google, Meta'
    }

    # Create and run the crew
    result = JDSummarizerCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()