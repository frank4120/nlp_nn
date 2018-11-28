from collections import defaultdict

class Vocab:
    def __init__(self):
        # Creating actions dictionary
        aFile = open('data/vocabs.actions', 'r')
        self.action_dict = defaultdict(int)

        for line in aFile:
            pair = line.split()
            self.action_dict[pair[0]] = int(pair[1])

        # Creating label dictionary
        lFile = open('data/vocabs.labels', 'r')
        self.label_dict = defaultdict(int)

        for line in lFile:
            pair = line.split()
            self.label_dict[pair[0]] = int(pair[1])

        # Creating POS dictionary
        pFile = open('data/vocabs.pos', 'r')
        self.pos_dict = defaultdict(int)

        for line in pFile:
            pair = line.split()
            self.pos_dict[pair[0]] = int(pair[1])

        # Creating word dictionary
        wFile = open('data/vocabs.word', 'r')
        self.word_dict = defaultdict(int)

        for line in wFile:
            pair = line.split()
            self.word_dict[pair[0]] = int(pair[1])

    def tag2id(self, tag):
        return self.pos_dict[tag]

    def dep2id(self, tag):
        return self.label_dict[tag]

    def action2id(self, tag):
        return self.action_dict[tag]

    def word2id(self, word):
        return self.word_dict[word] if word in self.word_dict else self.word_dict['<UNK>']

    def num_words(self):
        return len(self.word_dict)

    def num_dep(self):
        return len(self.label_dict)

    def num_tags(self):
        return len(self.pos_dict)

    def num_actions(self):
        return len(self.action_dict)

Vocab()
