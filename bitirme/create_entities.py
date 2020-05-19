import wikipedia as wiki
import requests
import json, copy

# Kategoriler sırasıyla:
# Doğa, Siyaset, Spor, Sanat
words = ["Hayvan", "Dünya", "Afet", "Doğa", "Bitki",
        "Türkiye", "Siyaset", "Siyasi Parti", "Birleşmiş Milletler", "Türkiye Büyük Millet Meclisi",
        "Bisiklet (spor)", "Futbol", "Basketbol", "Olimpiyat Oyunları", "Voleybol",
        "Müzik", "Heykel", "Tiyatro", "Edebiyat", "Resim"]

wiki.set_lang("tr")

entity_dict = {
        "id" : "",
        "title": "",
        "alias": "",
        "links": "",
        "categories": "",
        "content": ""
    }


S = requests.Session()
URL = "https://tr.wikipedia.org/w/api.php"

id_n = 1
entities = []
for word in words:
    print("Next word: " + word)
    
    a = wiki.page(word)
    
    categories = []
    for c in a.categories:
        cts = ((c.split(":"))[1])
        categories.append(cts)
   
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "backlinks",
        "bltitle": word,
        "bllimit": "max",
        "blfilterredir": "redirects"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    BACKLINKS = DATA["query"]["backlinks"]

    alias = [] 
    for b in BACKLINKS:
        alias.append(b["title"])
    
    entity_dict['id'] = str(id_n)
    entity_dict['title'] = word
    entity_dict['alias'] = alias
    entity_dict['links'] = a.links
    entity_dict['categories'] = categories
    entity_dict['content'] = a.content

    id_n = id_n+1

    ed = copy.deepcopy(entity_dict)
    entities.append(ed)

print("Creating json.\n")

with open('entities', 'w', encoding='utf8') as f:
    json.dump(entities, f, ensure_ascii=False)
    f.close()
