"The Tale of the Cat Burglar" by Jared Bronen

The maximum score is 12.

The Van is a room.
There is a cupcake in the Van. The cupcake is edible.
The description of the Van is "The haggard, beat-up van you're in is parked outside the Willingsworth mansion. You, my friend, are a cat burglar, which is to say you burgle cats. To the south is the mansion lobby."
The description of the cupcake is "An old cupcake with chocolate frosting and some sprinkles that probably weren't always green... you think the smell of the van might actually be coming from the cupcake. 'Gross', you mumble to yourself."
Instead of eating the cupcake:
	end the story finally saying "I recommend examining something before you eat it!"
	

The Main Lobby is a room. It is south of the van.
The description of the Main Lobby is "You've entered the beautiful, distinguished lobby of the Willingsworth mansion. Chandieliers and family photos featuring a loving, elderly couple and their cats decorate the room. A set of stairs leading to the south leads up to the second floor. To the west is a locked door. To the east is the kitchen."

The closet is a room. It is west of the Closet Door. The description of the closet is "A closet filled with some old jackets. 'It smells like old jackets in here,' you think. To the west is the Main Lobby."
The Closet Door is a door. It is locked. It is west of the Main Lobby and east of the closet. The Small Key unlocks the Closet Door.
The Cat named Clyde is in the closet. "The cat exclaims, 'Oh hey there you handsome young fella! I hope you don't steal me or nothing I got myelf I nice little cat life in this here mansion. My owners sure do love me 'n' such! Wheeeee!'"
After taking the Cat named Clyde for the first time:
	increase the score by 1; 
	say "Great, another burgled cat. You are fine, honorable young man/woman/person outside of the binary gender social construct."
	

The kitchen is a room. It is east of the Main Lobby. The description of the kitchen is "A very nice kitchen. Electric stoves, and more pictures of happy old people hugging happy old cats are scattered throughout. A couple of shelves with nothing interesting inside. To the west is the Main Lobby. To the south is the TV Room."
The refrigerador is a closed openable container in the kitchen. It is not portable.
The piece of meat is in the refrigerador. 
The piece of meat is edible. The description of the piece of meat is "Definitely rotten. Small chunks of dark green mold and bacteria bubble in the small crevices of the meat. Probably not good for you"

Instead of eating the piece of meat:
	end the story finally saying "I recommend examining food before it eating it!"

The TV Room is a room. It is south of the kitchen. The description of the TV Room is "You stand on top of a green carpet with red stains. 'Wine?' you ask yourself. You see the TV's and want to relax. You see a crate behind the Cracked TV. To the North is the Kitchen. To the west is the Living Room."

Crate is an open container in the TV Room. It is not portable.
A Cat named Kyle is a thing.


canSingWell is a number that varies. canSingwell is 0.
The Tube TV is a device in the TV Room. It is switched off. It is not portable.The Cracked TV is a device in the TV Room. It is switched off. It is not portable.
After switching on the Tube TV for the first time:
	increment canSingWell;
	say "You turn on the Tube TV. 'Singing for Fictional Thiefs' plays. You keep watching, and after a little while start practicing along with the program. You have learned the art of song."

Instead of singing:
	if canSingWell is 1, say "You are a true master of voice and song.";
	if canSingWell is 0, say "You could use some lessons."


After switching on the Cracked TV for the first time:
	Move the Cat named Kyle to crate;
	Say "You turn on the Cracked TV. A program titled, 'The Universe of Animals' is on. You sit down to watch it, and a segment on big cats comes up. After a commercial break, a lion roars across the screen. You hear a purr from behind the television."

After taking the Cat named Kyle for the first time:
	increase the score by 1;
	Say "Good job, you are now responsible for taking care of this text-only cat."

The Living Room is a room. It is west of the TV Room. The description of the Living Room is "Another fine room filled with sofas, couches, and big comfortable chairs. You appreciate how nice the lighting is in here. You take a look at one of the lamps. 'Ikea!' you say to yourself, 'so many wonderful products.' In the middle of the room, however, is a large, angry dog. It growls at you, threatening you not to come any closer. To the east is the TV Room. To the West is the library."
The dog is an animal in the living room. The dog is either dead or alive. The dog is alive. The description of the dog is " 'Good god,' you say to yourself, 'that is one mean looking dog!' The dog does not take its eyes off you. You decide it best not cross while it is so focused and intent on tearing you apart. If only you had something you could use for a distraction."
The Metallic Crate is a container in the Living Room. It is fixed in place.
A Cat named Drangus is a thing.

