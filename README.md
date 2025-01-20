# Quick Sentiment Analyzer

A lightweight Python script for rapid sentiment analysis of text data from CSV files using NLTK and VADER lexicons.

## Overview

This script provides a quick way to gauge the sentiment of text data in CSV files. It's designed for preliminary analysis and dataset quality assessment rather than formal sentiment analysis. Each text statement is analyzed and rated on a scale from -1 (negative) to +1 (positive) using NLTK's VADER sentiment analyzer.


## Prerequisites

```python
pip install nltk
```

## Usage

1. Ensure your input file is in CSV format
2. Run the script: `python sentiment_analyzer.py`
3. Follow the prompts to:
   - Enter your input CSV filename
   - Select the column containing text data
4. Results will be saved to a new CSV file with "_with_sentiment" suffix

## Output

The script generates a new CSV file containing:
- Original text data
- Compound sentiment scores (-1 to +1)
  - Negative: -1 to 0
  - Neutral: 0
  - Positive: 0 to +1

## Limitations

- Accuracy depends heavily on input data quality
- Best suited for English language text
- Intended for quick analysis rather than production use
- Performance may vary based on dataset characteristics

## Contact

For questions or feedback, contact: gerard.gd@icloud.com

## Note

This tool is designed for preliminary analysis and dataset exploration. For production-level sentiment analysis, consider using more sophisticated approaches or machine learning models.
