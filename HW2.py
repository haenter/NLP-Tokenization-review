from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import operator

def load_text(file_path):
    with open(file_path) as infile:
        return infile.read()

def preprocess_text(text):
    # Tokenize, lowercase, remove stopwords, and stem the words
    words = word_tokenize(text.lower())
    sw = stopwords.words('english')
    sents = sent_tokenize(text)
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words if word not in sw and word not in ['.', ',']]
    return stemmed_words, words, sents

def term_frequency_distribution(termlist, character='nothing'):
    '''
    :param termlist: a list of tokens from a document
    :return: the frequency distribution of the tokens
    '''
    frequency_distrib = defaultdict(int)
    if character == 'nothing':
        for t in termlist:
            frequency_distrib[t] += 1
    else:
        for t in termlist:
            if t.startswith(character.lower()) or t.startswith(character.upper()):
                frequency_distrib[t] += 1
    return frequency_distrib

def average_token_length(tokens):
    average_length = 0
    for token in tokens:
        average_length += len(token) / len(tokens)
    return average_length

def main():
    # read files
    filetext1 = load_text('./science_text/scientificpub1')
    filetext2 = load_text('./science_text/scientificpub2')
    filetext3 = load_text('./science_text/scientificpub3')
    filetext = filetext1 + filetext2 + filetext3 # corpus
    # preprocessing and tokenizations
    stemmed_words1, words1, sents1 = preprocess_text(filetext1)
    stemmed_words2, words2, sents2 = preprocess_text(filetext2)
    stemmed_words3, words3, sents3 = preprocess_text(filetext3)
    stemmed_words, words, sents = preprocess_text(filetext)
    # average token length (word tokenization)
    avg_length = average_token_length(words1)
    # average token length (sent tokenization)
    avg_length = average_token_length(sents1)
    # frequency distribution of words
    before_preproc = term_frequency_distribution(words1)                #before preprocessing
    after_preproc = term_frequency_distribution(stemmed_words1)         #after preprocessing
    # frequency distribution of words that start with 'p' or 'P'
    before_preproc_p = term_frequency_distribution(words1, 'p')         #before preprocessing
    after_preproc_p = term_frequency_distribution(stemmed_words1, 'p')  #after preprocessing
    
    print ('Before preprocessing...')
    print ('The number of sentences in the article1: ', len(sents1))
    print ('The total number of words in the article1: ', len(words1))
    print ('Total number of word types in the article1: ', len(set(words1))),
    print('Average Length of word tokens in article 1: ', avg_length)
    print('Average Length of sentence tokens in article 1 = ', avg_length)
    print('After preprocessing...')
    print('The total number of words in article 1 after preprocessing:', len(stemmed_words1))
    print('Total number of word types in article 1:', len(set(stemmed_words1)))
    print ('Top 10 most frequent terms in article 1 (before preprocessing):')
    print (sorted(before_preproc.items(), key=operator.itemgetter(1),reverse=True)[:10])
    print('----------------------------------------------------------------------------')
    print ('Top 10 most frequent terms in article 1 (after preprocessing):')
    print (sorted(after_preproc.items(), key=operator.itemgetter(1),reverse=True)[:10])
    print('----------------------------------------------------------------------------')
    print ('Top 10 most frequent terms in article 1 (before preprocessing):')
    print (sorted(before_preproc_p.items(), key=operator.itemgetter(1),reverse=True)[:10])
    print('----------------------------------------------------------------------------')
    print ('Top 10 most frequent terms in article 1 (after preprocessing):')
    print (sorted(after_preproc_p.items(), key=operator.itemgetter(1),reverse=True)[:10])
    print('----------------------------------------------------------------------------')
    print('''There are some noises which are caused by web scrapting. If we look at the text,
    we see some Goto links, some Figures, Tables (repititive) and some wierd characters
    like â€” , â€‹ , خ؛=Pr(a)âˆ’Pr(e)1âˆ’Pr(e). The first noise which are caused by
    links, have low frequency. And, the odd characters have uniqe shapes. All in all, 
    the frequency of the noises is really low, so it will not affect the statistics. ''')
    print('----------------------------------------------------------------------------')
    print ('The number of sentences in the whole courpus: ', len(sents))
    print ('The total number of words in the whole corpus: ', len(words))
    print ('Total number of word types in the whole courpus: ', len(set(words))),
    print ('Lexical diversity of the whole corpus: ')
    print ((len(set(stemmed_words)))/len(stemmed_words))
    print('----------------------------------------------------------------------------')
    print('Average number of words: ', (len(words1) + len(words2) + len(words3)) / 3)
    print('Average number of sentences: ', (len(sents1) + len(sents2) + len(sents3)) / 3)
    print('----------------------------------------------------------------------------')
    print ('Lexical diversity of article 1: ')
    print ((len(set(stemmed_words1)))/len(stemmed_words1))
    print('----------------------------------------------------------------------------')
    print ('Lexical diversity of article 2: ')
    print ((len(set(stemmed_words2)))/len(stemmed_words2))
    print('----------------------------------------------------------------------------')
    print ('Lexical diversity of article 3: ')
    print ((len(set(stemmed_words3)))/len(stemmed_words3))
    print('----------------------------------------------------------------------------')
    print('Second article has the most lexical diversity among others!')
    
    

if __name__ == "__main__":
    main()
