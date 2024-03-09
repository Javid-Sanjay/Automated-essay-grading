import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download the necessary data if not already present
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Load the text to be checked
text = "Your essay goes here."

# Tokenize the text into words
words = word_tokenize(text)

# Tag each word with its part of speech
tagged_words = nltk.pos_tag(words)

# Define a list of verb tenses that are indicative of past tense
past_tense_tags = ['VBD', 'VBN']

# Perform lemmatization on each word
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

text = input("Please enter the text you want to check: ")

text = "this are some sentences with gramaticle errors"

# Tokenize the text into individual words
words = nltk.word_tokenize(text)

# Tag each word with its part of speech
pos_tags = nltk.pos_tag(words)

# Correct any spelling mistakes using a spell checker library like pyspellchecker

# Implement grammar rules to correct sentence structure and usage errors
# You could write your own rules or use existing ones from libraries like GingerIt or LanguageTool

# Convert the corrected words back into a string
result = ' '.join(word for word, tag in pos_tags)

# Print the corrected sentence
print(result)

# Identify any verbs in past tense that could be changed to present tense
for i in range(len(tagged_words)):
    if tagged_words[i][1] in past_tense_tags:
        synsets = wordnet.synsets(lemmatized_words[i], pos='v')
        for synset in synsets:
            if '.01' in synset.name() and synset.pos() == 'v':
                print(f"There may be a grammatical error with the word '{words[i]}'. Consider changing it to '{lemmatized_words[i]}' for present tense.")
