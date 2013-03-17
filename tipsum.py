import mailbox
import re
import os

import markov


WORD_RE = r'^[a-zA-Z][a-zA-Z-\']*$'


def words(body):
    for word in body.split():
        word = word.strip(' ,.[]')
        if re.match(WORD_RE, word):
            yield word


def main():
    mkv = markov.make_markov()
    mboxes = os.listdir('mboxes')
    for mbox_file in mboxes:
        mbox = mailbox.mbox('mboxes/' + mbox_file)
        for message in mbox:
            markov.feed_markov(mkv, words(message.get_payload()))

    w = markov.walk_markov(mkv)
    for i in xrange(500):
        print w.next(),


if __name__ == '__main__':
    main()
