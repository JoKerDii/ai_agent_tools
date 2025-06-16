#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debater.crew import Debater

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'Is AI going to replace human jobs? or create more jobs?',
    }
    
    try:
        result = Debater().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