The Dead Dog is an animal. The description of the Dead Dog is "A dead (murdered) dog. You murdered this dog by feeding it that meat, you monster."

Instead of giving the piece of meat to the dog:
	remove the dog from play;
	move the Dead Dog to the Living Room;
	move the Cat named Drangus to the Metallic Crate;
	say "The dog gives a whimper and falls to it side. You feel bad, but not bad enough to stop ransacking this home of its cats. But wait! You hear a small purr from inside the empty the crate. Maybe something hiding from the dog?"
	
After taking the Cat named Drangus for the first time:
	increase the score by 1;
	say "Another cat you will either love and cherish for the rest of your life or sell on thet text-only cat black market."

The Library is a room. It is west of the Living Room. The description of the Library is "You're surrounded by books of every size and color. The smell of old books is comforting to your nose but mostly your brain. To the east is the Living Room."
The Book is a thing in the Library. The description of the book is "A Book of Poems by Brooker Tree Drewitt."

The Small Key is a thing. The description of the small key is "A key that is not large."
After taking the book for the first time:
	move the small key to the library;
	say "You are now a master of poetry. 'This might come in handy later,' you think. You see a small key under the book!"

The Second Floor Lobby is a room. It is up from the Main Lobby. The description of the Second Floor Lobby is "You have entered the Second Floor Lobby. You hear voices coming from the East, South, and West. To the East is the master bedroom. To the west is the Second Floor Closet. To the South is the Vault Room. You think about going in there (who wouldn't keep cats in their vault room?)."

The Master Bedroom is a room. It is east of the Second Floor Lobby. The description of the Master Bedroom is "The Master Bedroom is quite possibly the single fanciest room you've had the privelage of standing in. Enormous murals of the Willingsworth couple and their cats adorn the walls. The Bed, sized 'God-King' is a behemoth piece of furniture in the center of the room. In the Master Bedroom is a man... A man carrying a bag... A bag full of cats! You have encountered a 2nd Cat burglar. He's wearing a t-shirt that says, 'I sure do love pastries and eat them without looking at them regularly.' You have some options how to approach this one: kill the thief and take his cats, ask him about cats, or simply walk away. Up to you. But remember, violence is not always the answer. But sometimes it is.".
Second Cat burglar is a man in the Master bedroom. The description of the Second Cat burglar is "A Handsome young fellow. A lot of stains on his shirt though. He's actually really dirty. Doesn't seem to have the greatest sense of hygiene."

The Dead Cat burglar is a thing. It is not portable. "A man who you chose to murder in order to steal more cats. What a life you live."
A Cat named Diane is a thing. A Cat named Staci is a thing.

Instead of giving the cupcake to the Second Cat burglar:
	remove the Second Cat burglar from play;
	move the Dead Cat burglar to the Master Bedroom;
	move Cat named Diane to the Master Bedroom;
	move Cat named Staci to the Master Bedroom;
	say "You tricked him. He ate the meat. He is dead! Out from his cat-bag crawl two cats, Diane and Staci (that's with an i, mind you!)"

After asking the Second Cat burglar about "cats":
	say "The second cat burglar looks you in the eyes. 'I would steal to cats to feed my family... If I had a family! Alas I steal the cats, sell the cats, and use the money to buy food that to eat myself that is not made out of cats!' You are weirded out."

After taking the Cat named Diane for the first time:
	increase the score by 1;
	say "Another cat in the bag (literally)"
	
After taking the Cat named Staci for the first time:
	increase the score by 1;
	say "This cat will serve you well...somehow. You will figure that out later."
	


The Second Floor Closet is a room. It is west of the Second Floor Lobby. The description of the Second Floor Closet is "A closet filled with old people's clothes. You like the style quite a bit and look forward to your time spent as an old person. 'I should see a therapist for a lot of different reasons,' you think."
Mrs Willingsworth is a woman in the Second Floor Closet. The description of Mrs Willingsworth is "The heiress the Willingsworth fortune. This family made their money in arms profiteering. Who knew there was so much money in prostethics. She looks frail, but carries a big smile on her face. She asks you, 'Would like me to read you a poem?' You say, 'sure.' 'But I don't know any poems!'"

