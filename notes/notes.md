# What are tokens?
Tokens are sequences of characters, The process of breaking down the words into these sequences are called tokenization.
The split characters may be a full word or even 3/4 of a word. It is a sequences of characters frequently seen together.
For example, Gen|arative. The Model will predict the most likly occuring word Genarative
If we increase the token window to capture full words or full sentences then the vocab of the model will not be agile any change in the sequence of the word will lead to unwanted results for example, hey, how are you? vs hey how are you! will be different.
Very small token window may lead to capturing of context harder
Predicting the next word is easier than increasing the sentence. 

Tokenizer Playground: https://platform.openai.com/tokenizer
Same tokens will have same token IDs.
Leading Spaces are also considered as tokens.
Puncuations are also tokens.
Emojis are converted into bytes.
Frquently occuring numbers or words may be grouped together like
123 456 etc
Commonly occuring token will have lower Id number.
Starting words token will not capture space. What am I doing. What is capture without trailing space indicating a questions.
leading words token will capture spaces. I am fine. <space>fine is captured as token means it is a statement.
What, <space>what and <space>What will have different token IDs. 

Pricing is based on the # of tokens we consume. Larger token means more pricy models.
Input and output tokens are charged seperately.

Context window is how much text at a time it can process without failure.
128K