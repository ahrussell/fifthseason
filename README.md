fifthseason
===========

Project that uses pattern matching via suffix trees to replicate musical style via Markov chains.

This takes .json file(s) of a list of notes (see the files in the music directory) and returns a json object of a new list of notes.

Credit to [sreevisakh](http://github.com/sreevisakh) for the Suffix Tree code.

Also note that this project is biased toward the treble clef at the moment as I am a violinist, and built the program from that perspective first, without generalizing further.

The code is a bit messier than I would like it as it was hastily written as part of final project for a class in the study of Math and Music.

See example usage in ```examples.py```.  After running the script, you can view the output in sheet music form in ```output/fifthseason.html``` which uses the Vexflow library for formatting.