A Cat named Brian is a thing.
Instead of giving the book to Mrs Willingsworth:
	move Cat named Brian to the Second Floor Closet;
	say "You give Mrs. Willingsworth your book of poems. 'Let me find my favorite.' You wait patiently as she flips through each page, licking her very dry fingers for every turn. Finally, she stops. 'Who Shalt Be Punished? by Brooker Tree Drewitt,' she reads, [line break] [line break] 'Oh ye unfaithful, sly, sickly man, who hath lept from the high path towards God. [line break] Here you lie, a snake slivering towards greed and finite, fleeting happiness, unable to fathom the grace of God's light. [line break] What is it the bends the minds of men towards sin? [line break] Can we define a precursor for evil. [line break] We do not know. But in the meantime, respect other people's property.' [line break][line break] You hear a soft meow from behind an old jacket; it must have liked the poem."

After taking the Cat named Brian for the first time:
	increase the score by 1;
	say "You are going to be rich! [line break] if you ever get around to changing your name to Richard."
	

The Guest Bedroom is a room. It is south of the Second Floor Closet. The description of the Guest Bedroom is "The guest bedroom is small and desolate. Something about this room deeply upsets you. Maybe it reminds you of your own upbringing. Standing in the room is Mr. Willingsworth, who manages the Willingsworth fortune."

Mr Willingsworth is a man in the Guest Bedroom. The description of Mr Willingsworth is "A man of great statue. His prowess in the sales of artificial limbs are simply unrivaled. His only weakness, a deep affectionate love for his wife and his cats. Without either of them, he would no longer be able to carry on the life-changing work he continues to do to this very day! You think about asking him about the vault room."

After asking Mr Willingsworth about "vault room":
	say "Mr. Willingsworth gives you a stern look. 'I see you wish to enter the vault room,' he sighs, 'that's fine I suppose. We need someone to cheer the guard up. Are you any good at singing? Try singing him a song maybe... Only if you're good though! If you aren't the dude might kill ya! If you are good though, he might have something for ya.'"
	
After asking Mr Willingsworth about "the vault room":
	say "Mr. Willingsworth gives you a stern look. 'I see you wish to enter the vault room,' he sighs, 'that's fine I suppose. We need someone to cheer the guard up. Are you any good at singing? Try singing him a song maybe... Only if you're good though! If you aren't the dude might kill ya! If you are good though, he might have something for ya.'"

The Vault Door is a Door. It is south of the Second Floor Lobby. It is north of the Vault Room. It is locked. The description of the Vault Door is "A heavy door with the inscription 'NOTHING OF VALUE IN HERE'".

The Vault Room is a room. It is south of the Vault Door. It is east of the Guest Bedroom. The description is "You have made it to the vault room. This is it. You hear very loud meowing coming from inside the vault. 'Must be a whole goddamn litter in there,' you think. You approach the guard cautiously. The two of you lock eyes."
The Guard is a man in the Vault Room. The description of the Guard is "A bear of a man. But you sense a deep sadness in his eyes. You ask him if he needs anything, a tissue perhaps. He says, 'No. Nothing really. I just wish someone could cheer me up. But no one knows how to sing, at least sing well!"
The Main Vault is a locked, closed container in the Vault Room. The Bag of Cats is a thing in the Main Vault.
The description of the Main Vault is "A large, iron vault. The meowing coming from it is loud and intense."
The description of the Bag of Cats is "A bag filled with cats. 'Jackpot!' you think."

Instead of singing in the Vault Room:
	if canSingWell is 0, say "The guard is infuriated with your terrible voice. He screams and writhes in his fury. You stand still, locked from fright. He pulls out a dagger. You try to run for the door, but are not quick enough.";
	if canSingWell is 0, end the game in death;
	if canSingWell is 1, increase the score by 6;
	if canSingWell is 1, say "The guard is deeply moved by your masterful voice. Your rendition of 'Happy Birthday' is one of the best renditions of all time. He unlocks the Main Vault, handing you the bag of cats. You look inside. 6 of the finest cats you've ever seen! 'This is treasure,' you think to yourself. You can leave the Willingsworth mansion happy and rich.";
	if canSingWell is 1, end the game in victory.




