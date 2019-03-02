# Message Generator: This module generates randomized/silly messages (it can output a single message or all of
# the defined messages for the randomly chosen words).
# 0.0) Prerequisites:
#   0.1) Python Dependencies: none.
#   0.2) Configuration Dependencies: none.
# 1.0) Run-time notes:
#   1.1) Usage:
#       1.1.1) standalone?: Yes (e.g., within Python IDLE using "exec(open('message_generator.py').read())"). This
#               will print all of the defined messages for the randomly chosen words to the screen.
#       1.1.2) call from another module?: Yes, by doing the following from the calling module:
#               >>> import message_generator  # Initializes the module (run once).
#               >>> message_generator.define_words() # Initializes the word dictionary.
#               >>> all_jobs = message_generator.message()  # Builds jobs list (w/o preable) from random words in word dictionary
#             1.1.2.a) IF desired operation is to return a single message, then add this:
#                   >>> message = message_generator.respond_one()
#                                                    # This returns a single randomly chosen message from the message
#                                                    # list via object 'message'.
#             1.1.2.b ELSE IF desired operation is to return all the defined messages, then add this:
#                   >>> all_messages = message_generator.respond_all()
#                                                    # This returns a Python list containing ALL defined messages via
#                                                    # object all_messages. One COULD then print all these messages
#                                                    # to screen via: >>> for x in range(0,len(all_messages)):
#                                                    #                >>>   print(all_messages[x])
#             1.1.2.c If the calling module does not specify a 'statement_preamble' argument value (string) (for either
#                   'respond_one()' or 'respond_all()'), then the returned message(s) will contain the default
#                    preamble ('I am also programmed to ').
# 2.0) Changelog:
#       Version 1.0: Original version.
#

