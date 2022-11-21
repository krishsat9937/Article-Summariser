#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import Counter
from heapq import nlargest
from string import punctuation

import spacy
from spacy.lang.en.stop_words import STOP_WORDS


def auto_summarise(doc, num_sentences=3):
    """
    It takes a document, tokenizes it, removes stopwords and punctuation, and then uses the remaining
    words to calculate the sentence strength of each sentence in the document. The sentence strength isØ
    calculated by adding the normalized frequency of each word in the sentence. The top n sentences with
    the highest sentence strength are then returned as the summary
    
    :param doc: The document to be summarized
    :param num_sentences: The number of sentences you want in your summary, defaults to 3 (optional)
    :return: The summary of the text
    """
    nlp = spacy.load("en_core_web_md")
    doc = nlp(doc.replace("\n",""))

    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)    

    freq_word = Counter(keyword)

    #get the most frequently occuring word
    max_freq = Counter(keyword).most_common(1)[0][1]

    #normalizing every frequently occuring keyword
    for word in freq_word.keys():  
            freq_word[word] = (freq_word[word]/max_freq)

    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]

    summarized_sentences = nlargest(num_sentences, sent_strength, key=sent_strength.get)

    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    
    return summary