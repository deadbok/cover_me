Cover me.
=========

This is a Markov chain generator seeded with about 16000 lines of David Bowie
lyrics.

Why?
----

When i was young and my heart was an open book, I used to write something I 
defined as poetry. Life and my world view has since become way more diverse, to
the degree that I have not written more than scattered lines for many years, for
fear that I might oversimplify things.

When David Bowie died I had the urge to write something to commemorate him,
but that would be entering even more dangerous ground. A friend of mine, had
just discovered Markov chain generators, and told me about them. I knew these,
but had newer implemented one. Thinking of David Bowie's use of cut up technique,
an idea formed as to how I could get around writing something that made me
feel narrow minded and stupid. Let the computer do it, it is basically stupid
anyway.

How?
----

``wstat.py`` creates a dictionary of word associations and number of
occurrences needed for the generator. Since I dare not include the actual lyrics
of David Bowie's songs, this program saves the words and statistics in JSON
format, that the Markov chain generator can digest.

``words.json`` is the output of ``wstat.py`` chewing through a fairly large
set of David Bowie lyrics (and a Syd Barret song, that I could not persuade
myself to remove).

``markov.py`` is the actual Markov chain generator, that outputs something
that with a little love, might actually end up being
quite readable, sometime even touching, funny, and beautiful.

Templates.
----------

Templates may be used to control the output of the Markov generator. The 
templates are text files. There are a few command tokens, to control the
generator. Anything that is not recognised as a command is copied to the output
file.

Because of the way I handle newlines there is a quirk when starting a template.

 * If there is no newline at the beginning of the template, the first block
   will not be capitalised.
 * If there is a newline at the beginning of the template, the first block
   will not be capitalised.

Command syntax:

 * ``{n}``: Use the Markov generator to insert ``n`` words.
 * ``{!n}``: Same as above, but newlines are not allowed.
 * ``{.n}``: Use the Markov generator to insert ``n`` words, capitalise first letter.
 * ``{-n}``: Copy a Markov generated block ``n`` from the top.
   

Output examples.
----------------


**Welcome to the world**

	Welcome to the world
	Welcome to the baby,
	You gotta have
	Let him loose, chi child
	
	Yourself
	Deafen me
	Absolute
	
	Welcome to the world
	Welcome to the funhouse
	
	Away our heads
	Mouth
	Saviour machine
	Work's down
	Is the possibilities it


**Welcome to the world**

	Welcome to the world
	Welcome to the dreamers
	
	And your window
	All is a suffragette city
	
	Spring went
	Shopsdown
	
	Welcome to the world
	Welcome to the wagon
	
	It's only dancing
	Destruction as the dames
	Leisure
	The way into gloom


**Falling in**

	Dredging the pain, in vain sheets on refugees changed
	Say he pinned you, might have to touch the bushland over now we
	Tip get papa chains
	Beggar's face show respect even i am
	Daydreams made of hit him right on garbo's
	
	Sailor who would they don't grab that
	Fingerprints will come quick on high
	Vain showbiz anyway beautiful baby baby got, Moon
	Knowing right from day falling in you sleep!
	
	Sweeping over stiles woman, now tomorrow calls me to the
	Nightclubbing we're gonna pay, and
	Loneliness in town crazies with name york's,
	Reelin' like daisies, lie behind my day after today
	Romantic as forever i'm glad i've
	
	Sailor who would they don't grab that
	Fingerprints will come quick on high
	Vain showbiz anyway beautiful baby baby got,Moon
	Knowing right from day falling in you sleep!
	
	Devil breaking!
	Yards at!
	Utter destruction!


**Good again for**

	Enemy dropped a god-awful small enough to her
	Threading daisies lie low with their eyes
	Flipping time in a look into the flame filled sunset
	Bullshit from my head up there was so enticing to face, frightening, do-doh
	Elvis is my god
	Wanking to their whiskey voice croaked
	Dot marks


