===============================================================================

Natural Language Processing
Professor Collins
Homework 4 - Programming
Frankcarlos Castro (fc2518)
===============================================================================

Part 1
------

1.  Trained my model for 7 epochs
    Ran the decoder with input file trees/dev.conll and output file outputs/dev_part1.conll

2.  Ran this script: python3 src/eval.py trees/dev.conll outputs/dev_part1.conll
    to get the unlabeled and labeled dependency accuracies.
   
    I received the following values:
        Unlabeled attachment score 82.41
        Labeled attachment score 79.23

3. Ran the decoder again on the blind test file (trees/test.conll)
   Output content to outputs/test_part1.conll 


Part 2
------

1. Trained my model for 7 epochs, now changing the hidden_dim to 400 instead of 200
   Ran the decoder with input file trees/dev.conll and output file outputs/dev_part2.conll

2.  Ran this script: python3 src/eval.py trees/dev.conll outputs/dev_part2.conll
    to get the unlabled and labeled dependency accuracies.

    I received the following values:
        Unlabeled attachment score 82.55
        Labeled attachment score 79.44

3.  Ran the decoder again on blind test file (trees/test.conll)
    Output content to outputs/test_part2.conll

4.  
