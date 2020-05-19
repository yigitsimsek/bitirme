# Remove punctuations, create list of lists.

import json, copy, string, sys

def remove_punctuation_2(s):
    return s.translate(None, string.punctuation)

def remove_punctuation_3(s):
    return s.translate(str.maketrans('','',string.punctuation))

if sys.version.startswith('2'):
    remove_punctuation = remove_punctuation_2
else:
    remove_punctuation = remove_punctuation_3

with open('lemmatized_sentences', 'r', encoding='utf8') as f:
    entities = json.load(f)
    f.close()

new_entities = []
for e in entities:
    cont = e['content']
    new_content = []
    for sentence in cont:
        s = sentence.lower()
        s = remove_punctuation(s)
        new_s = ""
        for word in s.split():
            if(len(word) > 2 and word.isalpha()):
                if(word not in ['veya', 'fakat', 'ancak', 'ama', 'her']):
                    new_s = new_s + word + " "
        new_s = new_s[:-1]
        new_content.append(new_s)
    
    e['content'] = new_content
    ed = copy.deepcopy(e)
    new_entities.append(ed)

new_entities_ll = []
for e in new_entities:
    cont = e['content']
    new_content = []
    new_sentence = []

    for sentence in cont:
        new_sentence = sentence.split()
        new_content.append(new_sentence)
    
    e['content'] = new_content
    ed = copy.deepcopy(e)
    new_entities_ll.append(ed)

with open('lemmatized_ll', 'w', encoding='utf8') as f:
    json.dump(new_entities_ll, f, ensure_ascii=False)
    f.close()