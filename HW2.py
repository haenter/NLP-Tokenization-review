from nltk.stem import *
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import operator
from collections import defaultdict 


sw = stopwords.words('english')
stemmer = PorterStemmer()

# infile = open('./news_text/sportsnews')
infile = open('./science_text/scientificpub1')
filetext1 = infile.read()

print ('Before preprocessing...')
#Perform sentence tokenization
sents1 = sent_tokenize(filetext1)
print ('The number of sentences in the article1: ', len(sents1))

#Perform word tokenization
words1 = word_tokenize(filetext1)
print ('The total number of words in the article1: ', len(words1))
print ('Total number of word types in the article1: ', len(set(words1))),

# average token length (word tokenization)
avg_length = 0
for word in words1 : 
    avg_length += len(word) / len(words1)
print('Average Length of word tokens in article 1: ', avg_length)

# average token length (sent tokenization)
avg_length = 0
for sent in sents1 : 
    avg_length += len(sent) / len(sents1)
print('Average Length of sentence tokens in article 1 = ', avg_length)


print ('After preprocessing...')
lowercase_words1 = word_tokenize(filetext1.lower())
stemmed_words1 = []
for pw in lowercase_words1:
    if not pw in sw and not pw in ['.',',']:
        stemmed_words1.append(stemmer.stem(pw))


print ('The total number of words in article 1 after preprocessing: '),
print (len(stemmed_words1))

print ('Total number of word types in article 1: '),
print (len(set(stemmed_words1)))


def term_frequency_distribution(termlist, character='nothing'):
    '''

    :param termlist: a list of tokens from a document
    :return: the frequency distribution of the tokens
    '''
    frequency_distrib = defaultdict(int)
    if character == 'nothing' : 
        for t in termlist:
            frequency_distrib[t]+=1
    else : 
        for t in termlist : 
            if t.startswith(character.lower()) or t.startswith(character.upper()) : 
                frequency_distrib[t] += 1
    return frequency_distrib

before_preproc = term_frequency_distribution(words1)
print ('Top 10 most frequent terms in article 1 (before preprocessing):')
print (sorted(before_preproc.items(), key=operator.itemgetter(1),reverse=True)[:10])
print('----------------------------------------------------------------------------')
after_preproc = term_frequency_distribution(stemmed_words1)
print ('Top 10 most frequent terms in article 1 (after preprocessing):')
print (sorted(after_preproc.items(), key=operator.itemgetter(1),reverse=True)[:10])
print('----------------------------------------------------------------------------')
before_preproc_p = term_frequency_distribution(words1, 'p')
print ('Top 10 most frequent terms in article 1 (before preprocessing):')
print (sorted(before_preproc_p.items(), key=operator.itemgetter(1),reverse=True)[:10])
print('----------------------------------------------------------------------------')
after_preproc_p = term_frequency_distribution(stemmed_words1, 'p')
print ('Top 10 most frequent terms in article 1 (after preprocessing):')
print (sorted(after_preproc_p.items(), key=operator.itemgetter(1),reverse=True)[:10])
print('----------------------------------------------------------------------------')

text = '''There are some noises which are caused by web scrapting. If we look at the text,
we see some Goto links, some Figures, Tables (repititive) and some wierd characters
like â€” , â€‹ , خ؛=Pr(a)âˆ’Pr(e)1âˆ’Pr(e). The first noise which are caused by
links, have low frequency. And, the odd characters have uniqe shapes. All in all, 
the frequency of the noises is really low, so it will not affect the statistics. '''
print(text)
print('----------------------------------------------------------------------------')

infile = open('./science_text/scientificpub2')
filetext2 = infile.read()
infile = open('./science_text/scientificpub3')
filetext3 = infile.read()
filetext = filetext1 + filetext2 + filetext3
#Perform sentence tokenization
sents = sent_tokenize(filetext)
print ('The number of sentences in the whole courpus: ', len(sents))

#Perform word tokenization
words = word_tokenize(filetext)
print ('The total number of words in the whole corpus: ', len(words))
print ('Total number of word types in the whole courpus: ', len(set(words))),

lowercase_words = word_tokenize(filetext.lower())
stemmed_words = []
for pw in lowercase_words:
    if not pw in sw and not pw in ['.',',']:
        stemmed_words.append(stemmer.stem(pw))

print ('Lexical diversity of the whole corpus: ')
print ((len(set(stemmed_words)))/len(stemmed_words))
print('----------------------------------------------------------------------------')

words2 = word_tokenize(filetext2)
words3 = word_tokenize(filetext3)

sents2 = sent_tokenize(filetext2)
sents3 = sent_tokenize(filetext3)

print('Average number of words: ', (len(words1) + len(words2) + len(words3)) / 3)
print('Average number of sentences: ', (len(sents1) + len(sents2) + len(sents3)) / 3)
print('----------------------------------------------------------------------------')

lowercase_words2 = word_tokenize(filetext2.lower())
stemmed_words2 = []
for pw in lowercase_words2:
    if not pw in sw and not pw in ['.',',']:
        stemmed_words2.append(stemmer.stem(pw))
lowercase_words3 = word_tokenize(filetext3.lower())
stemmed_words3 = []
for pw in lowercase_words3:
    if not pw in sw and not pw in ['.',',']:
        stemmed_words3.append(stemmer.stem(pw))

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










