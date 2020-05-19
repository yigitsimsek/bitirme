import gensim, os, csv
import numpy as np
                                                                                                        # Kategoriler:
pages = ["Hayvan", "Dünya", "Afet", "Doğa", "Bitki",                                                    # Doğa
        "Türkiye", "Siyaset", "Siyasi Parti", "Birleşmiş Milletler", "Türkiye Büyük Millet Meclisi",    # Siyaset
        "Bisiklet (spor)", "Futbol", "Basketbol", "Olimpiyat Oyunları", "Voleybol",                     # Spor
        "Müzik", "Heykel", "Tiyatro", "Edebiyat", "Resim"]                                              # Sanat
categories = ["Doğa", "Siyaset", "Spor", "Sanat"]

with open('page_vectors.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Page Name", "Vector", "Category"])

    for i in range(0,20):
        name = "w2v_model_" + str(i+1)
        model = gensim.models.Word2Vec.load(os.path.join("trained", name))

        page_vector = np.zeros(100)
        total_count = 0
        for w in model.wv.vocab:
            if(w != "0" and w != "1"):
                count =  model.wv.vocab[w].count
                vec = model.wv[w]

                total_count += count
                page_vector += count*vec
            else:
                avg_count = total_count/(len(model.wv.vocab))
                page_vector += avg_count*2*model.wv[w]
        page_vector = page_vector/(total_count + 20)

        writer.writerow([i, pages[i], page_vector, categories[int((i)/5)]])
