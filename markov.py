import collections
import random


def make_markov():
    return collections.defaultdict(lambda: collections.defaultdict(int))


def feed_markov(markov, words):
    last_word = None
    for word in words:
        if last_word is None:
            last_word = word
            continue
        markov[last_word.lower()][word.lower()] += 1
        markov[last_word.lower()][None] += 1
        last_word = word
    return markov


def walk_markov(markov):
    current = random.choice(markov.keys())
    while True:
        yield current
        current = _step_markov(markov[current.lower()])
        if current is None:
            current = random.choice(markov.keys())


def _step_markov(word_counts):
    total = word_counts[None]
    lucky = random.randint(0, total)
    for word, val in word_counts.iteritems():
        if word is None:
            continue
        lucky -= val
        if lucky <= 0:
            return word

