ideas & problem:

i want a way in which to track progress, or perhaps analyze
songs that I play.

Ideas:
1. Legato and Staccato measurements: It's kind of hard to say how to "measure" these, as in how do
you measure how Legato a piece is played?

2. Given a collection of midi files that are of the same piece, is it possible to choose which one
is the best?

3. Similarly, given a collection of midi files of the same piece, can you average them out to create
a single midi file that represents the average of them?

4. Over the top idea: imagine a neural net that can accurately classify whether a midi file is a song or not.
Then you have another neural net that tries to "trick" the other, by generating a midi file with sounds, and
trying to test whether the other NN can tell if its a song or not -> an AI that can self produce music

-exceptions to this: one is considered a valid song? What features would you extract for training?

5. Perhaps you can analyze where the hardest parts are in a song? perhaps like where the largest intervals are,
where the notes are played in quick succession.
-but then, what is considered "hard?"

6. a way in which you can take a midi file and smooth it, to have notes and chords released precisely when they
need to

7. A way in which you can detect patterns. Perhaps then, you can display sequence of patterns. As in, suppose
there is a piece of music if pattern ABBA. I want a way to detect this pattern, then print it.

8. midi file -> sheet music? This would be a lot of work, and i'd have to think about it

9. Take the frequency of notes played -> Denalex Orakwue's idea

Things to do:
need to make a main entry point with arguments->
arguments are based on which analysis you want to perform->
based on choice, execute the analysis

Known Errors -> chord detecting can get messed up to overlapping notes, will fix