import json, copy

with open('lemmatized_ll', 'r', encoding='utf8') as f:
    entities = json.load(f)
    f.close()

all_links = []
all_categories = []
for e in entities:
    for l in e['links']:
        if(l not in all_links):
            all_links.append(l)
    for c in e['categories']:
        if(l not in all_categories):
            all_categories.append(c)
all_links.sort()
all_categories.sort()

new_entities = []
for e in entities:
    link_vector = ["0"] * len(all_links)
    category_vector = ["0"] * len(all_categories)

    for l in list(set(e['links'])):
        i = all_links.index(l)
        link_vector[i] = "1"
    e['link_vector'] = link_vector
    
    for c in list(set(e['categories'])):
        i = all_categories.index(c)
        category_vector[i] = "1"
    e['category_vector'] = category_vector
    
    ed = copy.deepcopy(e)
    new_entities.append(ed)
        
with open('last_vectors', 'w', encoding='utf8') as f:
    json.dump(new_entities, f, ensure_ascii=False)
    f.close()