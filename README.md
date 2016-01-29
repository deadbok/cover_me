Cover me.
=========

This is a Markov chain generator seeded with about 16000 lines of David Bowie
lyrics.

Why?
----

When i was young and my heart was an open book, I used to write something I 
defined as poetry. Life and my world view has since become way more complex, to
the degree that I have not written more than scattered lines for many years, for
fear that I might oversimplify things.

When David Bowie died I had the urge to write something to commemorate him,
but that would be entering even more dangerous ground. A friend of mine, had
just discovered Markov chain generators, and told me about them. I knew these,
but had newer implemented one. Thinking of David Bowie's use of cut up technique,
an idea formed, as to how I could get around writing something that made me
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
that through the use of cut up and human love, might actually end up being
quite readable, sometime even touching funny and beautiful.

Templates.
----------

Templates may be used to control the output of the Markov generator. The 
templates are text files. There are a few command tokens, to control the
generator. Anything that is not recognised as a command is copied to the output
file.

Command syntax:

 * ``{n}``: Use the Markov to insert ``n`` words.
   

Output examples.
----------------

READEME.md (without examples ;-) ):

	cover me again will kill for walking through
	me heard him she'll love her meat
	possibilities it all
	babies kissing all them i guess
	this honey - we wrote
	preening ourselves in heaven lies between us
	occurred that plane come
	is valuable
	a lie-high-high-high
	markov chain strong
	generator seeded sha la la la,  la la a duck's ass can i came my price for everyone
	with that proved the truth
	about charlie he gazes to god on grime goodwill and tommy's learned to you
	16000 numbers alone
	lines of the
	of guy
	oh    oh oh yeah!  (yeah
	david what is best ways ever know
	bowie lyrics ferny coach
	kill another you
	creeping pouncing shoutin' screamin'
	why it all but selling it could've been
	when he('s fast like every - fortune evasive and tired old fool
	ill with hard enough ain't that rainbow secrets i liked you you're dead - crying inside
	i love
	trendy rush of yore
	hit 'em where things loving life out over town
	was she walks
	cha-charlie a horrid cassette
	young girl my contact black
	shirley/charlie films that it's pictured on thin men around
	and out to save
	details following
	my baby doll
	heart oo-oo-oohh
	collects the fire
	was if they tumble from ripping off with pleasure
	an horror of history
	all-time low
	open up your naked eyes
	explain what did your parents' home
	village tied up
	book in and
	smiles on heat
	silly boy that neat
	dies on him
	i listen to
	guevara drove a shotgun
	used what this

bowie.txt:
	
	i spoke into town just an inmate needs a party on everybody's wall
	slides down ooo-ah-ah
	frangipani scents the traffic lights
	will move like candy-floss
	outrageous he danced with you
	meaningful teenage wildlife oh-oh-oh-ohh
	whop whop
	wednesday august 18th
	in lies and wind blows but whatever lies alone
	always been writing just dumb
	tourist pals
	miss you little sally may god's green world
	yo-yo wooh oh
	you turned at all    
	there pleading
	day breaks a street
	way and how long ago
	is shining so hard as babe and who's this greedy
	a figure sitting by these pieces are hungry mama
	gap jump in my
	why not tomorrow
	napalm to fall
	did i picked on poacher's hill
	surprise yourself
	stench was no religion
	bramble thorn
	dean was positively queer
	i got drama can't buy it isn't that she's doesn't recall how long to spare
	spelt p-a-n-i-c
	not take hold some are
	hear what of all kinds of the victim
	shine bleed like i'm stiff on bended knee
	the sober philistine
	implosion lovers' story
	libbilubbing litso-fitso
	martian blues away
	law earthlings on smoke today
	fatales emerged from writing just an unwanted toy
	moondust cover you flying in rule
	mess with their fingers broken
	will care someone new
	cover the fairground
	sneak from sin then your eye
	meets the glamorous
	you dreams was layin' on mars
	keeps on wings
	after all were dead ears
	happened all so sincere
	fragile champion boys
	mist in mine
	stunning you never give
	making sure i watch her

Freerunning:
	
	424 hello
	oxford town and watching from hell
	cup of breath anyway
	shouting about
	creep with people too long
	sir no reason
	understands him
	macabre shrine of grand delusion you care
	with leon
	he's told of wisdom
	tessie turns tricks with folk who is made up
	self control
	reveal what - though you was not so swishy in solemn perverse serenity wondrous beings chained to crush the crops of um in space
	christ and hundreds of rich girl
	popular musics
	cross-legged on dreaming my my tongue twisting storm will have splash
	eine chance
	tossing and cried
	secure again
	legendary curtains on white
	whale of manhattoes
	reject you don't wanna come through
	special place to yourself to myself
	goodnight siobhan
	resigned she moved toward the frangipani scents the zombies that leon
	herald loud as only want knowledge i started the silver fox now he uttered some clothes always looking satellites  
	kneel and told of crime
	callout raising hands
	attack your mile
	taking my wife i dream reality
	hitting an ice-cream in for i've had another way he he yells to bleed
	stimulating encouragement - but thin ice
	joe the far far
	scalding face
	main feature ah
	killed her escort asked why but cooking leaves the house
	soldier's spring went
	nah nah
	only destroy i gossip my burning pit of flowers
	bit and green
	praise to fool
	dresses silk blouse
	earth -
	line filing past the doctor
	shouting about
	yards at silver wings
	bended knee
	august 18th
	crops of one and i'll 