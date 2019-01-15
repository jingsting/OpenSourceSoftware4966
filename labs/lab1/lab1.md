# Two ideas about answering questions in a helpful way:
1. Make sure you are clear with the question, ask if you are not clear with the question
2. Briefly summarize the answer if its relatively long

# From the readings:
I think it is unjust that the matter ended with Jesse paying all he has to the RIAA. Jesse simply modified the search engine, making it easier to use. Jesse is not the person who build the engine. Jesse modified the engine not necessarily in order to help with pirating. He didn't intend to do anything with music. It would be nice if people can group up and fight against these attacks from organizations like RIAA. People like Jesse need to beware that things like this could happen and protect themselves as much as they can. Actions from organizations like this stifles technological progress.

# Linux
![Alt text](/labs/lab1/lab1resource/lab1_directory.png?raw=true "Title")
![Alt text](/labs/lab1/lab1resource/lab1_man_tree.png?raw=true "Title")

# Regex
![Alt text](/labs/lab1/lab1resource/lab1_regex.png?raw=true "Title")
![Alt text](/labs/lab1/lab1resource/lab1_beginner.png?raw=true "Title")
![Alt text](/labs/lab1/lab1resource/lab1_tutorial.png?raw=true "Title")

# Blockly
![Alt text](/labs/lab1/lab1resource/lab1_blockly.png?raw=true "Title")

# Reflection
Open source software of choice: ODAS (https://github.com/introlab/odas)
ODAS stands for Open embedded Audition System. ODAS is a free and open source library dedicated for sound source localization, tracking, separation and post-filtering.
I would want to add a function that gets output from microphone arrays and apporximate a estimated location of the sound source.
To do this I will fork the current repository of ODAS and modify the program to be able to identify whether itself is the server from configuration file.
I will create a separate file for the the estimation algorithm.
The server will receive outputs from clients and run the added algorithm and output in a different socket.