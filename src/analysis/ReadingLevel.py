#import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk import pos_tag
import re
from analysis.Statistics import Statistics
from analysis.Metrics import Metrics
from analysis.Frequency import Frequency
#import json
import sys

class ReadingLevel:
                
    def automatedReadabilityIndex(self, text):
        result = Statistics()
        sentences = sent_tokenize(text)
        result.sentences = len(sentences)
            
        #p = re.compile('^[^!#$%&\'()*+,-./:;<=>?@\\^_`{|}]*$')
        p = re.compile('[a-zA-Z]')
            
        result.words = 0
        words = word_tokenize(text)

        for word in words:
                match = p.match(word)
                if match:
                    result.words += 1
        
        result.chars = 0
        for word in words:
            for char in word:
                match = p.match(char)
                if match:
                    result.chars += 1
         
        #result.calculateLevel()
        
        #FIXME - make it a try catch with a time out
        m = Metrics.produceFrom(text)
        result.sentences = m.sentences()
        result.calculateLevel()
        
        result.sentences = str(result.sentences)
        result.clauses = str(round(float(m.clauses()), 3))
        #print('\n\nsent: ', result.sentences, '\n\n', type(result.sentences))
        #print('\n\nclauses: ', type(result.clauses))
        result.clausesPerSent = m.clausesPerSentence()
        
        f = Frequency()
        result.avg_frequency = round(f.find_avg_freq(text), 3)
        
        result.final_reading_level = round(float(result.clausesPerSent) * float(result.avg_frequency), 3) * 100
        
        return result
    
