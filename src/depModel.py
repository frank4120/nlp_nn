import os,sys
from optparse import OptionParser
from decoder import *
from network import *
from Vocab import *
from net_properties import *
import os.path

class DepModel:
    def __init__(self):
        '''
            You can add more arguments for examples actions and model paths.
            You need to load your model here.
            actions: provides indices for actions.
            it has the same order as the data/vocabs.actions file.
        '''
        # if you prefer to have your own index for actions, change this.
        self.actions = ['SHIFT', 'LEFT-ARC:rroot', 'LEFT-ARC:cc', 'LEFT-ARC:number', 'LEFT-ARC:ccomp', 'LEFT-ARC:possessive', 'LEFT-ARC:prt', 'LEFT-ARC:num', 'LEFT-ARC:nsubjpass', 'LEFT-ARC:csubj', 'LEFT-ARC:conj', 'LEFT-ARC:dobj', 'LEFT-ARC:nn', 'LEFT-ARC:neg', 'LEFT-ARC:discourse', 'LEFT-ARC:mark', 'LEFT-ARC:auxpass', 'LEFT-ARC:infmod', 'LEFT-ARC:mwe', 'LEFT-ARC:advcl', 'LEFT-ARC:aux', 'LEFT-ARC:prep', 'LEFT-ARC:parataxis', 'LEFT-ARC:nsubj', 'LEFT-ARC:<null>', 'LEFT-ARC:rcmod', 'LEFT-ARC:advmod', 'LEFT-ARC:punct', 'LEFT-ARC:quantmod', 'LEFT-ARC:tmod', 'LEFT-ARC:acomp', 'LEFT-ARC:pcomp', 'LEFT-ARC:poss', 'LEFT-ARC:npadvmod', 'LEFT-ARC:xcomp', 'LEFT-ARC:cop', 'LEFT-ARC:partmod', 'LEFT-ARC:dep', 'LEFT-ARC:appos', 'LEFT-ARC:det', 'LEFT-ARC:amod', 'LEFT-ARC:pobj', 'LEFT-ARC:iobj', 'LEFT-ARC:expl', 'LEFT-ARC:predet', 'LEFT-ARC:preconj', 'LEFT-ARC:root', 'RIGHT-ARC:rroot', 'RIGHT-ARC:cc', 'RIGHT-ARC:number', 'RIGHT-ARC:ccomp', 'RIGHT-ARC:possessive', 'RIGHT-ARC:prt', 'RIGHT-ARC:num', 'RIGHT-ARC:nsubjpass', 'RIGHT-ARC:csubj', 'RIGHT-ARC:conj', 'RIGHT-ARC:dobj', 'RIGHT-ARC:nn', 'RIGHT-ARC:neg', 'RIGHT-ARC:discourse', 'RIGHT-ARC:mark', 'RIGHT-ARC:auxpass', 'RIGHT-ARC:infmod', 'RIGHT-ARC:mwe', 'RIGHT-ARC:advcl', 'RIGHT-ARC:aux', 'RIGHT-ARC:prep', 'RIGHT-ARC:parataxis', 'RIGHT-ARC:nsubj', 'RIGHT-ARC:<null>', 'RIGHT-ARC:rcmod', 'RIGHT-ARC:advmod', 'RIGHT-ARC:punct', 'RIGHT-ARC:quantmod', 'RIGHT-ARC:tmod', 'RIGHT-ARC:acomp', 'RIGHT-ARC:pcomp', 'RIGHT-ARC:poss', 'RIGHT-ARC:npadvmod', 'RIGHT-ARC:xcomp', 'RIGHT-ARC:cop', 'RIGHT-ARC:partmod', 'RIGHT-ARC:dep', 'RIGHT-ARC:appos', 'RIGHT-ARC:det', 'RIGHT-ARC:amod', 'RIGHT-ARC:pobj', 'RIGHT-ARC:iobj', 'RIGHT-ARC:expl', 'RIGHT-ARC:predet', 'RIGHT-ARC:preconj', 'RIGHT-ARC:root']

        parser = OptionParser()
        parser.add_option("--train", dest="train_file", metavar="FILE", default=None)
        parser.add_option("--train_data", dest="train_data_file", metavar="FILE", default='../data/train.data')
        parser.add_option("--test", dest="test_file", metavar="FILE", default=None)
        parser.add_option("--output", dest="output_file", metavar="FILE", default=None)
        parser.add_option("--model", dest="model_path", metavar="FILE", default='trained.model')
        parser.add_option("--vocab", dest="vocab_path", metavar="FILE", default=None)
        parser.add_option("--we", type="int", dest="we", default=64)
        parser.add_option("--pe", type="int", dest="pe", default=32)
        parser.add_option("--de", type="int", dest="de", default=32)
        parser.add_option("--hidden", type="int", dest="hidden", default=200)
        parser.add_option("--minibatch", type="int", dest="minibatch", default=1000)
        parser.add_option("--epochs", type="int", dest="epochs", default=7)

        (options, args) = parser.parse_args()

        #if options.train_file and options.train_data_file and options.model_path:
        if options.train_data_file and options.model_path:
            net_properties = NetProperties(options.we, options.pe, options.de, options.hidden, options.minibatch)

            # creating vocabulary file
            vocab = Vocab()

            # writing properties and vocabulary file into pickle
            # pickle.dump((vocab, net_properties), open(options.vocab_path, 'w'))

            # constructing network
            network = Network(vocab, net_properties)

            # training
            network.train(options.train_data_file, options.epochs)

            # saving network
            network.save(options.model_path)

        if options.test_file and options.model_path and options.output_file:
            # loading vocab and net properties
            # vocab, net_properties = pickle.load(open(options.vocab_path, 'r'))

            vocab = Vocab()
            net_properties = NetProperties(options.we, options.pe, options.de, options.hidden, options.minibatch)

            # constructing default network
            network = Network(vocab, net_properties)

            # loading network trained model
            network.load(options.model_path)

            # writer = open(options.output_file, 'w')
            # for sentence in open(options.test_file, 'r'):
            #     words = sentence.strip().split()
            #     tags = network.decode(words)
            #     output = [word + '\t' + tag for word, tag in zip(words, tags)]
            #     writer.write('\n'.join(output) + '\n\n')
            # writer.close()

        # # Create vocabulary object (dictionaries of vocab file data)
        # vocab = Vocab()
        #
        # # constructing network
        # network = Network(vocab, net_properties)
        #
        # if os.path.isfile('trained.model'):
        #     # load stored trained model
        #     network.load('trained.model')
        # else:
        #     # train network for given epochs
        #     network.train('../data/train.data', epochs)
        #
        # # saving network
        # network.save('trained.model')


    def score(self, str_features):
        '''
        :param str_features: String features
        20 first: words, next 20: pos, next 12: dependency labels.
        DO NOT ADD ANY ARGUMENTS TO THIS FUNCTION.
        :return: list of scores
        '''
        # change this part of the code.
        # return [0]*len(self.actions)
        output = self.network.build_graph(str_features)
        scores = output.npvalue()
        return scores

if __name__=='__main__':

    m = DepModel()

    input_p = os.path.abspath(sys.argv[1])
    output_p = os.path.abspath(sys.argv[2])
    Decoder(m.score, m.actions).parse(input_p, output_p)