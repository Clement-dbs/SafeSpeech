import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import unicodedata

nltk.download('stopwords')
nltk.download("wordnet")

class TextCleaner:
    
    def __init__(self, 
                 lowercase=True, 
                 remove_apostrophe=True,
                 remove_urls=True,
                 remove_mentions=True,
                 remove_hashtags=True,
                 remove_emojis=True,
                 remove_accents=True,
                 remove_stopwords=True,
                 lemmatize=True,
                 stem=False,
                 language='english'):
        
        self.lowercase = lowercase
        self.remove_apostrophe = remove_apostrophe
        self.remove_urls = remove_urls
        self.remove_mentions = remove_mentions
        self.remove_hashtags = remove_hashtags
        self.remove_emojis = remove_emojis
        self.remove_accents = remove_accents
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.stem = stem
        self.language = language
        

        if self.remove_stopwords:
            self.stopwords = set(stopwords.words(language))
        
        if self.lemmatize:
            self.lemmatizer = WordNetLemmatizer()
        
        if self.stem:
            self.stemmer = PorterStemmer()
    
    def clean(self, text):
        # Lowercase
        if self.lowercase:
            text = text.lower()
        
        # Supprimer accents
        if self.remove_accents:
            nfd = unicodedata.normalize('NFD', text)
            text = ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
        
        # URLs
        if self.remove_urls:
            text = re.sub(r'http\S+|www\S+', '', text)
        
        # Mentions
        if self.remove_mentions:
            text = re.sub(r'@\w+', '', text)
        
        # Hashtags
        if self.remove_hashtags:
            text = re.sub(r'#\w+', '', text)
        
        # Emojis et caractères spéciaux
        if self.remove_emojis:
            text = re.sub(r'[^\w\s\']', '', text)

        # Supprimer les apostrophes
        if self.remove_apostrophe:
            text = re.sub(r"[’']", " ", text)

        # Caractères dupliqués
        text = re.sub(r'(!)\1{1,}|\?\?+|\.{2,}', lambda m: m.group(0)[0], text)
        
        # Normaliser espaces
        text = re.sub(r'\s+', ' ', text).strip()

        # Tokenization
        tokens = word_tokenize(text)
        
        # Stopwords
        if self.remove_stopwords:
            tokens = [token for token in tokens if token.lower() not in self.stopwords]
        
        # Lemmatisation
        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        # Stemming
        if self.stem:
            tokens = [self.stemmer.stem(token) for token in tokens]
        
        return tokens
    
    def clean_corpus(self, corpus):
        return [self.clean(text) for text in corpus]
    

if __name__ == "__main__":
    cleaner = TextCleaner()

    texts = [
        "The sun rises early in the spring mornings.",
        "I bought a new notebook to write down my ideas.",
        "She enjoys walking along the beach at sunset.",
        "The cat jumped onto the windowsill and watched the birds.",
        "He forgot his umbrella and got soaked in the rain.",
        "Traveling teaches you more than any classroom ever could.",
        "The city streets were quiet after midnight.",
        "I’m trying a new recipe for dinner tonight.",
        "They laughed loudly at the comedian’s joke.",
        "The old library smelled of books and polished wood."
        ]
    
    dataset_cleaned = []

    for text in texts:
        cleaned = cleaner.clean(text)
        dataset_cleaned.append(cleaned)
    print(dataset_cleaned)

