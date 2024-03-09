import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Get user input title and essay
title = input("Enter essay title: ")
essay = input("Enter essay text: ")



# Preprocess title and essay
title = title.translate(str.maketrans('', '', string.punctuation)).lower()
essay = essay.translate(str.maketrans('', '', string.punctuation)).lower()

# Calculate number of paragraphs in the essay
paragraphs = essay.split("\n\n")
num_paragraphs = len(paragraphs)

# Create TF-IDF vectorizer and fit on title and essay
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([title, essay])

# Calculate cosine similarity score between title and essay
similarity_score = cosine_similarity(tfidf_matrix)[0][1] * 100

# Evaluate essay size based on number of paragraphs
if num_paragraphs > 2:
    essay_size_percentage = 90
else:
    essay_size_percentage = (num_paragraphs / 2) * 100

# Print similarity score and essay size percentage
print("The essay is {:.2f}% related to the title.".format(similarity_score))
print("The percentage according to your essay size is {:.2f}%.".format(essay_size_percentage))
