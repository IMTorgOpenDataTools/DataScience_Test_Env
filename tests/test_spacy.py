#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"




def test_spacy_without_gpu():
    """Basic spacy installation."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    assert len(doc) > 0


def test_spacy_with_gpu():
    """Run spacy with gpu.

    This uses the following for installation with CUDA 11.3:
    >>>> sudo apt install nvidia-cuda-toolkit
    >>>> /usr/local/cuda/bin/nvcc --version                     #gives the CUDA compiler version (which matches the toolkit version)
    >>>> pip install -U 'spacy[cuda113]'
    """
    import spacy
    spacy.require_gpu() 
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    assert len(doc) > 0


def test_gpu_performance_comparison():
    """Performance comparison experiment.

    Code adopted from github [issue](https://github.com/BlueBrain/Search/issues/337).
    """
    import timeit

    import numpy as np
    import spacy
    import sqlalchemy
    import torch.multiprocessing as mp

    from bluesearch.sql import retrieve_sentences_from_sentence_ids

    mp.set_start_method('fork')  # for n_process is bigger than 1 

    # 1. Initiate spacy model
    model = "en_core_web_trf"          # or "en_core_web_lg"
    pipes_to_disable = []              # or ['tagger', 'parser', 'attribute_ruler', 'lemmatizer']
    entity_ruler = True                # or False
    DB_URL = ""                        # URL to the database

    spacy.require_gpu()                # or spacy.require_cpu()
    nlp = spacy.load(model, disable=pipes_to_disable)
    if entity_ruler:
        ruler = nlp.add_pipe("entity_ruler")
        ruler.add_patterns([{"label": "LOCATION", "pattern": "Berlin"}])

    # 2. First experiment: nlp(sentence)
    # 2.a. Create sentence to process
    n_times = 1
    sentence = "Emmanuel Macron is living in Paris." * n_times
    # 2.b. Results
    doc = nlp(sentence)
    print(doc.ents)
    # 2.b. Compute runtime
    time_results = timeit.repeat(lambda: nlp(sentence), repeat=10, number=10)
    mean_time = np.mean(time_results)
    print(mean_time)

    # 3. Second experiment: nlp.pipe(texts)
    # 3.a. Load sentences from database
    engine = sqlalchemy.create_engine(DB_URL)
    n_sentences = 10
    n_process = 1 
    sentences = retrieve_sentences_from_sentence_ids(np.arange(1, n_sentences+1), engine)
    texts = [(sent["text"], {"article_id": sent["article_id"], "sentence_id": sent["sentence_id"]}) for i, sent in sentences.iterrows()]
    all_texts.append(texts)
    # 3.b. Compute runtime
    time_results = timeit.repeat(lambda: list(nlp.pipe(texts, as_tuples=True)), repeat=10, number=10)
    mean_time = np.mean(time_results)
    print(mean_time)