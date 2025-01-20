import csv
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

#analysze sentiment ( using nltk vader lexicons)
nltk.download('vader_lexicon',quiet=True)
nltk.download('punkt_tab',quiet=True)       # for tokenization
nltk.download('stopwords',quiet=True)     # for stopword removal


# parse csv
input_file = input("input file name (.csv): ")
try:
    with open(input_file, "r"):
        pass
except FileNotFoundError:
        print("file not found.")
        sys.exit()

try:
    column_choice= int(input("specify column of data:"))
except ValueError:
    print("input should be an integer")
    sys.exit()

#logic read rsv
with open (input_file, 'r') as filename:
    csvreader = csv.reader(filename)
    header= next(csvreader)
    data= []

    # validate column index
    if column_choice < 0 or column_choice >= len(header):
        print(f"column index must be between 0 and {len(header) - 1}")
        sys.exit()

    # read data from specified column
    for row in csvreader:
        try:
            data.append(row[column_choice])
        except IndexError:
            print(f"warning: row doesn't have column {column_choice}")
            continue
#format text to be analysis
def process_data(text):
    # tokenize and lowercase
    lower =text.lower()
    tokens = word_tokenize(lower)
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    return ' '.join(tokens)


sia = SentimentIntensityAnalyzer()
#append to senti dat, ie sentiment score
for row in data:
    new_data = process_data(row)
    result = sia.polarity_scores(new_data)

#write data in new csv
# Write to new CSV with original data plus sentiment scores
output_file = input_file.rsplit('.', 1)[0] + '_with_sentiment.csv'
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)

    # Write header with new sentiment columns
    new_header =  ['Compound scores (+1 to -1)']
    writer.writerow(new_header)

    # Process each row and write to new file
    # Add sentiment scores to original row
    for row in data:
        processed_text = process_data(row)
        sentiment = sia.polarity_scores(processed_text)
        compound_score = sentiment['compound']
        writer.writerow([compound_score])

print(f"Sentiment analysis complete. Results written to: {output_file}")
