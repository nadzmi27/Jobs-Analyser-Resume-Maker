# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download tokenizer and stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Specifies the protocol buffer implementation in Python, used for efficient
# serialization and deserialization of structured data.
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

# Creating match function
def calculate_match_percentage(text1, text2):
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    match_percentage = cosine_sim[0, 1] * 100  # Convert to percentage
    return match_percentage

# Creating Keyword Extraction
def extract_key_terms(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_words = [w for w in word_tokens if not w in stop_words and w.isalpha()]

    return set(filtered_words)

