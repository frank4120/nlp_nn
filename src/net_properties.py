class NetProperties:
    def __init__(self, word_embed_dim, pos_embed_dim, dep_embed_dim, hidden1_dim, minibatch_size):
        self.word_embed_dim = word_embed_dim
        self.pos_embed_dim = pos_embed_dim
        self.dep_embed_dim = dep_embed_dim
        self.hidden_dim = hidden1_dim
        self.minibatch_size = minibatch_size