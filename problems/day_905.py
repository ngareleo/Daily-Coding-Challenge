"""
This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to form a circle. 
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair
"""


def can_form_circle(words: list) -> bool:
    for word in words:
        words.remove(word)
        if chain_word(word, words):
            return True
    return False


def chain_word(word: str, pool: list) -> bool:
    if len(pool) == 0:
        return True

    for p in pool:
        if word[-1] == p[0]:
            pool.remove(p)
            chain_found = chain_word(p, pool)
            if chain_found:  # early quit
                return True

    return False