if __name__ == '__main__':
    '''
    result = ReadingLevel().automatedReadabilityIndex(text)
    print(result)
    print(result.toJSON())
    print(pos_tag(text.split()))
    print()
'''
    #winnie = 'In after-years he liked to think that he had been in Very Great Danger during the Terrible Flood, but the only danger he had really been in was the last half-hour of his imprisonment, when Owl, who had just flown up, sat on a branch of his tree to comfort him, and told him a very long story about an aunt who had once laid a seagull\'s egg by mistake, and the story went on and on, rather like this sentence, until Piglet who was listening out of his window without much hope, went to sleep quietly and naturally, slipping slowly out of the window towards the water until he was only hanging on by his toes, at which moment, luckily, a sudden loud squawk from Owl, which was really part of the story, being what his aunt said, woke the Piglet up and just gave him time to jerk himself back into safety and say, "How interesting, and did she?" when — well, you can imagine his joy when at last he saw the good ship, Brain of Pooh (Captain, C. Robin; 1st Mate, P. Bear) coming over the sea to rescue him.'
    #age = 'Therefore, whenever anything happened that Mrs. Archer wanted to know about, she asked Mr. Jackson to dine; and as she honoured few people with her invitations, and as she and her daughter Janey were an excellent audience, Mr. Jackson usually came himself instead of sending his sister. If he could have dictated all the conditions, he would have chosen the evenings when Newland was out; not because the young man was uncongenial to him (the two got on capitally at their club) but because the old anecdotist sometimes felt, on Newland\'s part, a tendency to weigh his evidence that the ladies of the family never showed.'
    default = 'The rule of rhythm in prose is not so intricate. Here, too, we write in groups, or phrases, as I prefer to call them, for the prose phrase is greatly longer and is much more nonchalantly uttered than the group in verse; so that not only is there a greater interval of continuous sound between the pauses, but, for that very reason, word is linked more readily to word by a more summary enunciation. Still, the phrase is the strict analogue of the group, and successive phrases, like successive groups, must differ openly in length and rhythm. The rule of scansion in verse is to suggest no measure but the one in hand; in prose, to suggest no measure at all. Prose must be rhythmical, and it may be as much so as you will; but it must not be metrical. It may be anything, but it must not be verse.'
    #test = 'Gaily bedight a galant knight in sunshine and in shadow had journeyed long singing a song in search of El Dorado. But he grew old, this knight so bold and over his heart a shadow fell as he found no spot of ground that looked like El Dorado.'
    winnie1 = 'In after-years he liked to think that he had been in Very Great Danger during the Terrible Flood, but the only danger he had really been in was the last half-hour of his imprisonment, when Owl, who had just flown up, sat on a branch of his tree to comfort him, and told him a very long story about an aunt who had once laid a seagull\'s egg by mistake, and the story went on and on, rather like this sentence, until Piglet who was listening out of his window without much hope, went to sleep quietly and naturally, slipping slowly out of the window towards the water until he was only hanging on by his toes, at which moment, luckily, a sudden loud squawk from Owl, which was really part of the story, being what his aunt said, woke the Piglet up and just gave him time to jerk himself back into safety and say, \"How interesting, and did she?\" when — well, you can imagine his joy when at last he saw the good ship, Brain of Pooh (Captain, C. Robin; 1st Mate, P. Bear) coming over the sea to rescue him.'
    winnie2 = 'And then he had a Clever Idea. He would go up very quietly to the Six Pine Trees now, peep very cautiously into the Trap, and see if there was a Heffalump there. And if there was, he would go back to bed, and if there wasn\'t, he wouldn\'t. So off he went. At first he thought that there wouldn\'t be a Heffalump in the Trap, and then he thought that there would, and as he got nearer he was sure that there would, because he could hear it hefalumping about it like anything. \"Oh dear, oh dear, oh dear!\" said Piglet to himself. And he wanted to run away. But somehow, having got so near, he felt that he must just see what a Heffalump was like. So he crept to the side of the Trap and looked in And all the time Winnie-the-Pooh had been trying to get the honey-jar off his head. The more he shook it, the more tightly it stuck. '
    winnie3 = 'There was no wind to blow him nearer to the tree, so there he stayed. He could see the honey, he could smell the honey, but he couldn\'t quite reach the honey. After a little while he called down to you.  \"Christopher Robin!\" he said in a loud whisper. \"Hallo!\" \"I think the bees suspect something!\" \"What sort of thing?\" \"I don\'t know. But something tells me that they\'re suspicious!\" \"Perhaps they think that you\'re after their honey.\" \"It may be that. You never can tell with bees.\" There was another silence, and then he called down to you again. \"Christopher Robin!\" \"Yes?\" \"Have you an umbrella in your house?\" \"I think so.\" \"I wish you would bring it out here, and walk up and down with it, and look up at me every now and then, and say \'Tut-tut, it looks like rain.\' I think, if you did that, it would help with the deception which we are practising on these bees.\" Well, you laughed to yourself, \"Silly old Bear!\" but you didn\'t say it aloud because you were so fond of him, and you went home for your umbrella.'
    green1 = 'I AM SAM. I AM SAM. SAM I AM. THAT SAM-I-AM! THAT SAM-I-AM! I DO NOT LIKE THAT SAM-I-AM! DO WOULD YOU LIKE GREEN EGGS AND HAM? I DO NOT LIKE THEM,SAM-I-AM. I DO NOT LIKE GREEN EGGS AND HAM. WOULD YOU LIKE THEM HERE OR THERE? I WOULD NOT LIKE THEM HERE OR THERE. I WOULD NOT LIKE THEM ANYWHERE. I DO NOT LIKE GREEN EGGS AND HAM. I DO NOT LIKE THEM, SAM-I-AM. WOULD YOU LIKE THEM IN A HOUSE? WOULD YOU LIKE THEN WITH A MOUSE? I DO NOT LIKE THEM IN A HOUSE. I DO NOT LIKE THEM WITH A MOUSE. I DO NOT LIKE THEM HERE OR THERE. I DO NOT LIKE THEM ANYWHERE. I DO NOT LIKE GREEN EGGS AND HAM. I DO NOT LIKE THEM, SAM-I-AM. WOULD YOU EAT THEM IN A BOX? WOULD YOU EAT THEM WITH A FOX? NOT IN A BOX. NOT WITH A FOX. NOT IN A HOUSE. NOT WITH A MOUSE. I WOULD NOT EAT THEM HERE OR THERE. I WOULD NOT EAT THEM ANYWHERE. I WOULD NOT EAT GREEN EGGS AND HAM. I DO NOT LIKE THEM, SAM-I-AM.'
    green2 = 'WOULD YOU? COULD YOU? IN A CAR? EAT THEM! EAT THEM! HERE THEY ARE. I WOULD NOT, COULD NOT, IN A CAR. YOU MAY LIKE THEM. YOU WILL SEE. YOU MAY LIKE THEM IN A TREE! I WOULD NOT, COULD NOT IN A TREE. NOT IN A CAR! YOU LET ME BE. I DO NOT LIKE THEM IN A BOX. I DO NOT LIKE THEM WITH A FOX. I DO NOT LIKE THEM IN A HOUSE. I DO NOT LIKE THEM WITH A MOUSE. I DO NOT LIKE THEM HERE OR THERE. I DO NOT LIKE THEM ANYWHERE. I DO NOT LIKE GREEN EGGS AND HAM. I DO NOT LIKE THEM, SAM-I-AM. A TRAIN! A TRAIN! A TRAIN! A TRAIN! COULD YOU, WOULD YOU ON A TRAIN? NOT ON TRAIN! NOT IN A TREE! NOT IN A CAR! SAM! LET ME BE! I WOULD NOT, COULD NOT, IN A BOX. I WOULD NOT, COULD NOT, WITH A FOX. I WILL NOT EAT THEM IN A HOUSE. I WILL NOT EAT THEM HERE OR THERE. I WILL NOT EAT THEM ANYWHERE. I DO NOT EAT GREEN EGGS AND HAM. I DO NOT LIKE THEM, SAM-I-AM. SAY! IN THE DARK? HERE IN THE DARK! WOULD YOU, COULD YOU, IN THE DARK? I WOULD NOT, COULD NOT, IN THE DARK. WOULD YOU COULD YOU IN THE RAIN? I WOULD NOT, COULD NOT IN THE RAIN. NOT IN THE DARK. NOT ON A TRAIN. NOT IN A CAR. NOT IN A TREE. I DO NOT LIKE THEM, SAM, YOU SEE. NOT IN A HOUSE. NOT IN A BOX. NOT WITH A MOUSE. NOT WITH A FOX. I WILL NOT EAT THEM HERE OR THERE. I DO NOT LIKE THEM ANYWHERE! YOU DO NOT LIKE GREEN EGGS AND HAM? I DO NOT LIKE THEM, SAM-I-AM. COULD YOU, WOULD YOU, WITH A GOAT? I WOULD NOT, COULD NOT WITH A GOAT! WOULD YOU, COULD YOU, ON A BOAT?'
    green3 = 'I COULD NOT, WOULD NOT, ON A BOAT. I WILL NOT, WILL NOT, WITH A GOAT. I WILL NOT EAT THEM IN THE RAIN. NOT IN THE DARK! NOT IN A TREE! NOT IN A CAR! YOU LET ME BE! I DO NOT LIKE THEM IN A BOX. I DO NOT LIKE THEM WITH A FOX. I WILL NOT EAT THEM IN A HOUSE. I DO NOT LIKE THEM WITH A MOUSE. I DO NOT LIKE THEM HERE OR THERE. I DO NOT LIKE THEM ANYWHERE! I DO NOT LIKE GREEN EGGS AND HAM! I DO NOT LIKE THEM, SAM-I-AM. YOU DO NOT LIKE THEM. SO YOU SAY. TRY THEM! TRY THEM! AND YOU MAY. TRY THEM AND YOU MAY, I SAY. SAM! IF YOU LET ME BE, I WILL TRY THEM. YOU WILL SEE. (... and he tries them ...) SAY! I LIKE GREEN EGGS AND HAM! I DO! I LIKE THEM, SAM-I-AM! AND I WOULD EAT THEM IN A BOAT. AND I WOULD EAT THEM WITH A GOAT AND I WILL EAT THEM, IN THE RAIN. AND IN THE DARK. AND ON A TRAIN. AND IN A CAR. AND IN A TREE. THEY ARE SO GOOD, SO GOOD, YOU SEE! SO I WILL EAT THEM IN A BOX. AND I WILL EAT THEM WITH A FOX. AND I WILL EAT THEM IN A HOUSE. AND I WILL EAT THEM WITH A MOUSE. AND I WILL EAT THEM HERE AND THERE. SAY! I WILL EAT THEM ANYWHERE! I DO SO LIKE GREEN EGGS AND HAM! THANK YOU! THANK YOU, SAM I AM.'
    giving1 = 'Once there was a tree. and she loved a little boy. And everyday the boy would come and he would gather her leaves and make them into crowns and play king of the forest. He would climb up her trunk and swing from her branches and eat apples. And they would play hide-and-go-seek. And when he was tired, he would sleep in her shade. And the boy loved the tree.... very much. And the tree was happy. But time went by. And the boy grew older. And the tree was often alone. Then one day the boy came to the tree and the tree said, \"Come, Boy, come and climb up my trunk and swing from my branches and eat apples and play in my shade and be happy.\" \"I am too big to climb and play\" said the boy. \"I want to buy things and have fun. I want some money?\" \"I\'m sorry,\" said the tree, \"but I have no money. I have only leaves and apples. Take my apples, Boy, and sell them in the city. Then you will have money and you will be happy.\"'
    giving2 = 'And so the boy climbed up the tree and gathered her apples and carried them away. And the tree was happy. But the boy stayed away for a long time.... and the tree was sad. And then one day the boy came back and the tree shook with joy and she said, \"Come, Boy, climb up my trunk and swing from my branches and be happy.\" \"I am too busy to climb trees,\" said the boy. \"I want a house to keep me warm,\" he said. \"I want a wife and I want children, and so I need a house. Can you give me a house ?\" \" I have no house,\" said the tree. \"The forest is my house, but you may cut off my branches and build a house. Then you will be happy.\" And so the boy cut off her branches and carried them away to build his house. And the tree was happy. But the boy stayed away for a long time. And when he came back, the tree was so happy she could hardly speak. \"Come, Boy,\" she whispered, \"come and play.\" \"I am too old and sad to play,\" said the boy. \"I want a boat that will take me far away from here. Can you give me a boat?\" \"Cut down my trunk and make a boat,\" said the tree. \"Then you can sail away and be happy.\" And so the boy cut down her trunk and made a boat and sailed away. And the tree was happy ... but not really.'   
    giving3 = 'And after a long time the boy came back again. \"I am sorry, Boy,\" said the tree,\" but I have nothing left to give you - My apples are gone.\" \"My teeth are too weak for apples,\" said the boy. \"My branches are gone,\" said the tree. \" You cannot swing on them - \" \"I am too old to swing on branches,\" said the boy. \"My trunk is gone, \" said the tree. \"You cannot climb - \" \"I am too tired to climb\" said the boy. \"I am sorry,\" sighed the tree. \"I wish that I could give you something.... but I have nothing left. I am just an old stump. I am sorry....\" \"I don\'t need very much now,\" said the boy. \"just a quiet place to sit and rest. I am very tired.\" \"Well,\" said the tree, straightening herself up as much as she could, \"well, an old stump is good for sitting and resting Come, Boy, sit down. Sit down and rest.\" And the boy did. And the tree was happy.'
    outsiders1 = 'I had a long walk home and no company, but I usually lone it anyway, for no reason except that I like to watch movies undisturbed so I can get into them and live them with the actors. When I see a movie with someone it\'s kind of uncomfortable, like having someone read your book over your shoulder. I\'m different that way. I mean, my second-oldest brother, Soda, who is sixteen-going-on-seventeen, never cracks a book at all, and my oldest brother, Darrel, who we call Darry, works too long and hard to be interested in a story or drawing a picture, so I\'m not like them. And nobody in our gang digs movies and books the way I do. For a while there, I thought I was the only person in the world that did. So I loned it.'
    outsiders2 = 'It occurred to me then that they could kill me. I went wild. I started screaming for Soda, Darry, anyone. Someone put his hand over my mouth, and I bit it as hard as I could, tasting the blood running through my teeth. I heard a muttered curse and got slugged again, and they were stuffing a handkerchief in my mouth. One of them kept saying, \"Shut him up, for Pete\'s sake, shut him up!\" Then there were shouts and the pounding of feet, and the Socs jumped up and left me lying there, gasping. I lay there and wondered what in the world was happening; people were jumping over me and running by me and I was too dazed to figure it out. Then someone had me under the armpits and was hauling me to my feet. It was Darry. \"Are you all right, Ponyboy?\" He was shaking me and I wished he\'d stop. I was dizzy enough anyway. I could tell it was Darry though - partly because of the voice and partly because Darry\'s always rough with me without meaning to be. \"I\'m okay. Quit shaking me, Darry, I\'m okay.\"'
    outsiders3 = '\"Are you all right, kid? You look like you\'ve been in a fight.\" \"I have been. A rumble. I\'m okay.\" Johnny is not dead, I told myself, and I believed it. \"Hate to tell you this, kiddo,\" the guy said dryly, \"but you\'re bleedin\' all over my car seats.\" I blinked. \"I am?\" \"Your head.\" I reached up to scratch the side of my head where it\'d been itching for a while, and when I looked at my hand it was smeared with blood. \"Gosh, mister, I\'m sorry,\" I said, dumfounded. \"Don\'t worry about it. This wreck\'s been through worse. What\'s your address? I\'m not about to dump a hurt kid out on the streets this time of night.\" I told him. He drove me to my house, and I got out. \"Thanks a lot.\" What was left of our gang was in the living room. Steve was stretched out on the sofa, his shirt unbuttoned and his side bandaged. His eyes were closed, but when the door shut behind me he opened them, and I suddenly wondered if my own eyes looked as feverish and bewildered as his. Soda had a wide cut on his lip and a bruise across his cheek. There was a Band-Aid over Darry\'s forehead and he had a black eye. One side of Two-Bit\'s face was taped up; I found out later he had four stitches in his cheek and seven in his hand where he had busted his knuckles open over a Soc\'s head. They were lounging around, reading the paper and smoking.'
    giver1 = 'School seemed a little different today. The classes were the same: languages and communications; commerce and industry; science and technology; civil procedures and government. But during the breaks for recreation periods and the midday meal, the other new Twelves were abuzz with descriptions of their first day of training. All of them talked at once, interrupting each other, hastily making the required apology for interrupting, then forgetting again in the excitement of describing the new experiences. Jonas listened. He was very aware of his own admonition not to discuss his training. But it would have been impossible, anyway. There was no way to describe to his friends what he had experienced there in the Annex room. How could you describe a sled without describing a hill and snow; and how could you describe a hill and snow to someone who had never felt height or wind or that feathery, magical cold? '
    giver2 = 'He went to the desk, pretending not to be interested in the newchild. On the other side of the room, Mother and Lily were bending over to watch as Father unwrapped its blanket. \"What\'s his comfort object called?\" Lily asked, picking up the stuffed creature which had been placed beside the newchild in its basket. Father glanced at it. \"Hippo,\" he said. Lily giggled at the strange word. \"Hippo,\" she repeated, and put the comfort object down again. She peered at the unwrapped newchild who waved his arms. \"I think newchildren are so cute,\" Lily sighed. \"I hope I get assigned to be a Birthmother.\" \"Lily!\" Mother spoke very sharply. \"Don\'t say that. There\'s very little honor in that Assignment.\" \"But I was talking to Natasha. You know the Ten who lives around the corner? She does some of her volunteer hours at the Birthing Center. And she told me that the Birthmothers get wonderful food, and they have very gentle exercise periods, and most of the time they just play games and amuse themselves while they\'re waiting. I think I\'d like that,\" Lily said petulantly.'
    giver3 = 'Jonas reached the opposite side of the river, stopped briefly, and looked back. The community where his entire life had been lived lay behind him now, sleeping. At dawn, the orderly, disciplined life he had always known would continue again, without him. The life where nothing was ever expected. Or inconvenient. Or unusual. The life without color, pain, or past. He pushed firmly again at the pedal with his foot and continued riding along the road. It was not safe to spend time looking back. He thought of the rules he had broken so far: enough that if he were caught, now, he would be condemned. First, he had left the dwelling at night. A major transgression. Second, he had robbed the community of food: a very serious crime, even though what he had taken was leftovers, set out on the dwelling doorsteps for collection. Third, he had stolen his father\'s bicycle. He had hesitated for a moment, standing beside the bikeport in the darkness, not wanting anything of his father\'s and uncertain, as well, whether he could comfortably the larger bike when he was so accustomed to his own. But it was necessary because it had the child seat attached to the back. And he had taken Gabriel, too.'
    hunger1 = 'I swing my legs off the bed and slide into my hunting boots. Supple leather that has molded to my feet. I pull on trousers, a shirt, tuck my long dark braid up into a cap, and grab my forage bag. On the table, under a wooden bowl to protect it from hungry rats and cats alike, sits a perfect little goat cheese wrapped in basil leaves. Prim\'s gift to me on reaping day. I put the cheese carefully in my pocket as I slip outside. Our part of District 12, nicknamed the Seam, is usually crawling with coal miners heading out to the morning shift at this hour. Men and women with hunched shoulders, swollen knuckles, many who have long since stopped trying to scrub the coal dust out of their broken nails, the lines of their sun- ken faces. But today the black cinder streets are empty. Shutters on the squat gray houses are closed. The reaping isn\'t un- til two. May as well sleep in. If you can. '
    hunger2 = 'For a moment, no response. Then one of Rue\'s eyes edges around the trunk. \"You want me for an ally?\" \"Why not? You saved me with those tracker jackers. You\'re smart enough to still be alive. And I can\'t seem to shake you anyway,\" I say. She blinks at me, trying to decide. \"You hungry?\" I can see her swallow hard, her eye flickering to the meat. \"Come on then, I\'ve had two kills today.\" Rue tentatively steps out into the open. \"I can fix your stings.\" \"Can you?\" I ask. \"How?\" She digs in the pack she carries and pulls out a handful of leaves. I\'m almost certain they\'re the ones my mother uses. \"Where\'d you find those?\" \"Just around. We all carry them when we work in the orchards. They left a lot of nests there,\" says Rue. \"There are a lot here, too.\" '
    hunger3 = 'I don\'t care now that Peeta\'s footfalls send rodents scurrying, make birds take wing. We have to fight Cato and I\'d just as soon do it here as on the plain. But I doubt I\'ll have that choice. If the Gamemakers want us in the open, then in the open we will be. We stop to rest for a few moments under the tree where the Careers trapped me. The husk of the tracker jacker nest, beaten to a pulp by the heavy rains and dried in the burning sun, confirms the location. I touch it with the tip of my boot, and it dissolves into dust that is quickly carried off by the breeze. I can\'t help looking up in the tree where Rue secretly perched, waiting to save my life. Tracker jackers. Glimmer\'s bloated body. The terrifying hallucinations . . . \"Let\'s move on,\" I say, wanting to escape the darkness that surrounds this place. Peeta doesn\'t object. '
    age1 = 'Therefore, whenever anything happened that Mrs. Archer wanted to know about, she asked Mr. Jackson to dine; and as she honoured few people with her invitations, and as she and her daughter Janey were an excellent audience, Mr. Jackson usually came himself instead of sending his sister. If he could have dictated all the conditions, he would have chosen the evenings when Newland was out; not because the young man was uncongenial to him (the two got on capitally at their club) but because the old anecdotist sometimes felt, on Newland\'s part, a tendency to weigh his evidence that the ladies of the family never showed.'
    age2 = 'Archer received this strange communication in silence. His eyes remained unseeingly fixed on the thronged sunlit square below the window. At length he said in a low voice: \"She never asked me.\" \"No. I forgot. You never did ask each other anything, did you? And you never told each other anything. You just sat and watched each other, and guessed at what was going on underneath. A deaf-and-dumb asylum, in fact! Well, I back your generation for knowing more about each other\'s private thoughts than we ever have time to find out about our own.—I say, Dad,\" Dallas broke off, \"you\'re not angry with me? If you are, let\'s make it up and go and lunch at Henri\'s. I\'ve got to rush out to Versailles afterward.\" Archer did not accompany his son to Versailles. He preferred to spend the afternoon in solitary roamings through Paris. He had to deal all at once with the packed regrets and stifled memories of an inarticulate lifetime.'
    age3 = '\"Madame Olenska came forward with a smile. Her face looked vivid and happy, and she held out her hand gaily to Archer while she stooped to her grandmother\'s kiss. \"I was just saying to him, my dear: \'Now, why didn\'t you marry my little Ellen?\'\" Madame Olenska looked at Archer, still smiling. \"And what did he answer?\" \"Oh, my darling, I leave you to find that out! He\'s been down to Florida to see his sweetheart.\" \"Yes, I know.\" She still looked at him. \"I went to see your mother, to ask where you\'d gone. I sent a note that you never answered, and I was afraid you were ill.\" He muttered something about leaving unexpectedly, in a great hurry, and having intended to write to her from St. Augustine. \"And of course once you were there you never thought of me again!\" She continued to beam on him with a gaiety that might have been a studied assumption of indifference. \"If she still needs me, she\'s determined not to let me see it,\" he thought, stung by her manner. He wanted to thank her for having been to see his mother, but under the ancestress\'s malicious eye he felt himself tongue-tied and constrained.'
    crime1 = 'He had successfully avoided meeting his landlady on the staircase. His garret was under the roof of a high, five-storied house, and was more like a cupboard than a room. The landlady, who provided him with garret, dinners, and attendance, lived on the floor below, and every time he went out he was obliged to pass her kitchen, the door of which invariably stood open. And each time he passed, the young man had a sick, frightened feeling, which made him scowl and feel ashamed. He was hopelessly in debt to his landlady, and was afraid of meeting her. This was not because he was cowardly and abject, quite the contrary; but for some time past, he had been in an over-strained, irritable condition, verging on hypochondria. He had become so completely absorbed in himself, and isolated from his fellows that he dreaded meeting, not only his landlady, but any one at all. He was crushed by poverty, but the anxieties of his position had of late ceased to weigh upon him. He had given up attending to matters of practical importance; he had lost all desire to do so. Nothing that any landlady could do had a real terror for him. But to be stopped on the stairs, to be forced to listen to her trivial, irrelevant gossip, to pestering demands for payment, threats and complaints, and to rack his brains for excuses, to prevaricate, to lie--no, rather than that, he would creep down the stairs like a cat and slip out unseen.'
    crime2 = '\"I want to attempt a thing like that and am frightened by these trifles,\" he thought, with an odd smile. \"Hm . . . yes, all is in a man\'s hands and he lets it all slip from cowardice, that\'s an axiom. It would be interesting to know what it is men are most afraid of. Taking a new step, uttering a new word is what they fear most. . . . But I am talking too much. It\'s because I chatter that I do nothing. Or perhaps it is that I chatter because I do nothing. I\'ve learned to chatter this last month, lying for days together in my den thinking of Jack the Giant-killer. Why am I going there now? Am I capable of that? Is that serious? It is not serious at all. It\'s simply a fantasy to amuse myself; a plaything! Yes, maybe it is a plaything.\"' 
    crime3 = '\"What do you want?\" the old woman said severely, coming into the room and, as before, standing in front of him so as to look him straight in the face. \"I\'ve brought something to pawn here,\" and he drew out of his pocket an old-fashioned flat silver watch, on the back of which was engraved a globe; the chain was of steel. \"But the time is up for your last pledge. The month was up the day before yesterday.\" \"I will bring you the interest for another month; wait a little.\" \"But that\'s for me to do as I please, my good sir, to wait or to sell your pledge at once.\" \"How much will you give me for the watch, Alyona Ivanovna?\" \"You come with such trifles, my good sir, it\'s scarcely worth anything. I gave you two roubles last time for your ring and one could buy it quite new at a jeweller\'s for a rouble and a half.\" \"Give me four roubles for it, I shall redeem it, it was my father\'s. I shall be getting some money soon.\" \"A rouble and a half, and interest in advance, if you like!\" \"A rouble and a half!\" cried the young man.'
    moby1 = 'Lord save me, thinks I, that must be the harpooneer, the infernal head peddler. But I lay perfectly still, and resolved not to say a word till spoken to. Holding a light in one hand, and that identical New Zealand head in the other, the stranger entered the room, and without looking towards the bed, placed his candle a good way off from me on the floor in one corner, and then began working away at the knotted cords of the large bag I before spoke of as being in the room. I was all eagerness to see his face, but he kept it averted for some time while employed in unlacing the bag\'s mouth. This accomplished, however, he turned round when, good heavens! what a sight! Such a face! It was of a dark, purplish, yellow colour, here and there stuck over with large blackish looking squares. Yes, it\'s just as I thought, he\'s a terrible bedfellow; he\'s been in a fight, got dreadfully cut, and here he is, just from the surgeon. But at that moment he chanced to turn his face so towards the light, that I plainly saw they could not be sticking plasters at all, those black squares on his cheeks.'
    moby2 = 'And half concealed in this queer tenement, I at length found one who by his aspect seemed to have authority; and who, it being noon, and the ship\'s work suspended, was now enjoying respite from the burden of command. He was seated on an old fashioned oaken chair, wriggling all over with curious carving; and the bottom of which was formed of a stout interlacing of the same elastic stuff of which the wigwam was constructed. There was nothing so very particular, perhaps, about the appearance of the elderly man I saw; he was brown and brawny, like most old seamen, and heavily rolled up in blue pilot cloth, cut in the Quaker style; only there was a fine and almost microscopic net work of the minutest wrinkles interlacing round his eyes, which must have arisen from his continual sailings in many hard gales, and always looking to windward; for this causes the muscles about the eyes to become pursed together. Such eye wrinkles are very effectual in a scowl. \"Is this the Captain of the Pequod?\" said I, advancing to the door of the tent. \"Supposing it be the captain of the Pequod, what dost thou want of him?\" he demanded. \"I was thinking of shipping.\" \"Thou wast, wast thou? I see thou art no Nantucketer ever been in a stove boat?\" \"No, Sir, I never have.\" \"Dost know nothing at all about whaling, I dare say eh?\" \"Nothing, Sir; but I have no doubt I shall soon learn. I\'ve been several voyages in the merchant service, and I think that\"'
    moby3 = 'He was an old man, who, at the age of nearly sixty, had postponedly encountered that thing in sorrow\'s technicals called ruin. He had been an artisan of famed excellence, and with plenty to do; owned a house and garden; embraced a youthful, daughter like, loving wife, and three blithe, ruddy children; every Sunday went to a cheerful looking church, planted in a grove. But one night, under cover of darkness, and further concealed in a most cunning disguisement, a desperate burglar slid into his happy home, and robbed them all of everything. And darker yet to tell, the blacksmith himself did ignorantly conduct this burglar into his family\'s heart. It was the Bottle Conjuror! Upon the opening of that fatal cork, forth flew the fiend, and shrivelled up his home. Now, for prudent, most wise, and economic reasons, the blacksmith\'s shop was in the basement of his dwelling, but with a separate entrance to it; so that always had the young and loving healthy wife listened with no unhappy nervousness, but with vigorous pleasure, to the stout ringing of her young armed old husband\'s hammer; whose reverberations, muffled by passing through the floors and walls, came up to her, not unsweetly, in her nursery; and so, to stout Labor\'s iron lullaby, the blacksmith\'s infants were rocked to slumber.'
    try:
        d = ReadingLevel().automatedReadabilityIndex(default)
        w1 = ReadingLevel().automatedReadabilityIndex(winnie1)
        w2 = ReadingLevel().automatedReadabilityIndex(winnie2)
        w3 = ReadingLevel().automatedReadabilityIndex(winnie3)
        g1 = ReadingLevel().automatedReadabilityIndex(green1)
        g2 = ReadingLevel().automatedReadabilityIndex(green2)
        g3 = ReadingLevel().automatedReadabilityIndex(green3)
        tgt1 = ReadingLevel().automatedReadabilityIndex(giving1)
        tgt2 = ReadingLevel().automatedReadabilityIndex(giving2)
        tgt3 = ReadingLevel().automatedReadabilityIndex(giving3)
        o1 = ReadingLevel().automatedReadabilityIndex(outsiders1)
        o2 = ReadingLevel().automatedReadabilityIndex(outsiders2)
        o3 = ReadingLevel().automatedReadabilityIndex(outsiders3)
        tg1 = ReadingLevel().automatedReadabilityIndex(giver1)
        tg2 = ReadingLevel().automatedReadabilityIndex(giver2)
        tg3 = ReadingLevel().automatedReadabilityIndex(giver3)
        h1 = ReadingLevel().automatedReadabilityIndex(hunger1)
        h2 = ReadingLevel().automatedReadabilityIndex(hunger2)
        h3 = ReadingLevel().automatedReadabilityIndex(hunger3)
        a1 = ReadingLevel().automatedReadabilityIndex(age1)
        a2 = ReadingLevel().automatedReadabilityIndex(age2)
        a3 = ReadingLevel().automatedReadabilityIndex(age3)
        c1 = ReadingLevel().automatedReadabilityIndex(crime1)
        c2 = ReadingLevel().automatedReadabilityIndex(crime2)
        c3 = ReadingLevel().automatedReadabilityIndex(crime3)
        m1 = ReadingLevel().automatedReadabilityIndex(moby1)
        m2 = ReadingLevel().automatedReadabilityIndex(moby2)
        m3 = ReadingLevel().automatedReadabilityIndex(moby3)
       
        print('\nD = ', d.final_reading_level, d.avg_frequency, d.clausesPerSent)
        print('\nW1 = ', w1.final_reading_level, w1.avg_frequency, w1.clausesPerSent)
        print('\nW2 = ', w2.final_reading_level, w2.avg_frequency, w2.clausesPerSent)
        print('\nW3 = ', w3.final_reading_level, w3.avg_frequency, w3.clausesPerSent)
        print('\nG1 = ', g1.final_reading_level, g1.avg_frequency, g1.clausesPerSent)
        print('\nG2 = ', g2.final_reading_level, g2.avg_frequency, g2.clausesPerSent)
        print('\nG3 = ', g3.final_reading_level, g3.avg_frequency, g3.clausesPerSent)
        print('\nTGT1 = ', tgt1.final_reading_level, tgt1.avg_frequency, tgt1.clausesPerSent)
        print('\nTGT2 = ', tgt2.final_reading_level, tgt2.avg_frequency, tgt2.clausesPerSent)
        print('\nTGT3 = ', tgt3.final_reading_level, tgt3.avg_frequency, tgt3.clausesPerSent)
        print('\nO1 = ', o1.final_reading_level, o1.avg_frequency, o1.clausesPerSent)
        print('\nO2 = ', o2.final_reading_level, o2.avg_frequency, o2.clausesPerSent)
        print('\nO3 = ', o3.final_reading_level, o3.avg_frequency, o3.clausesPerSent)
        print('\nTG1 = ', tg1.final_reading_level, tg1.avg_frequency, tg1.clausesPerSent)
        print('\nTG2 = ', tg2.final_reading_level, tg2.avg_frequency, tg2.clausesPerSent)
        print('\nTG3 = ', tg3.final_reading_level, tg3.avg_frequency, tg3.clausesPerSent)
        print('\nH1 = ', h1.final_reading_level, h1.avg_frequency, h1.clausesPerSent)
        print('\nH2 = ', h2.final_reading_level, h2.avg_frequency, h2.clausesPerSent)
        print('\nH3 = ', h3.final_reading_level, h3.avg_frequency, h3.clausesPerSent)
        print('\nA1 = ', a1.final_reading_level, a1.avg_frequency, a1.clausesPerSent)
        print('\nA2 = ', a2.final_reading_level, a2.avg_frequency, a2.clausesPerSent)
        print('\nA3 = ', a3.final_reading_level, a3.avg_frequency, a3.clausesPerSent)
        print('\nC1 = ', c1.final_reading_level, c1.avg_frequency, c2.clausesPerSent)
        print('\nC2 = ', c2.final_reading_level, c2.avg_frequency, c2.clausesPerSent)
        print('\nC3 = ', c3.final_reading_level, c3.avg_frequency, c3.clausesPerSent)
        print('\nM1 = ', m1.final_reading_level, m1.avg_frequency, m1.clausesPerSent)
        print('\nM2 = ', m2.final_reading_level, m2.avg_frequency, m2.clausesPerSent)
        print('\nM3 = ', m3.final_reading_level, m3.avg_frequency, m3.clausesPerSent)
        '''m = Metrics.produceFrom(test)
        print()
        print()
        print('Metrics:\n', m)
        print('\n\nDefault\n')
        print('Number of clauses = ', m.clauses())
        print('Number of sentences = ', m.sentences())
        print('Number of clauses per sentence = ', m.clausesPerSentence())
        print()
        
        m = Metrics.produceFrom(age)
        print('\n\nAge of Innocence\n')
        print('Number of clauses = ', m.clauses())
        print('Number of sentences = ', m.sentences())
        print('Number of clauses per sentence = ', m.clausesPerSentence())
        print()
        
        m = Metrics.produceFrom(winnie)
        print('\n\nWinnie the Pooh\n')
        print('Number of clauses = ', m.clauses())
        print('Number of sentences = ', m.sentences())
        print('Number of clauses per sentence = ', m.clausesPerSentence())'''
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise # well-known exception that the caller will digest 