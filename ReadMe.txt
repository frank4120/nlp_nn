===============================================================================

Natural Language Processing
Professor Collins
Homework 4 - Programming
Frankcarlos Castro (fc2518)
===============================================================================
This project was written in python 3.5.3
The trained models for each part is stored in the src folder:
- part1: trained.model
- part2: trained2.model
- part3: trained3.model 

The submitted code is ready to run part 3.
Read on and see code comments for necessary changes to run parts 1 and 2.

Part 1
------
In the src Folder run: python3 src/depModel.py trees/dev.conll outputs/dev_part1.conll
If there is no 'trained.model' in the src folder, the network is trained and the resulting model
is stored in src/trained.model 
The stored model directory is written within depModel.py as an option
The change needed for part 2/3 for this trained model is commented within depModel.py

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
In the src Folder run: python3 src/depModel.py trees/dev.conll outputs/dev_part2.conll
Again, in depModel you can specify which trained model to use or the path to store the resulting model
For this part the hidden_dim option in depModel.py is changed from 200 to 400 (commented in depModel.py)

1. Trained my model for 7 epochs, now changing the hidden_dim to 400 instead of 200
   Ran the decoder with input file trees/dev.conll and output file outputs/dev_part2.conll

2.  Ran this script: python3 src/eval.py trees/dev.conll outputs/dev_part2.conll
    to get the unlabled and labeled dependency accuracies.

    I received the following values:
        Unlabeled attachment score 82.55
        Labeled attachment score 79.44

3.  Ran the decoder again on blind test file (trees/test.conll)
    Output content to outputs/test_part2.conll

4.  The accuracy stayed fairly close to that of part 1 but does see a slight improvement.
    After doubling the hidden input dimension, my model trained noticably slower.
    I believe the slight improvement is due to the increase number of hidden neurons.
    Due to this, the network can fit the training data with higher complexity and benefit more from neuron codependency.
    In essence, the network has more data to base its computations during training. 
    However, after a certain point, this would lead to overfitting.  

Part 3
------
In the src Folder run: python3 src/depModel.py trees/dev.conll outputs/dev_part3.conll
The changes needed to use dropout are commented within network.py 
(adding a dropout layer between the 2 hidden layers in the build_graph function)

For this part I tried the following changes in the setup of the network:
- hidden_dim 300, epoch 7, minibatch 500
- hidden_dim 200, epoch 7, minibatch 1500
- hidden_dim 200, epoch 7, minibatch 800
- hidden_dim 200, epoch 10, minibatch 1000

The least effective model was trained using 10 epochs, this is most because by training for more epochs, 
I begin overfitting the training data and perform less effectively on unseen data.
The above attempts didn't outperform parts 1 and 2 so I began looking into using dropout during training
Here I tried the given settings (hidden_dim 200, epoch 7, minibatch 1000) along with adding a dropout layer
between the two hidden layers. This change is commented within src/network.py 
I tried the following dropout rates within the dropout layer:

- dropout rate 0.5
- dropout rate 0.3
- dropout rate 0.1

Finally I was able to outperform part 1 and 2 using a dropout rate of 0.1
I received the following values:
    Unlabeled attachment score 83.48
    Labeled attachment score 80.23

This improvement is due to dropout reducing overfitting by ignoring certain neurons (dropping with rate 0.1)
and lowering the codependency between neurons thus improving the individual strength of a given neuron 
and generalizing better to unseen data.
