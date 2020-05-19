from gensim.models import Word2Vec
import multiprocessing, json
from time import time
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
import os

with open('last_vectors', 'r', encoding='utf8') as f:
    entities = json.load(f)
    f.close()

num_features = 100
min_word_count = 3
num_workers = multiprocessing.cpu_count()
context_size = 5
downsampling = 1e-3
seed = 1

cores = multiprocessing.cpu_count()

for e in entities:
    w2v_model = Word2Vec(min_count=2,
                window=2,
                size=100,
                sample=6e-5, 
                alpha=0.03, 
                min_alpha=0.0007, 
                negative=20,
                workers=cores-1)

    s = e['content'] + e['link_vector'] + e['category_vector']
    w2v_model.build_vocab(sentences=s)
    print("Word2Vec vocabulary length:", len(w2v_model.wv.vocab))

    t = time()
    w2v_model.train(s, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))
    w2v_model.init_sims(replace=True)

    if not os.path.exists("trained"):
        os.makedirs("trained")

    name = "w2v_model_" + str(e['id'])
    w2v_model.save(os.path.join("trained", name))