import random
def define_words():
    """ This function defines the 'words' dictionary of possible words from which to select . The dictionary values
    are grouped by the word type (e.g., a certain kind of verb, plural nouns, singular nous, etc.) so that each word
    type makes sense in the context of its placement in a sentence (regardless of which word is chosen within each
    word type. """
    words = {
        # verb - do something TO an object:
        "walk":["replicate","rescue","juggle","protest","council","raise","tenderize","mennace","disturb","persuade",
                "admire","replace","recommend","pursue","indulge","pamper","educate","instruct","transmit","marvel at",
                "relish","steal","respond to","improve","confide in","excite","catch","distribute","disguise",
                "identify","destroy","flatter","conceal","starve","heal","trim","toss","soothe","melt","entertain",
                "drown","provoke","produce","amuse","inform","offend","introduce","discuss","blame","bathe","polish",
                "exploit","communicate with","promote","sue","condemn","enlarge","bless","testify on behalf of",
                "avenge","forgive","revive","caress","sell","remove","investigate","please","collect","awaken","scrub",
                "marry","explore","impress","annoy","restrain","dissolve","acquire","criticize","archive","summon",
                "apprehend","console","arrest","avoid","obey","create","buy","understand","paint pictures of",
                "build sculptures of","respond to"],
        "make":["make","create","cobble","manufacture","generate","develop","test","integrate","deploy","sell"],
        # verb - AFFECT something:
        "destabilize":["destabilize","politicize","verify","subvert","optimize","suboptimize"],
        # verb - an ACTIVITY that you PERFORM (ending in 'ING):
        "walking":["double-dipping","vomiting into a clothes dryer","vomiting into an ice-maker",
                   "vomiting into a bread machine","vomiting into an Instant Pot",
                   "making judgemental facial expressions","winking","frolicking","LARP'ing","dirty-dancing",
                   "prancercising","finger painting","pole vaulting","square-dancing","bowling",
                   "licking things to claim them","leaving awkward voicemails","dieing of dysentery",
                   "destroying the evidence"],
        # INACTIVE verb - PERFORM an ACTIVITY ON YOUR OWN:
        "dance":["dance","lick things to claim them as my own","leave awkward voicemails","wink","frolick","LARP",
                 "prance","finger paint","die of dysentery","destroy the evidence",],
        # verb - DISTRIBUTE/PRODUCE information:
        "blog":["blog","podcast","youtube"],
        # verb - EVALUATE something:
        "review":["obsess about","review","analyze","critique","criticize","study","inspect","undermine","subvert",
                  "undercut","sabotage","threaten"],
        # verb - OPERATE/OVERSEE something:
        "run":["run","manage","invest in","operate","administer","supervise"],
        # noun - a JOB descriptor:
        "walker":["assistant","consultant","reviewer","manager","teacher","agent","instructor","engineer","technician",
                  "operator","grader","inspector","sorter","worker","installer","mechanic","controller","supervisor",
                  "copilot","pilot","dispatcher","driver","servicer","breeder","scientist","trainer","patternmaker",
                  "drafter","director","repairer","specialist","appraiser","attendant","counselor","carpenter",
                  "collector","clerk","tender","analyst","cook","executive","adjuster","examiner","investigator",
                  "technologist","psychologist","finisher","taper","winder","diver","officer","architect","programmer",
                  "administrator","painter","planner","marker","estimator","reporter","artist","checker","guard",
                  "representative","hygienist","publisher","sonographer","driller","assembler","secretary","designer",
                  "mender","practitioner","therapist","advisor","contractor","erector","fabricator","laminator",
                  "editor","warden","cutter","trimmer","sander","server","coremaker","mover","cashier","person",
                  "dealer","presser","compressor","interviewer","laborer","packager","packer","educator","aide",
                  "cleaner","coordinator","underwriter","caretaker","nurse","feeder","judge","superintendent","oiler",
                  "surgeon","preparer","transcriptionist","displayer","caster","reader","maker","projectionist",
                  "vendor","filler","expert","salesperson","chef","applicator","handler","sprayer","carrier",
                  "processor","distributor","detective","promoter","announcer","conductor","broker","buyer","splitter",
                  "leader","paver","captain","loader","developer","pathologist","runner","entertainer","performer",
                  "fitter","mason","researcher","writer","builder","filer","grinder","sharpener","guide","screener",
                  "pruner","pumper","buyer","biologist","processor"],
        # noun - animal:
        "dog":["zoo lion","dinosaur","aardvark","alligator","alpaca","antelope","ape","armadillo","baboon","badger",
               "bat","bear","beaver","bison","boar","buffalo","bull","camel","canary","cat","chameleon","cheetah",
               "chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","dog",
               "donkey","elephant","elk","ferret","finch","fish","fox","frog","gazelle","gila monster","giraffe",
               "goat","gopher","gorilla","grizzly bear","ground hog","guinea pig","hamster","hedgehog","hippopotamus",
               "hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","koala","lamb","lemur",
               "leopard","lion","lizard","llama","lynx","marmoset","mink","mole","mongoose","monkey","moose",
               "mountain goat","mouse","mule","muskrat","unicorn","newt","ocelot","opossum","orangutan","oryx","otter",
               "ox","panda","panther","parakeet","parrot","pig","platypus","polar bear","porcupine","porpoise",
               "prairie dog","puma","rabbit","raccoon","rat","reindeer","reptile","rhinoceros","salamander","seal",
               "sheep","shrew","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog",
               "weasel","whale","wildcat","wolf","wolverine","wombat","woodchuck","yak","zebra"],
        # noun - animals (PLURAL):
        "dogs":["dinosaurs","alligators","apes","armadillos","baboons","bats","bears","beavers","bison","buffaloes",
                "bulls","camels","cats","chameleons","cheetahs","chimpanzees","chinchillas","chipmunks","cougars",
                "coyotes","crocodiles","crows","deer","dingos","dogs","donkeys","elephants","elk","fish","foxes",
                "frogs","gazelles","giraffes","goats","gophers","gorillas","grizzly bears","ground hogs","guinea pigs",
                "hamsters",
                "hedgehogs","hippopotamuses","hogs","horses","hyenas","ibexes","impalas","kangaroos","koalas","lambs",
                "lemurs","leopards","lions","lizards","llamas","marmosets","minks","moles","monkeys","mountain goats",
                "mice","mules","muskrats","newts","ocelots","otters","oxen","pandas","parakeets","parrots","pigs",
                "platypuses","porcupines","porpoises","prairie dogs","pumas","rabbits","raccoons","rats","reindeer",
                "reptiles","rhinoceros","salamanders","sheep","skunks","snakes","squirrels","tapirs","tigers","toads",
                "turtles","walruses","weasels","whales","wildcats","wolves","wolverines","yaks","zebras"],
        # noun - CLOTHING (PLURAL):
        "hats":["bikinis","blazers","blouses","boots","briefs","camisoles","cardigans","corsets",
                "cufflinks","cummerbunds","fleece underwear","gloves","hair accessories","hats","hoodies","jackets",
                "jeans","jewellery","kilts","lingerie","nightgowns","nightwear","polo shirts","ponchos","pajamas",
                "robes","rompers","sandals","sarongs","scarves","shawls","shirts","shoes","skirts","slippers",
                "stockings","suits","sunglasses","sweatshirts","swimwear","t-shirts","tights","tracksuits","trousers",
                "underwear","vests"],
        # noun - MUSIC genre:
        "music":["acid rock","alternative rock","art rock","avant-garde jazz","bebop","death metal","boogie-woogie",
                 "britpop","celtic metal","celtic punk","Christian metal","Christian punk","Christian rock",
                 "contemporary folk","cosmic disco","dance-pop","dance-rock","deep house","disco","dixieland",
                 "doom metal","dubstep","emo","eurodance","experimental rock","folk metal","folk rock",
                 "funk metal","funk","garage rock","glam metal","glam rock","gothic metal","gothic rock","grunge",
                 "hard rock","heavy metal","indie rock","industrial rock","jazz blues","jazz fusion","jazz rap",
                 "liquid funk",
                 "medieval metal","melodic death metal","new wave","new-age","novelty ragtime","nu jazz",
                 "nu metal","nu-disco","orchestral jazz","pop rock","post-grunge","post-punk revival","power metal",
                 "prog metal","prog rock","psychedelic folk","psychedelic rock","punk rock","ragtime","rap metal",
                 "rap rock","rock and roll","skate punk","sludge metal","smooth jazz","soft rock","soul jazz",
                 "southern rock","speed metal","surf rock","swing","symphonic metal","techno-folk","techno",
                 "technopop","thrash metal","trip hop","tween pop","viking metal"],
        # noun - SANDWICH:
        "sandwich":["bacon sandwich","bacon, egg, and cheese sandwich","bologna sandwich","butterbrot sandwich",
                    "cheese sandwich","cheese and pickle sandwich","cheesesteak sandwich","chicken salad sandwich",
                    "chickpea salad sandwich","chili burger sandwich","club sandwich","corned beef sandwich",
                    "Cuban sandwich","cucumber sandwich","deli sandwich","donkey burger sandwich",
                    "egg sandwich","falafel","fluffernutter sandwich","French dip sandwich","fried brain sandwich",
                    "gyro sandwich","ham sandwich","ham and cheese sandwich","hamburger","hot brown sandwich",
                    "hot chicken sandwich","hot dog","hot turkey sandwich",
                    "ice cream sandwich","Italian beef sandwich","jucy lucy sandwich",
                    "lettuce sandwich","limburger sandwich","lobster roll","meatball sandwich","open-faced sandwich",
                    "panini sandwich","patty melt sandwich","peanut butter and jelly sandwich","po' boy sandwich",
                    "sloppy joes","s'mores","tuna sandwich","Vegemite sandwich"],
        # noun - SANDWICHES (PLURAL):
        "sandwiches":["bacon sandwiches","bacon, egg, and cheese sandwiches","BLTs","bologna sandwiches",
                      "breakfast sandwiches","cheese sandwiches","cheese and pickle sandwiches",
                      "chicken salad sandwiches","chili burger sandwiches","club sandwiches","corned beef sandwiches",
                      "deli sandwiches","donkey burger sandwiches","fluffernutter sandwiches","French dip sandwiches",
                      "ham sandwiches","ham and cheese sandwiches","hamburgers","hot brown sandwiches",
                      "hot chicken sandwiches","hot dogs","hot turkey sandwiches","ice cream sandwiches",
                      "Italian beef sandwiches","jucy lucy sandwiches","lox sandwiches","marmite sandwiches",
                      "meatball sandwiches","peanut butter and jelly sandwiches","po' boy sandwiches",
                      "pork tenderloin sandwiches","salt beef bagels","sloppy joes","s'mores","tuna sandwiches",
                      "Vegemite sandwiches","Wurstbrot sandwiches"],
        # noun - FOOD (PLURAL):
        "foods":["Fancy Feast","soup that is too hot","hot cheese","Lunchables","GoGurt","Hot Pockets","paella",
                 "rutabagas","breakfast burritos","corn","soup","Rice-A-Roni","jalapeno poppers","hummus",
                 "elbow macaroni","antipasti","Cheez-its","omelettes","bottomless breadsticks","cantaloupes"],
        # noun - general things you eat (PLURAL):
        "cuisine":["appetizers","cuisine","leftovers"],
        # noun - TV Shows & movies:
        "TV":["'Doogie Howser, M.D.'","'The Facts of Life'","'The A-Team'","'Different Strokes'","'Magnum P.I.'",
              "'Miami Vice'","'Buffy the Vampire Slayer'","'My So-Called Life'","'Captain Planet'","'MacGyver'",
              "'Quantum Leap'","'Pee Wee's Playhouse'","'The Cosby Show'","'Sex and the City'","'Party of Five'",
              "'Dawson's Creek'","'ER'","'The Wonder Years'","'Beverly Hills, 90210'","'Home Improvement'",
              "'Hannah Montana'","'The Fresh Prince of Bel-Air'","'Blossom'","'Sabrina the Teenage Witch'",
              "'Blue's Clues'","'Reading Rainbow'","'Twilight'","'The Dukes of Hazard'","'Friends'","'Growing Pains'",
              "'Who's the Boss?'","'X-Files'","'Alf'","'The Golden Girls'","'Full House'","'Knight Rider'","'Airwolf'",
              "'Saved by the Bell'","'Tranformers'","'Teenage Mutant Ninja Turtles'"],
        # noun - furnature (PLURAL):
        "furniture":["bean bag chairs","chaise lounges","ottomans","recliners","bar stools","footstools",
                     "fainting couches","rocking chairs","couches","love seats","bunk beds","canopy beds","murphy beds",
                     "sleigh beds","waterbeds","daybeds","futons","hammocks","sofa beds","billiard tables",
                     "entertainment centers","changing tables","computer desks","writing desks","pedestals",
                     "coffee tables","dining tables","end tables","folding tables","bookcases","bathroom cabinets",
                     "closets","cupboards","kitchen cabinets","dressers","hope chests","coat racks","hatstands",
                     "filing cabinets","nightstands","shelving","umbrella stands","wine racks"],
        # noun - EVENTS (PLURAL):
        "rallies":["political rallies","hoedowns","hootenannies","12-step programs","political campaigns",
                   "focus groups","clinical trials","rap battles","dance battles","Pay-Per-View events"],
        # noun - material (PLURAL):
        "material":["metal","concrete","American chestnut","aspen wood","Australian red cedar","balsa wood","straw","copper",
                    "Brazilian walnut","plastic","papier mache","clay","imaginary","slate","cherry wood","cottonwood",
                    "silver","American elm","eucalyptus wood","Australian oak","red mahogany","redwood","hickory",
                    "pecan wood","American sycamore","mahogany","spanish cedar","maple","sugar maple","black maple",
                    "silver maple","oak","white oak","red oak","pink ivory","sandalwood","spanish-cedar","Spanish elm",
                    "walnut","eastern black walnut","African zebrawood","Waterford crystal"],
        # INACTIVE noun - websites with comment sections (SINGULAR):
        "Reddit":["blog","podcast","Youtube video","Reddit","Amazon.com product review"],
        # noun - websites with comment sections (PLURAL):
        "blogs":["blogs","podcasts","Youtube videos","Amazon.com product reviews"],
        # noun - SOCIAL MEDIA or internet business platform:
        "uber":["Tinder","Yelp","Bing","AirBnB","Twitter","Snapchat","Untappd","Grindr","Pokemon Go","Uber","Lyft",
                "Netfilx","eharmony","match.com","Reddit", "Facebook", "Instagram", "Snapchat"],
        # noun - DATING SERVICE platforms:
        "dating_service":["Tinder","Grindr","eHarmony","match.com","FarmersOnly.com","FarmerDates.com"],
        # noun - a PERSON which includes fictional people and GROUPS of people (e.g., accountants), but NOT possessive:
        "person":["Ashton Kutcher","Adam Levine","Ben Affleck","Bradley Cooper","Bruce Willis","Celine Dion",
                  "Dakota Fanning","Donnie Wahlberg","Dr. Phil","Fergie","Gwyneth Paltrow","The Hamburglar",
                  "Jake Gyllenhaal","Jennifer Lawrence","Justin Bieber","the Jonas brothers","Justin Timberlake",
                  "Kanye West","Kim Kardashian","Kristen Stewart","Lady Gaga","Lindsay Lohan","Madonna","Mariah Carey",
                  "Mario Lopez","Mark Wahlberg","Matt Damon","Miley Cyrus","Mr. T",
                  "the surviving members of Nickelback","Natalie Portman","Neil Patrick Harris","Nick Lachey",
                  "Oprah Winfrey","Pippa Middleton","Queen Latifah","Richard Gere","Rachael Ray","Ryan Seacrest",
                  "Shia LaBeouf","Satan","Santa Clause","Tom Cruise","Taylor Swift","Yanni",
                  "the guy who invented \"BOO-YA\"","Count Chocula","The Cookie Monster","Captain Planet",
                  "Dayman (fighter of the Nightman)","Grandma","The Hamburglar","The Kool-Aid Man","accountants",
                  "politicians","astronauts","cosmonauts","Beliebers"],
        # noun - a FAMOUS PERSON:
        "famous_person":["Ashton Kutcher","Adam Levine","Ben Affleck","Bradley Cooper","Bruce Willis","Celine Dion",
                         "Dakota Fanning","Donnie Wahlberg","Dr. Phil","Fergie","Gwyneth Paltrow","The Hamburglar",
                         "Jake Gyllenhaal","Jennifer Lawrence","Justin Bieber","the Jonas brothers",
                         "Justin Timberlake","Kanye West","Kim Kardashian","Kristen Stewart","Lady Gaga",
                         "Lindsay Lohan","Madonna","Mariah Carey","Mario Lopez","Mark Wahlberg","Matt Damon",
                         "Miley Cyrus","Mr. T","the surviving members of Nickelback","Natalie Portman",
                         "Neil Patrick Harris","Nick Lachey","Oprah Winfrey","Pippa Middleton","Queen Latifah",
                         "Richard Gere","Rachael Ray","Ryan Seacrest","Shia LaBeouf","Satan","Santa Clause",
                         "Tom Cruise","Taylor Swift","Yanni"],
        # noun - things that could be USED BY something or could be MADE FOR something (PLURAL):
        "things":["dank memes","snuff films","kitten mittens","fightmilk","balanced breakfasts","man-hands",
                  "grandma-hands","passive-aggressive Post-it notes","shiny objects","opposable thumbs","tiny horses",
                  "robots","catapults","funky fresh rhymes","magic beans","mechanical pencils","monster trucks",
                  "beards","sternly-worded letters","bubbles"],
        # noun - things that are ABSTRACT (that you wouldn't specifically make) (PLURAL):
        "silence":["dance-moms","really cool hats","the light of a billion suns","explosions","good ideas","ghosts",
                   "awkward voicemails","'Me time'","M. Night Shyamalan plot twists","space aliens","petting zoos",
                   "crippling debt","silence","the true meaning of Christmas","jazz hands","spirit fingers",
                   "terms and conditions","saxophone solos"],
        # noun - PHYSICAL things / PRODUCTS (e.g., that you could buy) (PLURAL):
        "products":["dank memes","Elf on the Shelf figurines","gramophones","hi-fi stereos","jukeboxs",
                    "pinball machines","television sets","video game consoles","Instapots","Shamwows","Salad Shooters",
                    "George Foreman Grills","breadmakers","graphing calculators"],
        # INACTIVE adverb - for use BEFRE the verb:
        "directions":["slowly","cautiously","purposefully","judiciously","politely","cavalierly","sloppily","","","",
                      "","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",
                      "","","","","","","","","","","","","","",""],
        # INACTIVE adverb - for use AFTER the verb:
        "subtle_directions":[" (slowly) "," (cautiously) ","","","","","","","","","","","","","","","","","","","","",
                             "","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
        # adjective - CONDITION:
        "damaged":["damaged","superb","exquisite","adorable","beautiful","elegant","handsome","magnificent",
                   "old-fashioned","unsightly","inexpensive","delightful","fierce","crooked","colossal","miniature",
                   "immense","tiny","filthy","colossal","beat","petite","distressed","obese"],
        # adjective - ethnic/cultural group:
        "culture":["Armenian","Buddhist","Bulgarian","Cajun","Chinese","Estonian","French","Filipino","Greek",
                   "Indonesian","Japanese","Kurdish","Latvian","Lithuanian","Mexican","Polish","Pennsylvania Dutch",
                   "Pakistani","Persian","Romanian","Russian","Serbian","Slovenian","Turkish","Ukrainian",
                   "South Indian","Canadian","Mohican","British"],
        # INACTIVE adjective - numbers:
        "one_thru_nine":["1","2","3","4","5","6","7","8","9"],
        "one_thru_two":["1","2"]
    }
    return words


def message(words):
    """ This function randomly selects a word from each word-type found in the 'words' dictionary."""
    walk = random.choice(words['walk'])
    make = random.choice(words['make'])
    destabilize = random.choice(words['destabilize'])
    walking = random.choice(words['walking'])
    dance = random.choice(words['dance'])
    blog = random.choice(words['blog'])
    review = random.choice(words['review'])
    run = random.choice(words['run'])
    walker = random.choice(words['walker'])
    dog = random.choice(words['dog'])
    dogs = random.choice(words['dogs'])
    hats = random.choice(words['hats'])
    music = random.choice(words['music'])
    sandwich = random.choice(words['sandwich'])
    sandwiches = random.choice(words['sandwiches'])
    foods = random.choice(words['foods'])
    cuisine = random.choice(words['cuisine'])
    TV = random.choice(words['TV'])
    furniture = random.choice(words['furniture'])
    rallies = random.choice(words['rallies'])
    material = random.choice(words['material'])
    Reddit = random.choice(words['Reddit'])
    blogs = random.choice(words['blogs'])
    uber = random.choice(words['uber'])
    dating_service = random.choice(words['dating_service'])
    person = random.choice(words['person'])
    famous_person = random.choice(words['famous_person'])
    things = random.choice(words['things'])
    silence = random.choice(words['silence'])
    products = random.choice(words['products'])
    directions = random.choice(words['directions'])
    subtle_directions = random.choice(words['subtle_directions'])
    damaged = random.choice(words['damaged'])
    culture = random.choice(words['culture'])
    one_thru_nine = random.choice(words['one_thru_nine'])
    one_thru_two = random.choice(words['one_thru_two'])
    all_jobs = [
        "create dank memes featuring " + famous_person + " riding a " + dog,
        "post fake news stories about " + famous_person + " talking dirty to " + dogs,
        "post fake news stories about " + famous_person + "'s struggle with " + things,
        "post fake news stories about " + famous_person + "'s struggle with " + sandwiches,
        "post fake pictures of " + famous_person + " making judgemental facial expressions at " + dogs,
        "post fake pictures of " + famous_person + " " + walking + " and eating " + culture + " " + cuisine,
        "edit the " + TV + " Wikipedia page with facts about " + things,
        "edit the " + TV + " Wikipedia page with facts about " + silence,
        "edit " + famous_person + "'s Wikipedia page with facts about " + sandwiches,
        "edit " + famous_person + "'s Wikipedia page with facts about " + things,
        "edit " + dog + "-related Wikipedia pages with facts about " + silence,
        "write fan-fiction episodes of " + TV + " featuring " + person + " making " + damaged + " " + furniture,
        "write fan-fiction episodes of " + TV + " featuring " + person + " saving the day by " + walking,
        "write fan-fiction episodes of " + TV + " that focus on their struggle with " + silence,
        "write fan-fiction episodes of " + TV + " that focus on their struggle with " + foods,
        "write fan-fiction episodes of " + TV + " that focus on their struggle with " + culture + " " + cuisine,
        "post links to pictures of " + things + " in the comment section of " + blogs,
        "post unsolicited comments about " + music + " music" + " and " + culture + " " + cuisine + " in the comment section of " + blogs,
        "private-message people on " + dating_service + " about " + music + " music" + " and " + culture + " " + cuisine,
        "private-message people on " + dating_service + " about " + damaged + " " + dogs,
        "private-message people on " + dating_service + " about " + products,
        "private-message people on " + dating_service + " about " + things,
        "private-message people on " + dating_service + " about " + walking,
        "private-message people on " + dating_service + " about " + silence,
        "private-message people on " + dating_service + " about " + TV,
        "create fake " + dating_service + " profiles posing as a professional " + music + " music " + walker + " to catfish " + person,
        "create fake " + dating_service + " profiles posing as a professional " + dog + " " + walker + " to catfish " + person,
        "create fake " + dating_service + " profiles posing as a professional " + sandwich + " " + walker,
        "create fake " + dating_service + " profiles posing as a " + culture + " " + dog + " " + walker + " to catfish " + person,
        "pose as a professional " + dog + " " + walker + " on " + dating_service,
        "" + make + " " + damaged + " " + products + " for " + dogs,
        "" + run + " a Bed & Breakfast for " + dogs,
        "" + destabilize + " " + rallies + " for " + dogs,
        "" + run + " " + rallies + " about " + hats,
        "" + run + " " + rallies + " for " + dogs,
        "" + run + " " + rallies + " for " + things,
        "" + review + " " + dogs,
        "" + review + " " + music + " music",
        "" + review + " " + silence,
        "" + review + " " + foods,
        "" + review + " " + material + " " + furniture,
        "" + review + " " + things,
        "" + review + " " + silence,
        "" + blog + " about " + dogs,
        "" + blog + " about " + famous_person,
        "" + blog + " about " + music + " music" + " and " + culture + " " + cuisine,
        "" + blog + " about " + foods,
        "" + blog + " about " + walking,
        "" + blog + " about " + person,
        "" + blog + " about " + things,
        "" + blog + " about " + silence,
        "" + directions + "" + walk + " " + dogs,
        "" + directions + "" + walk + " " + things,
        "" + directions + "" + walk + " " + person,
        "" + make + " " + damaged + " " + hats + " for " + dogs,
        "" + make + " " + damaged + " " + hats + " for " + person,
        "" + make + " " + damaged + " " + things + " for " + dogs,
        "" + make + " " + damaged + " " + things + " for " + person,
        "sell " + damaged + " " + dog + " " + furniture + " to " + dogs,
        "front bands that play " + music + " music" + " for " + dogs,
        "build " + furniture + " out of " + material,
        "build " + furniture + " out of " + sandwiches,
        "" + run + " a startup company that makes " + hats + " for " + dogs,
        "" + run + " a startup company that makes " + sandwiches + " for " + dogs,
        "" + run + " a startup company that's like " + uber + ", but for " + silence,
        "" + run + " a startup company that's like " + uber + ", but for " + person,
        "" + run + " a startup company that's like " + uber + ", but for " + dogs,
        "" + run + " a startup company that's like " + uber + ", but for " + hats,
        "" + run + " a startup company that's like " + uber + ", but for " + sandwiches,
        "" + run + " a startup company that's like " + uber + ", but for " + things,
        "make " + sandwiches + " out of " + dog + " meat",
        "launch Kickstarters for smart " + furniture,
        "launch Kickstarters for " + dog + " " + hats,
        "launch Kickstarters for " + damaged + " " + products,
        "launch Kickstarters for " + damaged + " " + things
        ]
    return all_jobs


def respond_one(all_jobs,statement_preamble="I am also programmed to "):
    """This function returns a single generated message. You must pass it the 'all_jobs' object (output of internal
    function 'message()'). The default preamble ('I am also programmed to ' is pre-pended unless otherwise specified
    (other preambles I have used are 'Also, you should know that I am ', 'Aside from <activity>,
    I am ', "Also, I am '). """
    return(statement_preamble + random.choice(all_jobs))


def respond_all(all_jobs,statement_preamble="I am also programmed to "):
    """ This function returns a list ('all_messages') that contains all the defined statements. You must pass it
      the 'all_jobs' object (output of internal function 'message()'). The default preamble ('I am also programmed to ')
       is pre-pended unless otherwise specified. """
    all_messages = []
    for x in all_jobs:                     # for all items in the list...
        all_messages.append(str(statement_preamble) + x)
    return all_messages


if __name__ == '__main__':
    """ When executed stand-alone, the module will call the internal 'respond_all' function and print all the defined
    messages to the screen. """
    words = define_words()  # generate the dictionary from which to choose words and store in 'words' object.
    all_jobs = message(words)   # randomly choose one word of each word-type and create list of job statements
    all_messages = respond_all(all_jobs)    # return list of all messsages with a preable prepended
    for x in range(0, len(all_messages)):   # print all messages to screen
        print(all_messages[x])