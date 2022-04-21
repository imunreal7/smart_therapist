import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


def get_words_in_dataset(dataset):
    all_words = []
    for (words, sentiment) in dataset:
      all_words.extend(words)
 
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
  
    return word_features


def read_datasets(fname, t_type):
    data = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()
    return data


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_dataset(data):
    return classifier.classify(extract_features(nltk.word_tokenize(data)))


# read in joy , disgust, sadness, shame, anger, guilt, fear training dataset

joy_feel= read_datasets('D:/project/minor/smartTherapist/main/static/main/text/joy.txt', 'joy')
disgust_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/disgust.txt', 'disgust')
shame_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/shame.txt', 'shame')
sadness_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/sadness.txt', 'sadness')
anger_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/anger.txt', 'anger')
guilt_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/guilt.txt', 'guilt')
fear_feel = read_datasets('D:/project/minor/smartTherapist/main/static/main/text/fear.txt', 'fear')

# filter away words that are less than 3 letters to form the training data
indata = []
for (words, sentiment) in joy_feel + disgust_feel + shame_feel + sadness_feel + anger_feel + guilt_feel + fear_feel:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    indata.append((words_filtered, sentiment))




# extract the word features out from the training data
word_features = get_word_features(get_words_in_dataset(indata))




# get the training set and train the Naive Bayes Classifier
training_set = nltk.classify.util.apply_features(extract_features, indata)
classifier = NaiveBayesClassifier.train(training_set)







