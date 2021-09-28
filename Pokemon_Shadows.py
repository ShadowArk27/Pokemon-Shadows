
#----------------LIBRARIES---------------

import random
import time
import string
import json



#----------------------LOADING VARIABLES AND INFORMATION---------------

with open('poke.json', 'r') as f:
    pokefile = json.load(f)

#-- Charmander --
charmanderhp = pokefile[str("charmanderhp")]
charmandermove1 = pokefile[str("charmandermove1")]
charmandermove2 = pokefile[str("charmandermove2")]
charmandermove1d = pokefile[str("charmandermove1d")]
charmandermove2d = pokefile[str("charmandermove2d")]
charmandermove1t = pokefile[str("charmandermove1t")]
charmandermove2t = pokefile[str("charmandermove2t")]
charmanderlevel = pokefile[str("charmanderlevel")]
charmandertype = pokefile[str("charmandertype")]

# -- Pidgey --

pidgeyhp = pokefile[str("pidgeyhp")]
pidgeymove1 = pokefile[str("pidgeymove1")]
pidgeymove2 = pokefile[str("pidgeymove2")]
pidgeymove1d = pokefile[str("pidgeymove1d")]
pidgeymove2d = pokefile[str("pidgeymove2d")]
pidgeymove1t = pokefile[str("pidgeymove1t")]
pidgeymove2t = pokefile[str("pidgeymove2t")]
pidgeylevel = pokefile[str("pidgeylevel")]
pidgeytype = pokefile[str("pidgeytype")]

# --- Arbok --

arbokhp = pokefile[str("arbokhp")]
arbokmove1 = pokefile[str("arbokmove1")]
arbokmove2 = pokefile[str("arbokmove2")]
arbokmove1d = pokefile[str("arbokmove1d")]
arbokmove2d = pokefile[str("arbokmove2d")]
arbokmove1t = pokefile[str("arbokmove1t")]
arbokmove2t = pokefile[str("arbokmove2t")]
arboklevel = pokefile[str("arboklevel")]
arboktype = pokefile[str("arboktype")]

#Ekans

ekanshp = pokefile[str("ekanshp")]
ekansmove1 = pokefile[str("ekansmove1")]
ekansmove2 = pokefile[str("ekansmove2")]
ekansmove1d = pokefile[str("ekansmove1d")]
ekansmove2d = pokefile[str("ekansmove2d")]
ekansmove1t = pokefile[str("ekansmove1t")]
ekansmove2t = pokefile[str("ekansmove2t")]
ekanslevel = pokefile[str("ekanslevel")]
ekanstype = pokefile[str("ekanstype")]

#Caterpie

caterpiehp = pokefile[str("caterpiehp")]
caterpiemove1 = pokefile[str("caterpiemove1")]
caterpiemove2 = pokefile[str("caterpiemove2")]
caterpiemove1d = pokefile[str("caterpiemove1d")]
caterpiemove2d = pokefile[str("caterpiemove2d")]
caterpiemove1t = pokefile[str("caterpiemove1t")]
caterpiemove2t = pokefile[str("caterpiemove2t")]
caterpielevel = pokefile[str("caterpielevel")]
caterpietype = pokefile[str("caterpietype")]

#Metapod

metapodhp = pokefile[str("metapodhp")]
metapodmove1 = pokefile[str("metapodmove1")]
metapodmove2 = pokefile[str("metapodmove2")]
metapodmove1d = pokefile[str("metapodmove1d")]
metapodmove2d = pokefile[str("metapodmove2d")]
metapodmove1t = pokefile[str("metapodmove1t")]
metapodmove2t = pokefile[str("metapodmove2t")]
metapodlevel = pokefile[str("metapodlevel")]
metapodtype = pokefile[str("metapodtype")]

#Pidgeotto

pidgeottohp = pokefile[str("pidgeottohp")]
pidgeottomove1 = pokefile[str("pidgeottomove1")]
pidgeottomove1 = pokefile[str("pidgeottomove1")]
pidgeottomove1d = pokefile[str("pidgeottomove1d")]
pidgeottomove2d = pokefile[str("pidgeottomove2d")]
pidgeottomove1t = pokefile[str("pidgeottomove1t")]
pidgeottomove2t = pokefile[str("pidgeottomove2t")]
pidgeottolevel = pokefile[str("pidgeottolevel")]
pidgeottotype = pokefile[str("pidgeottotype")]



#Oddish

oddishhp = pokefile[str("oddishhp")]
oddishmove1 = pokefile[str("oddishmove1")]
oddishmove2 = pokefile[str("oddishmove2")]
oddishmove1d = pokefile[str("oddishmove1d")]
oddishmove2d = pokefile[str("oddishmove2d")]
oddishmove1t = pokefile[str("oddishmove1t")]
oddishmove2t = pokefile[str("oddishmove2t")]
oddishlevel = pokefile[str("oddishlevel")]
oddishtype = pokefile[str("oddishtype")]


#Gloom

gloomhp = pokefile[str("gloomhp")]
gloommove1 = pokefile[str("gloommove1")]
gloommove2 = pokefile[str("gloommove2")]
gloommove1d = pokefile[str("gloommove1d")]
gloommove2d = pokefile[str("gloommove2d")]
gloommove1t = pokefile[str("gloommove1t")]
gloommove2t = pokefile[str("gloommove2t")]
gloomlevel = pokefile[str("gloomlevel")]
gloomtype = pokefile[str("gloomtype")]


#Scyther

scytherhp = pokefile[str("scytherhp")]
scythermove1 = pokefile[str("scythermove1")]
scythermove2 = pokefile[str("scythermove2")]
scythermove1d = pokefile[str("scythermove1d")]
scythermove2d = pokefile[str("scythermove2d")]
scythermove1t = pokefile[str("scythermove1t")]
scythermove2t = pokefile[str("scythermove2t")]
scytherlevel = pokefile[str("scytherlevel")]
scythertype = pokefile[str("scythertype")]


#Shellder

shellderhp = pokefile[str("shellderhp")]
shelldermove1 = pokefile[str("shelldermove1")]
shelldermove2 = pokefile[str("shelldermove2")]
shelldermove1d = pokefile[str("shelldermove1d")]
shelldermove2d = pokefile[str("shelldermove2d")]
shelldermove1t = pokefile[str("shelldermove1t")]
shelldermove2t = pokefile[str("shelldermove2t")]
shellderlevel = pokefile[str("shellderlevel")]
shelldertype = pokefile[str("shelldertype")]


#Lapras

laprashp = pokefile[str("laprashp")]
laprasmove1 = pokefile[str("laprasmove1")]
laprasmove2 = pokefile[str("laprasmove2")]
laprasmove1d = pokefile[str("laprasmove1d")]
laprasmove2d = pokefile[str("laprasmove2d")]
laprasmove1t = pokefile[str("laprasmove1t")]
laprasmove2t = pokefile[str("laprasmove2t")]
lapraslevel = pokefile[str("lapraslevel")]
laprastype = pokefile[str("laprastype")]

"""
def testfunc():
    pokefile[str("arbokhp")] = 140
    pokefile[str("arbokmove1")] = "Poison Dab"

    with open ('poke.json', 'w') as f:
        json.dump(pokefile, f, indent=4)
        
    print('worked')

testfunc()
"""
    
#--------------------------------POKEMON ASCII DATABASE--------------------------------

def charmander():
    if starter == "Charmander":
        #print("You sent out Charmander")
        time.sleep(2)
        print('')
        print("NAME: Charmander")
        print('')
        print('')
        print("")
        print("                   _.--''`-.. ")
        print("                 ,'          `. ")
        print("               ,'          __  `. ")
        print("              /|          ' __   \ ")
        print("             , |           / |.   . ")
        print("             |,'          !_.'|   | ")
        print("           ,'             '   |   | ")
        print("          /              |`--'|   |  ")
        print("         |                `---'   |  ")
        print("          .   ,                   |                       ,'. ")
        print("           ._     '           _'  |                    , ' \ ` ")
        print("       `.. `.`-...___,...---''    |       __,.        ,`'   L,| ")
        print("       |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \ ")
        print("     -:..     `. `-..--_.,.<       `'      / `.        `-/ |   . ")
        print("       `,         '''''     `.              ,'         |   |  ',, ")
        print("         `.      '            '            /          '    |'. |/ ")
        print("           `.   |              \       _,-'           |       '' ")
        print("             `._'               \   ''\                .      | ")
        print("                |                '     \                `._  ,' ")
        print("                |                 '     \                 .'| ")
        print("                |                 .      \                | | ")
        print("                |                 |       L              ,' | ")
        print("                `                 |       |             /   ' ")
        print("                 \                |       |           ,'   / ")
        print("               ,' \               |  _.._ ,-..___,..-'    ,' ")
        print("              /     .             .      `!             ,j' ")
        print("             /       `.          /        .           .'/ ")
        print("            .          `.       /         |        _.'.' ")
        print("             `.          7`'---'          |------''_.' ")
        print("            _,.`,_     _'                ,''-----'' ")
        print("        _,-_    '       `.     .'      ,\ ")
        print("        -' /`.         _,'     | _  _  _.| ")
        print("         ''--'---''''''        `' '! |! / ")
        print("                                 `' ' -'  ")
        
        
    elif starter == "Charmeleon":
        print("You sent out Charmeleon")
        time.sleep(2)
        print('')
        print("NAME: Charmeleon")
        print('')
        
        print('')
        print('                          ,-"`\   ')
        print('                       _,""    j ')
        print('                __....+       /               . ')
        print('            ,-""             /               ; `-._.". ')
        print('           /                (              ,"       ." ')
        print('          |            _.    \             \   ---._ `-. ')
        print('          ,|    ,   _."  Y    \             `- ,"   \   `.`. ')
        print('          l"    \ ,"._,\ `.    .              /       ,--. l ')
        print('       .,-        `._  |  |    |              \       _   l . ')
        print('      /              `"--"    /              ."       ``. |  ) ')
        print('     .\    ,                 |                .        \ `. " ')
        print('     `.                .     |                "._  __   ;. \" ')
        print('       `-..--------..."       \                  `"  `-"".  \ ')
        print('           `......___          `._                        |  \ ')
        print('                    /`            `..                     |   . ')
        print('                   /|                `-.                  |    L ')
        print('                  / |               \   `._               .    | ')
        print('                ,"  |,-"-.   .       .     `.            /     | ')
        print('              ,"    |     "   \      |       `.         /      | ')
        print('            ,"     /|       \  .     |         .       /       | ')
        print('          ,"      / |        \  .    +          \    ,"       ." ')
        print('         .       .  |         \ |     \          \_,"        / j ')
        print('         |       |  L          `|      .          `        ," " ')
        print('         |    _. |   \          /      |           .     ." ," ')
        print('         |   /  `|    \        .       |  /        |   ," ." ')
        print('         |   ,-..\     -.     ,        | /         |,." ," ')
        print('         `. |___,`    /  `.   /`.       "          |  ." ')
        print('           "-`-"     j     ` /."7-..../|          ,`-" ')
        print('                     |        ."  / _/_|          . ')
        print('                     `,       `""/""    \          `. ')
        print('                       `,       ".       `.         | ')
        print('                  __,.-"         `.        \"       | ')
        print('                 /_,-"\          ,"        |        _. ')
        print('                  |___.---.   ,-"        .-":,-"`\," . ')
        print('                       L,.--""           "-" |  ," `-.\ ')
        print('                                             `." ')

    elif starter == "Charizard":
        print("You sent out Charizard")
        time.sleep(2)
        print('')
        print("NAME: Charizard")
        print('')
        
        print('')
        print('                      ."-,.__     ')
        print('                      `.     `.  ,     ')
        print('                   .--"  .._,""-" `.     ')
        print('                  .    ."         `"     ')
        print('                  `.   /          ,"     ')
        print('                    `  "--.   ,-""     ')
        print('                     `"`   |  \     ')
        print('                        -. \, |     ')
        print('                         `--Y."      ___.     ')
        print('                              \     L._, \     ')
        print('                    _.,        `.   <  <\                _     ')
        print('                  ," "           `, `.   | \            ( `     ')
        print('               ../, `.            `  |    .\`.           \ \_     ')
        print('              ," ,..  .           _.,"    ||\l            )  "".     ')
        print('             , ,"   \           ,".-.`-._,"  |           .  _._`.     ')
        print('           ," /      \ \        `" " `--/   | \          / /   ..\     ')
        print('         ."  /        \ .         |\__ - _ ,"` `        / /     `.`.     ')
        print('         |  "          ..         `-...-"  |  `-"      / /        . `.     ')
        print('         | /           |L__           |    |          / /          `. `.     ')
        print('        , /            .   .          |    |         / /             ` `     ')
        print('       / /          ,. ,`._ `-_       |    |  _   ,-" /               ` \     ')
        print('      / .           \"`_/. `-_ \_,.  ,"    +-" `-"  _,        ..,-.    \`.     ')
        print('     .  "         .-f    ,"   `    ".       \__.---"     _   ."   "     \ \     ')
        print('     " /          `."    l     ." /          \..      ,_|/   `.  ,"`     L`     ')
        print('     |"      _.-""` `.    \ _,"  `            \ `.___`.""`-.  , |   |    | \     ')
        print('     ||    ,"      `. `.   "       _,...._        `  |    `/ "  |   "     .|     ')
        print('     ||  ,"          `. ;.,.---" ,"       `.   `.. `-"  .-" /_ ."    ;_   ||     ')
        print('     || "              V      / /           `   | `   ,"   ," ".    !  `. ||     ')
        print('     ||/            _,-------7 "              . |  `-"    l         /    `||     ')
        print('     . |          ," .-   ," ||               | .-.        `.      ."     ||     ')
        print('      `"        ,"    `"."    |               |    `.        ". -."       `"     ')
        print('               /      ,"      |               |,"    \-.._,."/"     ')
        print('               .     /        .               .       \    .""     ')
        print('             .`.    |         `.             /         :_,"."     ')
        print('               \ `...\   _     ,"-.        ."         /_.-"     ')
        print('                `-.__ `,  `"   .  _.>----"".  _  __  /     ')
        print('                     ."        /""          |  ""   "_     ')
        print('                    /_|.-"\ ,".             "."`__"-( \     ')
        print('                      / ,"""\,"               `/  `-.|" mh     ')


    return ("")




                                #---------------------------

#----------Arbok---------------------------

def arbok():
    print("NAME: Arbok")
    print('')
  
    print('')
    print ('')
    print('                       _,.----"""""---..._                     ')
    print('                   _,-""                   `-..            ')
    print('                _,"                            `-.            ')
    print('              ,"                                  `-.            ')
    print('            ,"                                _,..._ `.            ')
    print('           /                               ,."     `:- L            ')
    print('         ,"                             |."         / ||            ')
    print('        /            _,.-._             L        .-" -,"            ')
    print('       /        _,.-"      `.            `     __   ."            ')
    print('      j      _,"           ||\|           `. ,-  _."            ')
    print('     .     ," `-..________.-" |            |" ,-"            ')
    print('     |   ." `--,.___       _,"| /`.        ` "            ')
    print('     |   |     `._  """""""   . `_Y.        Y_            ')
    print('     `._          `-...__      `.`-"        | `-,...___            ')
    print('        ``-,.._          `""--.._`.         |  /     _,+`-._            ')
    print('         ."    "--._             `-+      _ |./    ,"       \            ')
    print('        ,  _,...._  `..             `-.:L_,v-""`-./_____     L            ')
    print('       .,-"       `-.| `,                )/       \     "`   |            ')
    print('       j             |  \`\       _,......|       |       `  |            ')
    print('       |       _,.---^.v[\_   _,-"        |       |        \ "            ')
    print('       |     ,"       _>.. """            |       |        _V            ')
    print('       "    .        /  |"`\              |.._   ,"     _,"            ')
    print('        .  j       ,"    |  `._           |   `""-----""            ')
    print('         \ |      j      "     `--..,,,..j            ')
    print('          Y       |       \             /            ')
    print('           `.     |        \           /            ')
    print('             `.   `         `.      _,"            ')
    print('               `._ `.         `--.."            ')
    print('                  `---...,,,...-""            ')

    return("")



#----------------------------------------
def ekans():
    print("NAME: Ekans")
    print('')
    
    print('')
    print('')                            
    print('            _,--""""""-. ')
    print('          ,"   .,-.     `. ')
    print('         / "`...( |  |    \ ')
    print('         |      `--"        . ')
    print('         "_,...__,"          ` ')
    print('          `._                 ` ')
    print('             `..______         | ')
    print('                  |.          ,| ')
    print('                  | `-.....,-" | ')
    print('                  |            j ')
    print('                  ^.         _F ')
    print('                 /  `-.....-"/ ')
    print('                /          ," ')
    print('               /          / ')
    print('              /          / ')
    print('             j       _.-- . ')
    print('             |      /     ,+---....___ ')
    print('             L     /     /            ""`-.._ ')
    print('              \   j     j                    `-. ')
    print('               `. |     |            ."         ` ')
    print('                 `+...__|__       .,+-..         | ')
    print('                           ""`._.l      `.       j ')
    print('                           ,.-"   "-.     L    ," ')
    print('                         ,"          L    : _." ')
    print('                        /            |   _:" ')
    print('                       .            .|,-" ')
    print('                        .            `.._ ')
    print('        "\               `-.             `"-. ')
    print('      ,`."                  `-.              L ')
    print('      |  )                     `-. _...__     | ')
    print('     ."-"                         )      `.   j ')
    print('     |  |_                      _,"""`.    \ / ')
    print('      .-" `+._               _,"       `.  |/ ')
    print('       \   |  "`,,,,,....---"           | ." ')
    print('        `-."   /                        |+ ')
    print('           `--+                     _.-" ')
    print('               `--._____________.---" ')                       

    return("")            

                                
 #=---------------------------------------------=
#--------Pidgey-----

def pidgey():
    print("NAME: Pidgey")
    print('')
    #print("HP: ")
    print('                          .,                          ')
    print('                 , _.-:,:        ')
    print('               ""|"    `"""".,        ')
    print('              /:/       __.-:-"/        ')
    print('             :,:  _,--""      :-._        ')
    print('         _...`...:."""""".\""-----:        ')
    print('      ,-:          `-.) /  `.  \        ')
    print('     +---."-.    |     `.    .  \        ')
    print('          \  `.  |       \   |   L        ')
    print('           `v  ,-j        , .:   |        ')
    print('          .:\,: /        /,:      -._        ')
    print('         ,____.:        .            `-.        ')
    print('             |         /                `-.        ')
    print('            /          `.                  `-.        ')
    print('           /             `. |                 `.                  _.        ')
    print('          .                `|                 ,-.             _.-" .        ')
    print('         j                  |                 |  \         _.:    /        ')
    print('         .                  |               .:    \     ,-:      /        ')
    print('         |                  |            ,-.\      \  ,:      _.-        ')
    print('         |                . :  `.       |   `      `v:  _,.-"/        ')
    print('         ||    \          |  ` |(`:-`.,.j         \ `.-:----+---.        ')
    print('         |:|   |L    \  | |   `|   \:              L \___      /        ')
    print('         : L   |`     L | |     `.                 | j   `"""-:        ')
    print('            `-:||\    | ||j       `.       ._    ` :.        ')
    print('               `\ :"`^"- :          `.       \    |/|        ')
    print('                 `._                  `-.     \   Y |        ')
    print('         __,..-""`..`._                  `-._  `\ `.|        ')
    print('        +.....>+----.: ""----.........,--""" `--.:.:        ')
    print('            ,: _\  ,..--.-": __>---:  |        ')
    print('           --""  ":  _." }<""          `---""`._        ')
    print('                    /..."  L__.+--   _,......:..:        ')
    print('                      /.-"":/   \ ,-:        ')
    print('                          .: ,-"":        ')
    print('                         /.-:        ')
    print("")
    return("")

#-----------------------------------------------

def caterpie():
    print("NAME: Caterpie")
    print('')
    #print("HP: ")
    print('')
    print('                           _,........_           ')
    print('                    _.-"    ___    `-._       ')
    print('                 ,-"      ,"   \       `.     ')
    print('      _,...    ,"      ,-"     |  ,""":`._.     ')
    print('     /     `--+.   _,."      _.",",|"|  ` \`        ')
    print('     \_         `""     _,-""  | / `-"   l L\        ')
    print('       `"---.._      ,-"       | l       | | |       ')
    print('           /   `.   |          " `.     ," ; |     ')
    print('          j     |   |           `._`"""" ,"  |__         ')
    print('          |      `--"____          `----"    ." `.        ')
    print('          |    _,-"""    `-.                 |    \      ')
    print('          l   /             `.               F     l   ')
    print('           `./     __..._     `.           ,"      |   ')
    print('             |  ,-"      `.    | ._     _."        |  ')
    print('             . j           \   j   /`"""      __   |          ,"`.    ')
    print('              `|           | _,.__ |        ,"  `. |          |   |    ')
    print('               `-._       /-"     `L       .     , "          |   |      ')
    print('                   F-...-"          `      |    , /           |   |     ')
    print('                   |            ,----.     `..." /            |   |    ')
    print('                   .--.        j      l        ,"             |   j      ')
    print('                  j    L       |      |"-...--<               .  /   ')
    print('                  `     |       . __,,_    ..  |               \/     ')
    print('                   `-..".._  __,-"     \  |  |/`._           ,"`        ')
    print('                       |   ""       .--`. `--,  ,-`..____..,"   |     ')
    print('                        L          /     \ _.  |   | \  .-.\    j  ')
    print('                       ."._        l     .\    `---" |  |  || ,"   ')
    print('                        .  `..____,-.._."  `._       |  `--;"I"     ')
    print('                         `--"" `.            ,`-..._/__,.-1,"        ')
    print('                                 `-.__  __,."     ," ," _-"       ')
    print('                                      `"...___..`"--^--"       ')

    print("")
    return ("")



#-----------------------SPRINGFIELD CITY--------------


#-------METAPOD---------
def metapod():
    print("NAME: Metapod")
    print('')
    #print("HP: ")
    print('')

    print('                                        ,--..        ')
    print('                                       /     `.   ')
    print('                                      /|       `.   ')
    print('                                     / |        |   ')
    print('                                    /  j        |   ')
    print('                                   /  |         `   ')
    print('                                  "  ,"          \   ')
    print('                                ,"                L   ')
    print('                               /                  +   ')
    print('                             .:.                   .       ')  
    print('                          ,"`.  `.       ,..-._    +   ')
    print('                          |  |`.  L     "   _."`.   .   ')
    print('                          j  `.,\ "    | ,." |  +.  +   ')
    print('                         "`.    |,"    |" `""   / `, .   ')
    print('                        |   `"""/      `-.____."    \|   ')
    print('                      ,"|     ,"                     Y   ')
    print('                     /  |    /                      "|   ')
    print('                    /   |  ,"                     ," +   ')
    print('                   /    \-"                      /    `   ')
    print('                  /    /                       ,"      `   ')
    print('                 .     ,`"-.                 ,"         L   ')
    print('                  \   /     \               /            .   ')
    print('                     /      `               \            |   ')
    print('                   `/          _,            `          ,"   ')
    print('                    |                         `       ,"   ')
    print('                    |           ""             `.   ,"   ')
    print('                    j         -""               |`-"   ')
    print('                   /                           /"/   ')
    print('                  /           ,               / /   ')
    print('                 /            "              j /   ')
    print('               ." ___                        "/   ')
    print('               |-"   `"`-.                  "/   ')
    print('               "          \                ."   ')
    print('             ,"            l          _,.-"   ')
    print('            ,---..         |L     _.-"   ')
    print('          ,"      `.      / |  ,-"   ')
    print('         /          `  _,"  ;-"   ')
    print('       ,"--.       ,-`|  ,-"   ')
    print('      /     L   _,"  _|-"   ')
    print('     (       \-" _,-"   ')
    print('      `......^.-"   ')
    print('')

    return ("")


#---------------------------------------,ks


#------PIDGEOTTO------

def pidgeotto ():
    print("NAME: Pidgeotto")
    print('')
    #print("HP: ")
    print('')
    
    print('')
    print('                        ____ A,       ')
    print('                    _,-"\  || /`"`.   ')
    print('                   /-.   "."|    ,"-.   ')
    print('                 ."   `. |/j | ,"    ..   ')
    print('                .""|._  \` | ,"  _.,\--.   ')
    print('                "/ |  |"\\,| |,"| |  |  \   ')
    print('                |."_..|().\../()|_/\ |\ |"   ')
    print('                | |     ,"   `    L \| Y   ')
    print('                | "    /.-""-.`    |||  \   ')
    print('                . |   |_,-----.|   j||  `   ')
    print('                | .   . .     ,"  /,"/   ')
    print('              __|  \   \ \__,"/  // j   ')
    print('          _,"" ,"   `._ `.__."  ,"  |---._   ')
    print('        ,"    .        `"----"""    .     `.   ')
    print('       ,     .                       `      `   ')
    print('      /     /    ,-""""""""""""`--._  \      "   ')
    print('      |    j   ,"                   `. `     |   ')
    print('     |"."  |  /                       `.|    |   ')
    print('     | `.  /."                          \  | |   ')
    print('     L  `"v"/                            . |,|   ')
    print('      \   "|                             | " f   ')
    print('           |                             ./ /   ')
    print('       `   "                             j /   ')
    print('        `  `                            / /   ')
    print('         `. .                          / /   ')
    print('           `.`.                       /,"   ')
    print('              \`.                   ,",   ')
    print('               . `                 .-   ')
    print('                `.  +.       _,.- ,"   ')
    print('                 |`-| `"--""" `,"-|   ')
    print('                ,"  | _      _ |  |   ')
    print('        ,--...-"    `" |> <("     |-..__,..   ')
    print('      ,"    _.+- ,  +.."    `-.  .  `.___  "   ')
    print('     `-""--:-" ," |  `.       |   `..   .||_\   ')
    print('          /"|_"   `.,-|       | _.|  `-."_\ `   ')
    print('          ."        | |        ` ||   ')
    print('                     "          V"   ')
    print('')

    return("")


#0------------


#-----------PIDGEOT
def pidgeot():
    print("NAME: Pidgeot")
    print('')
    #print("HP: ")
    print('')
    print('                        ..-`"-._       ')
    print('                      ,"      ,"`.   ')
    print('                    ,f \   . / ,-"-.   ')
    print('                   "  `. | |  , ,"`|   ')
    print('                  `.-.  \| | ,." ,-.\   ')
    print('                   /| |. ` | /.""||Y .   ')
    print('                  . |_|U_\.|//_U_||. |   ')
    print('                  | j    /   .    \ |"   ')
    print('                   L    /     \    .j`   ')
    print('                    .  `"`._,--|  //  \   ')
    print('                    j   `.   ,"  , \   L   ')
    print('               ____/      `""     \ L  |   ')
    print('            ,-"   ,"               \|"-+.   ')
    print('           /    ,"                  .    \   ')
    print('          /    /                     `    `.   ')
    print('         . |  j                       \     \   ')
    print('         |F   |                        "   \ .   ')
    print('         ||  F                         |   |\|   ')
    print('         ||  |                         |   | |   ')
    print('         ||  |                         |   | |   ')
    print('         `.._L                         |  ," "   ')
    print('          .   |                        |,| ,"   ')
    print('           `  |                    "|||  j/   ')
    print('            `."    .             ,"   /  "   ')
    print('              \\    `._        ,"    / ,"   ')
    print('               .\         ._ ,"     /,"   ')
    print('                 .  ,   ."| \  (   //   ')
    print('                 j_|"_,"  |  ._"` / `.   ')
    print('                " |  |    |   |  Y    `.   ')
    print('         ,.__  `; |  |-"""^""""  |.--""`   ')
    print('      ,--\   """ ,    \  / \ ,-     """"---.   ')
    print('     ".--`v.=:.-"  .  L."`"""\   ,  `.,.._ /`.   ')
    print('          .L    j-"`.   `\    j  |`.  ""--""`-"   ')
    print('          / |_,"    L ,-.|   (/`.)  `-\.-"\   ')
    print('         `-""        `. |     l /     `-"`-"   ')
    print('                       `      `-   ')
    return("")

#-------------------------------------------

#---------GLOOM

def gloom():
    print("NAME: Gloom")
    print('')
    #print("HP: ")
    print('')
    print('                                ,.--""+`-,     ')
    print('                         ___,..-"  C"  `." `-.     ')
    print('                      ."|      `-,...._   ___:.     ')
    print('                     /""|   _,..^..__ _"""     `-.     ')
    print('                    " `" ,-`c.   ..  `.     ,"".  `.     ')
    print('                   /,  ,"       `._"   `.|)  ""    /\           ')     
    print('               _,.|"- /  .-.             \         `".          |\     ')
    print('           _.-"   |  |   "-        _     |           |          | \     ')
    print('         ,"       |  |            \."    |           |          |  .     ')
    print('        ,          . |                   |           j          j  |     ')
    print('       /_.-""""""":.+|                   |          /         ,"   |     ')
    print('      /"       ,-"    \                 /        _,"-..___,.."     j     ')
    print('     j|       /        `.             ,^.......-+                 /     ')
    print('     ||      /     _,-."""-..____,..-"-._        \               /     ')
    print('     | \   ,|    ," ."   ,"    .         `.       \__         ,-"     ')
    print('      . `-".|   /  /  _."       `.         \       . `---+.-"|     ')
    print('       `._, " j   j ""            `--..     `.     |.     `. |     ')
    print('             .|   |                           .    ||       `|     ')
    print('             `"   |,----......__...._         "    ||        |     ')
    print('                  |`._=-=====___""-. `-.      |   / |        "     ')
    print('               _,.L   `"""------|  .---"      |  /`-+_     ')
    print('          ,""`/    \            |  |          |.".    `"""-.     ')
    print('          |   \__,."`           | j              _+-._     |     ')
    print('          |    `     `._        | |             ,     `---"     ')
    print('           .    `...,-" +._      `|            /     ')
    print('            `.       -""   `-...________,..--.  `.,..     ')
    print('              \     |                         `.     |     ')
    print('               `._  |                          "    /     ')
    print('                  `"                      _,.-"    /     ')
    print('                                       ,-"        /     ')
    print('                                      `.       _,"     ')
    print('                                        `"----" mh     ')
    return("")

#---------SCYTHER

def scyther():
    print('')
    #print("HP: ")
    print('')
    print('                ______     ')
    print('            _.-"______`._             ,.    ')
    print('          ,"_,""      `-.`._         /.|    ')
    print('        ,","   ____      `-.`.___   // |    ')
    print('       /." ,-""    `-._     `.   | j.  |  /|    ')
    print('      // ."   __...._  `"--.. `. " |   | " "    ')
    print('     j/  _.-""       `._,."".   |  |   |/ "    ')
    print('     |.-"                    `."/| |   | /    ')
    print('     "                        "/ | |   |/    ')
    print('                              /  " "   "    ')
    print('                        |.   ` ."/.   /    ')
    print('                        | `. ,",".  ,"    ')
    print('                        |   \." j.-"/    ')
    print('                        "   "   ". /    ')
    print('                       |          `"-...__    ')
    print('                       |             _..-"    ')
    print('                      ,|"      __.-7"   _......____    ')
    print('                     . |    ,"/   ,"`."__........___`-...__    ')
    print('                      .    "-"_.." .-""-._         `"""-----`---...___    ')
    print('                      |____.-","" /      /`.._,"".                 _.-"    ')
    print('                   ,"`| ,"   "   |      .,--. ;--|             _,-"    ')
    print('                  |   ".| `-.|   `.     ||   /   "`---.....--"".    ')
    print('                  "     `._  |     `+----`._;".   `-..____..--""    ')
    print('                   `.    | ""|__...-|,|       /     `.    ')
    print('                     |-..|`-.7    /   "      /   |  "|    ')
    print('                     " |" `.||`--"    |      \   | . |    ')
    print('                             |        |       \  " | |    ')
    print('                             `.      ."        .   " "    ')
    print('                               `"-+-"|`.       "  " /    ')
    print('                                  |`-"  \     /  /."    ')
    print('                                  `   _ ,.   / ,"/    ')
    print('                                   ||"."`.  / /,"    ')
    print('                                    `      " ."    ')
    print('                                          /." mh    ')
    return("")

#----------VILEPLUME

def vileplume():
    print('')
    #print("HP: ")
    print('')
    print('                             _..--------..__     ')
    print('                         ,-""    __         `-.     ')
    print('                      ,-"    .-""  |   .--.    `. ____     ')
    print('                    ,"  _..   `""""    `-"  _.-"""    `"--._     ')
    print('                  ."   `.."  _           _," ,""`,        __`._     ')
    print('           _.--"""`"---.._  "."   ___..,"__   `""        `. `. `.     ')
    print('         ."__       .-,   `"-+.--"-------..`-.   `=`       `""   \     ')
    print('       ,"(__,"   _   "       |( ,-"""""""`-.`,|  _.----""""`--.../     ')
    print('      /         |_)          | `-...______,." |-"        `-"      `-.     ')
    print('     j                      ."_,..........__,"     c.          .-.   `.     ')
    print('     |        _,..  `+" _,.-""        .,    `-._               \__"    `     ')
    print('     |       `___,"   ,"   .:"",     ""    .-,  `-.     ,--.      _     |     ')
    print('      \             ,"       ""             `      `.   `--"    ," |    |     ')
    print('       `.         ,"  ."""`.          :",       __   \          `.."    "     ')
    print('         `._     .    `---"            "       |  `.  \               ,"     ')
    print('            `"--+                   __          `""    .           _,"     ')
    print('                |                 ("  )                |...,,...-""     ')
    print('                 `.                 ""                ,"     ')
    print('                   `-..__                          _,"     ')
    print('                         `+---.=,---------+.----+""     ')
    print('                     ,""`/     "          "   ,-.\     ')
    print('                     \    \         _        /  | +.     ')
    print('                    .`.            "/       /   | | \     ')
    print('                  ,"   A   "               /    j |  `.     ')
    print('                 "    / \   \             j    / /`.   \     ')
    print('                  `--"   \   \            |   j,"   `.,"     ')
    print('                           . |-.........,.|   .     ')
    print('                            `"            `,." mh     ')
    return("")

#-----------ODDISH

def oddish():
    print('')
    #print("HP: ")
    print('')
    print('                                 .-"--.__     ')    
    print('               _                / "+.--"     ')
    print('                \.-._          j / |     ')
    print('                 \`-.`._      . j  |     ')
    print('                  \  `. `.    | |  L                        _,,--+="     ')
    print('                   L   `. `-. | |   \                  _.-+"    /     ')
    print('                   |     \   j  |    \            _,-"" ."    ,"     ')
    print('                   .      \  |  |     \         ,"   _,"    ,"     ')
    print('                    \      `j   |      \      ."   ,"      /     ')
    print('                     `.     |   |       \   ,"   ,"       /     ')
    print('                       \    |   |        \ /    /        /     ')
    print('       _,-""""""""""""`--. j    |         V    /      _,+............._     ')
    print('     -=`...-----...__     `|    |         .   /   _.-"        _,.--"",..=.     ')
    print('           `-.       `._   |    |          L,"  ,"       _,.-"    ,-"     ')
    print('              `.        `. |    |          |  ."     _.-"       ,"     ')
    print('                 .        \|    "          L/    _,-"          /     ')
    print('                  `._      `.    L        /   _,"            ,"     ')
    print('                     `-._    \   `       ," ,"             ,"     ')
    print('                         `-.. `   \     /,-"           _.-"     ')
    print('                           ,""-..  .   /_,..---"`+"""""     ')
    print('                          /           "           `.     ')
    print('                         j                          .     ')
    print('                        .                           |     ')
    print('                        |   .-.       ,.            |     ')
    print('                        |    -"       `."           |     ')
    print('                        `                           "     ')
    print('                         `.      .--.             ,"     ')
    print('                           `.    `._|          ,-"     ')
    print('                         _.-`   ,..______.. .  `-.     ')
    print('                       ,"       |          |      `.     ')
    print('                     ,"         "          |        `.     ')
    print('                    /         ,"            .         .     ')
    print('                    \     _,-"               `._      |     ')
    print('                     `---"                      `-...." mh     ')
    return("")


#-------------------------CRYSTAL GLADES----------------------#


#----------SHELLDER

def shellder():
    print('')
    #print("HP:")
    print('')              
    print('                   _,.-""""""--..._   ')
    print('                _,-"               `."-.._  ')
    print('              ."     _..-"""""--._   `.   `-._  ')
    print('            ,"   _.-"             `._  `.     `-._  ')
    print('           /   .`                    `.  \        `.  ')
    print('          /  ."                        `. `.        `.       _,..  ')
    print('        ."  /                            `. `.        `...-""    \  ')
    print('       /   /                               _. `.               ,-"  ')
    print('      j   /                   ,-"""`.   ,""  `. `.           ."  ')
    print('      |  .     _..------...__"  "   |  |   "   |  `.       ,"  ')
    print('      `._...-""_,.-""        `..__,"    `._ _,."`.  `    ."\  ')
    print('        ,"  _,"             __..-"""`"".  ,"    `..  `.     .  ')
    print('      ,"  ."        _..-""""            \/        `.   \    "  ')
    print('     :         _..+"----""               `.         `.  \    \  ')
    print('     :      _,"    `-._                               \  \    \  ')
    print('      `...-"           `.                              \  \  ')
    print('                         \                              \  \   .  ')
    print('                          \                              .     "  ')
    print('                         / \                    .        "  `  :  ')
    print('                       ,"   \               .    \        \  \  `-,._  ')
    print('                     ,"    __\               \    \        \  \  /._ `.  ')
    print('                    .  _.""   \               \    \        `._"/._ "-.\  ')
    print('                     `"        `.              `._."        ,".-.. `-._ `  ')
    print('                                 `-._                    _.".  `,"`-._ `.`  ')
    print('                                     `--...__     ___..-"  \ `. "     `._`|  ')
    print('                                             `"""" \   :    \  `.`.      "  ')
    print('                                                    \  :     `   `.`.  ')
    print('                                                     "":      `.__,."  ')
    print('                                                       `-....."  ')
    print('')
    return("")


#--------Lapras

def lapras():
    print("                                       ,|")
    print("                                       ||")
    print("                               ,-''''`' `._")
    print("                              '----.     __`....._")
    print("                               `    `.  `. ;      `.")
    print("                                `.    `.  `   ,'`. |")
    print("                                  `.  _.`._   |  ' |")
    print("                                  .','  ,' `.  `--'")
    print("                                 /.' _,'    | /")
    print("                                '/_.'       |.")
    print("                                 `---`'.    ||")
    print("                                       |    ||")
    print("                                      ,'    `|")
    print("                         _           /       |")
    print("                        ' `.        .'       |")
    print("                         .  `._  _,'/|       |")
    print("                        _|     ''  / |       '")
    print("                    _,-' |        /  '        .")
    print("                 |''            ,'  '          \ ")
    print("                 |   _        ,'   /            \ ")
    print("                 ;  '        /    j              .")
    print("            ,'--'    `.    .      |              |         ________")
    print("            `.   -.       / '     |              |   _,-'''   __.._'`-._")
    print("             ,' ,-.`-.__.' /      '              |.-'  _..--''       _.-'")
    print("             \.'   `-.___.'      ,               '__.-'           _.'")
    print("             /        _..--    . |              /               ,'")
    print("           ,`      .-'         | |           _,'._          _,-'")
    print("       _,-'      ,'           .' '       _.-'     '-.....-''")
    print("     ,'     __ ,'          _.'  /  __..-'")
    print("   ,' _.-'''  /         _.'  _.'-''")
    print("  '-''       /      _.-' _.-'")
    print("            /    _.' _.-'")
    print("           .   .'_.-'")
    print("           | ,'.'")
    print("           | .`")
    print("            `")
    return("")



#------POKEMON TIERS------

basic_list = ['Ekans', 'Pidgey', 'Caterpie', 'Metapod', 'Oddish', 'Shellder', 'Dratini', 'Magikarp', 'Pikachu', 'Abra']

basic = ['1', '2', '2', '2']

good_list = ['Arbok', 'Pidgeotto', 'Gloom', 'Cloyster', 'Dragonair', 'Growlithe', 'Raichu', 'Kadabra', 'Haunter' ]

good = ['1', '2', '2', '2']

amazing_list = ['Beedrill', 'Pidgeot', 'Vileplume', 'Scyther', 'Dragonite', 'Arcanine', 'Gyarados',
                'Lapras', 'Alakazam', 'Snorlax', 'Gengar', 'Nidoking', 'Nidoqueen', 'Lapras' ]

amazing = ['1', '2', '2']

legendary_list = ['Articuno', 'Moltres', 'Zapdos']

legendary = ['1', '1', '2']






#------- LOCATION LISTS ---------

location = "Aurora Hills"

hills_list = [ 'Caterpie', 'Caterpie', 'Pidgey', 'Pidgey', 'Ekans', 'Ekans']

spring_list = ['Pidgey', 'Pidgey', 'Pidgey', 'Caterpie',  'Caterpie', 'Caterpie',  'Pidgeotto', 'Pidgeotto', 'Metapod', 'Metapod']

wilds_list = ['Oddish', 'Gloom', 'Scyther', 'Arbok']

crystal_list = ['Lapras']





#--- POKEDEX AND PARTY ---

pokedex_list = ['Charmander']

party_list = ['Charmander']

pc_list = ['Charmander']





#------ HP LIST -------

high_list = ['1', '2', '1']

low_list = ['1', '2', '2', '2']





#--------- POKEBALL LISTS ---------

pokeball_list = ['1', '2', '2']

greatball_list = ['1', '1', '2', '2', '2']

ultraball_list = ['1', '2', '2', '2']

masterball_list = ['2']





# ---------------- STATS AND SWAPPING FUNCTIONS -------------


swap = "Charmander"

possibles = globals().copy()
possibles.update(locals())





hpcarrier = 0


#------------------------POKEMON STATS DATA BASE--------------------------

#---AURORA HILLS POKEMON---
#Ekans

ekans_list = ["Bite", "Acid"]

#Arbok


arbok_list = ["Bite", "Poison Jab"]

#Caterpie


caterpie_list = ["Tackle", "Bug Bite" ]

#Pidgey


pidgey_list = ["Tackle", "Gust"]

hpcarrier = 0

#-----SPRINGFIELD CITY-----

#Metapod


metapod_list = ['Tackle', 'Tackle']

#Pidgeotto


pidgeotto_list = ['Quick Attack', 'Peck']

#Pidgeot


pidgeot_list = ['Air Slash', 'Sky Attack']




#-------TEMPEST WILDS------

#Gloom


gloom_list = ['Acid', 'Razor Leaf']

#Oddish


oddish_list = ['Acid', 'Leech Seed']

#Scyther


scyther_list = ['Fury Cutter', 'X Scissor']

#Vileplume


vileplume_list = ['Petal Blizzard', 'Sludge Wave']




#---------CRYSTAL GLADES---------

#Shellder


shellder_list = ['Water Gun', 'Ice Shard']


#Lapras

lapras_list = ['Ice Beam', 'Surf']


#--------------- VARIABLES -----------

starter = "Charmander"

starterlevel = 5

#Charmander
charmanderhp = 12

charmanderhpn = 12

pokemonhp = charmanderhp

pokemonhpn = pokemonhp

move1 = "Scratch"

move2 = "Ember"

move1t = "normal"

move2t = "fire"

move1d = 3

move2d = 4



level = starterlevel

stype = "fire"

ctype = "fire"

coke = "Charmander"

current = "Charmander"

bus = "oug"


#POKEBALLS
          
pokeball = 9

greatball = 10

ultraball = 5

masterball = 1

         
#----Loops----

bushing = False

running = True

battling = False

attacking = False

evolving = True

evolving2 = True

catching = False

balling = False

swapping = False
enemy = "hah"

used = "none"

status = "ok"

#-----------------SAVE FUNCTION-------------------

def save():
    global current
    with open('poke.json', 'r') as f:
        pokefile = json.load(f)
    print("Saving......")

    possibles = globals().copy()
    possibles.update(locals())     
    returnmethod = possibles.get(current)
    returnmethod()

    #-- Charmander --
    pokefile[str("charmanderhp")] = charmanderhp
    pokefile[str("charmandermove1")] = charmandermove1 
    pokefile[str("charmandermove2")] = charmandermove2  
    pokefile[str("charmandermove1d")] = charmandermove1d  
    pokefile[str("charmandermove2d")] = charmandermove2d  
    pokefile[str("charmandermove1t")] = charmandermove1t  
    pokefile[str("charmandermove2t")] = charmandermove2t  
    pokefile[str("charmanderlevel")] = charmanderlevel 
    pokefile[str("charmandertype")] = charmandertype


    # -- Pidgey --

    pokefile[str("pidgeyhp")] = pidgeyhp  
    pokefile[str("pidgeymove1")] = pidgeymove1  
    pokefile[str("pidgeymove2")] = pidgeymove2  
    pokefile[str("pidgeymove1d")] = pidgeymove1d  
    pokefile[str("pidgeymove2d")] = pidgeymove2d  
    pokefile[str("pidgeymove1t")] = pidgeymove1t  
    pokefile[str("pidgeymove2t")] = pidgeymove2t  
    pokefile[str("pidgeylevel")] = pidgeylevel  
    pokefile[str("pidgeytype")] = pidgeytype  

    # --- Arbok --

    pokefile[str("arbokhp")] = arbokhp  
    pokefile[str("arbokmove1")] = arbokmove1  
    pokefile[str("arbokmove2")] = arbokmove2  
    pokefile[str("arbokmove1d")] = arbokmove1d  
    pokefile[str("arbokmove2d")] = arbokmove2d  
    pokefile[str("arbokmove1t")] = arbokmove1t  
    pokefile[str("arbokmove2t")] = arbokmove2t  
    pokefile[str("arboklevel")] = arboklevel  
    pokefile[str("arboktype")] = arboktype  

    #Ekans

    pokefile[str("ekanshp")] = ekanshp  
    pokefile[str("ekansmove1")] = ekansmove1  
    pokefile[str("ekansmove2")] = ekansmove2  
    pokefile[str("ekansmove1d")] = ekansmove1d  
    pokefile[str("ekansmove2d")] = ekansmove2d 
    pokefile[str("ekansmove1t")] = ekansmove1t 
    pokefile[str("ekansmove2t")] = ekansmove2t 
    pokefile[str("ekanslevel")] = ekanslevel  
    pokefile[str("ekanstype")] = ekanstype  

    #Caterpie

    pokefile[str("caterpiehp")] = caterpiehp
    pokefile[str("caterpiemove1")] = caterpiemove1 
    pokefile[str("caterpiemove2")] = caterpiemove2  
    pokefile[str("caterpiemove1d")] = caterpiemove1d  
    pokefile[str("caterpiemove2d")] = caterpiemove2d  
    pokefile[str("caterpiemove1t")] = caterpiemove1t  
    pokefile[str("caterpiemove2t")] = caterpiemove2t  
    pokefile[str("caterpielevel")] = caterpielevel  
    pokefile[str("caterpietype")] = caterpietype  

    #Metapod

    pokefile[str("metapodhp")] = metapodhp  
    pokefile[str("metapodmove1")] = metapodmove1  
    pokefile[str("metapodmove2")] = metapodmove2  
    pokefile[str("metapodmove1d")] = metapodmove1d  
    pokefile[str("metapodmove2d")] = metapodmove2d  
    pokefile[str("metapodmove1t")] = metapodmove1t  
    pokefile[str("metapodmove2t")] = metapodmove2t  
    pokefile[str("metapodlevel")] = metapodlevel  
    pokefile[str("metapodtype")] = metapodtype 

    #Pidgeotto

    pokefile[str("pidgeottohp")] = pidgeottohp  
    pokefile[str("pidgeottomove1")] = pidgeottomove1  
    pokefile[str("pidgeottomove1")] = pidgeottomove1  
    pokefile[str("pidgeottomove1d")] = pidgeottomove1d  
    pokefile[str("pidgeottomove2d")] = pidgeottomove2d  
    pokefile[str("pidgeottomove1t")] = pidgeottomove1t  
    pokefile[str("pidgeottomove2t")] = pidgeottomove2t  
    pokefile[str("pidgeottolevel")] = pidgeottolevel  
    pokefile[str("pidgeottotype")] = pidgeottotype  



    #Oddish

    pokefile[str("oddishhp")] = oddishhp  
    pokefile[str("oddishmove1")] = oddishmove1  
    pokefile[str("oddishmove2")] = oddishmove2  
    pokefile[str("oddishmove1d")] = oddishmove1d  
    pokefile[str("oddishmove2d")] = oddishmove2d  
    pokefile[str("oddishmove1t")] = oddishmove1t
    pokefile[str("oddishmove2t")] = oddishmove2t  
    pokefile[str("oddishlevel")] = oddishlevel  
    pokefile[str("oddishtype")] = oddishtype  


    #Gloom

    pokefile[str("gloomhp")] = gloomhp   
    pokefile[str("gloommove1")] = gloommove1   
    pokefile[str("gloommove2")] = gloommove2 
    pokefile[str("gloommove1d")] = gloommove1d 
    pokefile[str("gloommove2d")] = gloommove2d 
    pokefile[str("gloommove1t")] = gloommove1t 
    pokefile[str("gloommove2t")] = gloommove2t 
    pokefile[str("gloomlevel")] = gloomlevel 
    pokefile[str("gloomtype")] = gloomtype 


    #Scyther

    pokefile[str("scytherhp")] = scytherhp  
    pokefile[str("scythermove1")] = scythermove1 
    pokefile[str("scythermove2")] = scythermove2 
    pokefile[str("scythermove1d")] = scythermove1d 
    pokefile[str("scythermove2d")] = scythermove2d 
    pokefile[str("scythermove1t")] = scythermove1t
    pokefile[str("scythermove2t")] = scythermove2t 
    pokefile[str("scytherlevel")] = scytherlevel 
    pokefile[str("scythertype")] = scythertype 


    #Shellder

    pokefile[str("shellderhp")] = shellderhp 
    pokefile[str("shelldermove1")] = shelldermove1 
    pokefile[str("shelldermove2")] = shelldermove2 
    pokefile[str("shelldermove1d")] = shelldermove1d 
    pokefile[str("shelldermove2d")] = shelldermove2d 
    pokefile[str("shelldermove1t")] = shelldermove1t 
    pokefile[str("shelldermove2t")] = shelldermove2t
    pokefile[str("shellderlevel")] = shellderlevel 
    pokefile[str("shelldertype")] = shelldertype 


    #Lapras

    pokefile[str("laprashp")] = laprashp 
    pokefile[str("laprasmove1")] = laprasmove1 
    pokefile[str("laprasmove2")] = laprasmove2 
    pokefile[str("laprasmove1d")] = laprasmove1d 
    pokefile[str("laprasmove2d")] = laprasmove2d 
    pokefile[str("laprasmove1t")] = laprasmove1t 
    pokefile[str("laprasmove2t")] = laprasmove2t 
    pokefile[str("lapraslevel")] = lapraslevel 
    pokefile[str("laprastype")] = laprastype

    with open ('poke.json', 'w') as f:
        json.dump(pokefile, f, indent=4)




    print('')
    print("Saved!!!")


#-------#
    


        
#---- POKEMON RETURNER FUNCTIONS  ----

def Charmander():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype, charmanderhp, charmandermove1, charmandermove2, charmandermove1d, charmandermove2d, charmandermove1t, charmandermove2t, charmanderlevel, charmandertype

    charmanderhp = pokemonhp
    charmandermove1 = move1
    charmandermove2 = move2
    charmandermove1d = move1d
    charmandermove2d = move2d
    charmandermove1t = move1t
    charmandermove2t = move2t
    charmanderlevel = level
    charmandertype = ctype

def Pidgey():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype, pidgeyhp, pidgeymove1, pidgeymove2, pidgeymove1d, pidgeymove2d, pidgeymove1t, pidgeymove2t, pidgeylevel, pidgeytype

    pidgeyhp = pokemonhp
    pidgeymove1 = move1
    pidgeymove2 = move2
    charmandermove1d = move1d
    charmandermove2d = move2d
    charmandermove1t = move1t
    charmandermove2t = move2t
    charmanderlevel = level
    charmandertype = ctype

def Ekans():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global ekanshp, ekansmove1, ekansmove2, ekansmove1d, ekansmove2d, ekansmove1t, ekansmove2t, ekanslevel, ekanstype

    ekanshp = pokemonhp
    ekansmove1 = move1
    ekansmove2 = move2
    ekansmove1d = move1d
    ekansmove2d = move2d
    ekansmove1t = move1t
    ekansmove2t = move2t
    ekanslevel = level
    ekanstype = ctype
    
def Arbok():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global arbokhp, arbokmove1, arbokmove2, arbokmove1d, arbokmove2d, arbokmove1t, arbokmove2t, arboklevel, arbokstype

    arbokhp = pokemonhp
    arbokmove1 = move1
    arbokmove2 = move2
    arbokmove1d = move1d
    arbokmove2d = move2d
    arbokmove1t = move1t
    arbokmove2t = move2t
    arboklevel = level
    arboktype = ctype

def Pidgeotto():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global pidgeottohp, pidgeottomove1, pidgeottomove2, pidgeottomove1d, pidgeottomove2d, pidgeottomove1t, pidgeottomove2t, pidgeottolevel, pidgeottostype

    pidgeottohp = pokemonhp
    pidgeottomove1 = move1
    pidgeottomove2 = move2
    pidgeottomove1d = move1d
    pidgeottomove2d = move2d
    pidgeottomove1t = move1t
    pidgeottomove2t = move2t
    pidgeottolevel = level
    pidgeottotype = ctype


def Caterpie():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global caterpiehp, caterpiemove1, caterpiemove2, caterpiemove1d, caterpiemove2d, caterpiemove1t, caterpiemove2t, caterpielevel, caterpiestype

    caterpiehp = pokemonhp
    caterpiemove1 = move1
    caterpiemove2 = move2
    caterpiemove1d = move1d
    caterpiemove2d = move2d
    caterpiemove1t = move1t
    caterpiemove2t = move2t
    caterpielevel = level
    caterpietype = ctype
     

def Metapod():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global metapodhp, metapodmove1, metapodmove2, metapodmove1d, metapodmove2d, metapodmove1t, metapodmove2t, metapodlevel, metapodstype

    metapodhp = pokemonhp
    metapodmove1 = move1
    metapodmove2 = move2
    metapodmove1d = move1d
    metapodmove2d = move2d
    metapodmove1t = move1t
    metapodmove2t = move2t
    metapodlevel = level
    metapodtype = ctype

    
def Oddish():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global oddishhp, oddishmove1, oddishmove2, oddishmove1d, oddishmove2d, oddishmove1t, oddishmove2t, oddishlevel, oddishstype

    oddishhp = pokemonhp
    oddishmove1 = move1
    oddishmove2 = move2
    oddishmove1d = move1d
    oddishmove2d = move2d
    oddishmove1t = move1t
    oddishmove2t = move2t
    oddishlevel = level
    oddishtype = ctype


def Gloom():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global gloomhp, gloommove1, gloommove2, gloommove1d, gloommove2d, gloommove1t, gloommove2t, gloomlevel, gloomstype

    gloomhp = pokemonhp
    gloommove1 = move1
    gloommove2 = move2
    gloommove1d = move1d
    gloommove2d = move2d
    gloommove1t = move1t
    gloommove2t = move2t
    gloomlevel = level
    gloomtype = ctype

def Scyther():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global scytherhp, scythermove1, scythermove2, scythermove1d, scythermove2d, scythermove1t, scythermove2t, scytherlevel, scytherstype

    scytherhp = pokemonhp
    scythermove1 = move1
    scythermove2 = move2
    scythermove1d = move1d
    scythermove2d = move2d
    scythermove1t = move1t
    scythermove2t = move2t
    scytherlevel = level
    scythertype = ctype

def Shellder():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global shellderhp, shelldermove1, shelldermove2, shelldermove1d, shelldermove2d, shelldermove1t, shelldermove2t, shellderlevel, shellderstype

    shellderhp = pokemonhp
    shelldermove1 = move1
    shelldermove2 = move2
    shelldermove1d = move1d
    shelldermove2d = move2d
    shelldermove1t = move1t
    shelldermove2t = move2t
    shellderlevel = level
    shelldertype = ctype

def Lapras():
    global swap, current, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype
    global laprashp, laprasmove1, laprasmove2, laprasmove1d, laprasmove2d, laprasmove1t, laprasmove2t, lapraslevel, laprasstype

    laprashp = pokemonhp
    laprasmove1 = move1
    laprasmove2 = move2
    laprasmove1d = move1d
    laprasmove2d = move2d
    laprasmove1t = move1t
    laprasmove2t = move2t
    lapraslevel = level
    laprastype = ctype

    

#----------- POKEMON SWAPPER FUNCTION -------- 


def swapper():
    global swap, current, pokemonhpn, pokemonhp, move1, move2, move1d, move2d, move1t, move2t, level, ctype





    # --- RETURNING THE VALUES ---
    possibles = globals().copy()
    possibles.update(locals())     
    returnmethod = possibles.get(current)
    returnmethod()




    # --- CREATING THE NEW VALUES ---          
    pokehp = possibles.get(swap.lower() + 'hp')
    pokemove1 = possibles.get(swap.lower() + 'move1')
    pokemove2 = possibles.get(swap.lower() + 'move2')
    pokemove1d = possibles.get(swap.lower() + 'move1d')
    pokemove2d = possibles.get(swap.lower() + 'move2d')
    pokemove1t = possibles.get(swap.lower() + 'move1t')
    pokemove2t = possibles.get(swap.lower() + 'move2t')
    pokelevel = possibles.get(swap.lower() + 'level')
    poketype = possibles.get(swap.lower() + 'type')





    # -- BORROWING THE NEW VALUES - 
    pokemonhp = pokehp
    move1 = pokemove1
    move2 = pokemove2
    move1d = pokemove1d
    move2d = pokemove2d
    move1t = pokemove1t
    move2t = pokemove2t
    level = pokelevel
    ctype = poketype


    #-----ENSURING STORAGE VALUES ARE SET UP-----

    pokemonhpn = pokemonhp

    
    

    
    


#--- BEEPING FUNCTION ----
def beeping():
    print('')
    time.sleep(1)
    print('1...')
    print('')
    time.sleep(1)
    print('2....')
    print('')
    time.sleep(1)
    print('3......')
    print('')
    time.sleep(3)

#------------------- SAVE FUNCTION -----------------




    

#------------------- TYPE EFFECTIVENESS -----------------

#ATTACKING
def effect(movet, ptype, effecthp, damage):

    global hpcarrier
    if movet == "normal" and ptype == "rock":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "normal" and ptype == "ghost":
        effecthp = (effecthp - damage * 0)

    elif movet == "normal" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "bug":
        effecthp = (effecthp - damage * 2)

    elif movet == "fire" and ptype == "water":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "grass":
        effecthp = (effecthp - damage * 2)

    elif movet == "fire" and ptype == "rock":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "ground":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "dragon":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fire" and ptype == "ice":
        effecthp = (effecthp - damage * 2)

    elif movet == "water" and ptype == "fire":
        effecthp = (effecthp - damage * 2)

    elif movet == "water" and ptype == "water":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "water" and ptype == "grass":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "water" and ptype == "ground":
        effecthp = (effecthp - damage * 2)

    elif movet == "water" and ptype == "rock":
        effecthp = (effecthp - damage * 2)

    elif movet == "water" and ptype == "dragon":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "water":
        effecthp = (effecthp - damage * 2)

    elif movet == "grass" and ptype == "grass":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "poison":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "ground":
        effecthp = (effecthp - damage * 2)

    elif movet == "grass" and ptype == "flying":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "bug":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "grass" and ptype == "rock":
        effecthp = (effecthp - damage * 2)

    elif movet == "electric" and ptype == "water":
        effecthp = (effecthp - damage * 2)

    elif movet == "electric" and ptype == "electric":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "electric" and ptype == "grass":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "electric" and ptype == "ground":
        effecthp = (effecthp - damage * 0)

    elif movet == "electric" and ptype == "flying":
        effecthp = (effecthp - damage * 2)

    elif movet == "electric" and ptype == "dragon":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ice" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ice" and ptype == "water":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ice" and ptype == "grass":
        effecthp = (effecthp - damage * 2)

    elif movet == "ice" and ptype == "ice":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ice" and ptype == "ground":
        effecthp = (effecthp - damage * 2)

    elif movet == "ice" and ptype == "flying":
        effecthp = (effecthp - damage * 2)

    elif movet == "ice" and ptype == "dragon":
        effecthp = (effecthp - damage * 2)

    elif movet == "ice" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fighting" and ptype == "normal":
        effecthp = (effecthp - damage * 2)

    elif movet == "fighting" and ptype == "ice":
        effecthp = (effecthp - damage * 2)

    elif movet == "fighting" and ptype == "poison":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fighting" and ptype == "flying":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fighting" and ptype == "psychic":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fighting" and ptype == "bug":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fighting" and ptype == "rock":
        effecthp = (effecthp - damage * 2)

    elif movet == "fighting" and ptype == "ghost":
        effecthp = (effecthp - damage * 0)

    elif movet == "fighting" and ptype == "dark":
        effecthp = (effecthp - movet * 2)

    elif movet == "fighting" and ptype == "steel":
        effecthp = (effecthp - movet * 2)

    elif movet == "fighting" and ptype == "fairy":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "poison" and ptype == "grass":
        effecthp = (effecthp - damage * 2)

    elif movet == "poison" and ptype == "poison":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "poison" and ptype == "ground":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "poison" and ptype == "rock":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "poison" and ptype == "ghost":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "poison" and ptype == "fairy":
        effecthp = (effecthp - damage * 2)

    elif movet == "posion" and ptype == "steel":
        effecthp = (effecthp - damage * 0)

    elif movet == "ground" and ptype == "fire":
        effecthp = (effecthp - damage * 2)

    elif movet == "ground" and ptype == "grass":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ground" and ptype == "electric":
        effecthp = (effecthp - damage * 2)

    elif movet == "ground" and ptype == "poison":
        effecthp = (effecthp - damage * 2)

    elif movet == "ground" and ptype == "flying":
        effecthp = (effecthp - damage * 0)

    elif movet == "ground" and ptype == "bug":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ground" and ptype == "rock":
        effecthp = (effecthp - damage * 2)

    elif movet == "flying" and ptype == "electric":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "flying" and ptype == "grass":
        effecthp = (effecthp - damage * 2)

    elif movet == "flying" and ptype == "fighting":
        effecthp = (effecthp - damage * 2)

    elif movet == "flying" and ptype == "bug":
        effecthp = (effecthp - damage * 2)

    elif movet == "flying" and ptype == "rock":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "psychic" and ptype == "fighting":
        effecthp = (effecthp - damage * 2)

    elif movet == "psychic" and ptype == "psychic":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "psychic" and ptype == "dark":
        effecthp = (effecthp - damage * 0)

    elif movet == "psychic" and ptype == "poison":
        effecthp = (effecthp - damage * 2)

    elif movet == "psychic" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "grass":
        effecthp = (effecthp - damage * 2)

    elif movet == "bug" and ptype == "fighting":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "poison":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "flying":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "psychic":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "ghost":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "bug" and ptype == "fairy":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "rock" and ptype == "fire":
        effecthp = (effecthp - damage * 2)

    elif movet == "rock" and ptype == "ice":
        effecthp = (effecthp - damage * 2)

    elif movet == "rock" and ptype == "fighting":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "rock" and ptype == "ground":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "rock" and ptype == "flying":
        effecthp = (effecthp - damage * 2)

    elif movet == "rock" and ptype == "bug":
        effecthp = (effecthp - damage * 2)

    elif movet == "rock" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "ghost" and ptype == "normal":
        effecthp = (effecthp - damage * 0)

    elif movet == "ghost" and tyoe == "psychic":
        effecthp = (effecthp - damage * 2)

    elif movet == "ghost" and ptype == "ghost":
        effecthp = (effecthp - damage * 2)

    elif movet == "ghost" and ptype == "dark":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "dragon" and ptype == "dragon":
        effecthp = (effecthp - damage * 2)

    elif movet == "dragon" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "dragon" and ptype == "fairy":
        effecthp = (effecthp - damage * 0)

    elif movet == "dark" and ptype == "fighting":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "dark" and ptype == "psychic":
        effecthp = (effecthp - damage * 2)

    elif movet == "dark" and ptype == "ghost":
        effecthp = (effecthp - damage * 2)

    elif movet == "dark" and ptype == "dark":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "dark" and ptype == "fairy":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "steel" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "steel" and ptype == "water":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "steel" and ptype == "electric":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "steel" and ptype == "ice":
        effecthp = (effecthp - damage * 2)

    elif movet == "steel" and ptype == "rock":
        effecthp = (effecthp - damage * 2)

    elif movet == "steel" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "steel" and ptype == "fairy":
        effecthp = (effecthp - damage * 2)

    elif movet == "fairy" and ptype == "fire":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fairy" and ptype == "fighting":
        effecthp = (effecthp - damage * 2)

    elif movet == "fairy" and ptype == "poison":
        effecthp = (effecthp - damage * 0.5)

    elif movet == "fairy" and ptype == "dragon":
        effecthp = (effecthp - damage * 2)

    elif movet == "fairy" and ptype == "dark":
        effecthp = (effecthp - damage * 2)

    elif movet == "fairy" and ptype == "steel":
        effecthp = (effecthp - damage * 0.5)
        
    else:
        effecthp = (effecthp - damage)

    try:
        effecthp = int(effecthp)
    except:
        effecthp = float(effecthp)

    hpcarrier = effecthp
    #print('This is a test')
    #print(effecthp)












    
#-------------------- POKEMON CATCHING FUNCTION --------------------

def catch():
    global bush_item
    global status
    global used
    global pokeball
    global greatball
    global ultraball
    global masterball
    global perhp
    global poophp
    global bus
    global level
    global pokemonhpn
    global pokemonhp
    global hpcarrier
    
    

    if used == "pokeball":
        status = "good"
        if pokeball >= 1:
            beeping()
            
            ballrat = random.choice(pokeball_list)
            pokeball = (pokeball - 1)
        else:
            print("You do not have any Pokeballs left")
            print('')
            #break
        
    elif used == "greatball":
        status = "good"
        if greatball >= 1:
            ballrat = random.choice(greatball_list)
            beeping()
            greatball = (greatball - 1)
        else:
            print("You do not have any Greatballs left")
            print('')
            #break
        
    elif used == "ultraball":
        status = "good"
        if ultraball >= 1:
            beeping()
            ballrat = random.choice(ultraball_list)
            ultraball = (ultraball - 1)
        else:
            print("You do not have any Ultraballs left")
            print('')
            #break
        
    elif used == "masterball":
        status = "good"
        if masterball >= 1:
            ballrat = random.choice(masterball_list)
            beeping()
            masterball = (masterball - 1)
        else:
            print("You do not have any Masterballs left")
            print('')
            #break

    if bush_item in basic_list:
        tierat = random.choice(basic)

    elif bush_item in good_list:
        tierat = random.choice(good)

    elif bush_item in amazing_list:
        tierat = random.choice(amazing)

    elif bush_item in legendary_list:
        tierat = random.choice(legendary)

    if poophp < (perhp * 0.5):
        hprat = random.choice(low_list)
    else:
        hprat = random.choice(high_list)

    if status == "good":
        if ballrat == "2" and hprat == "2" and tierat == "2" or ballrat == "1" and hprat == "2" and tierat == "2": #  or ballrat == "2" and hprat == "2" and tierat == "1":
            print('Gotcha')
            print('')
            print ("Congratulations, you caught a " + bush_item)
            level = (level + 1)
            pokemonhpn = (pokemonhpn + 1)
            print('')
            bus = "yes"
            pc_list.append(bush_item)
            status = "none"
            if bush_item not in pokedex_list:
                print(bush_item + " has been registered to the Pokedex")
                print('')
            pokedex_list.append(bush_item)
            #balling = False
            #catching = False
            #battling = False
            
            #break        
        else:
            print('Oh no the ' + bush_item + ' got out')
            print('')
            #balling = False
            #catching = False
            #break
            


 
    
#-------------------------POKEMON BATTLING FUNCTION-------------------------


def pokemon (name, hp, table, attack1, num1, attack2, num2, type):
    global pokemonhp 
    global level
    global pokemonhpn
    global pokeball
    global greatball
    global ultraball
    global masterball
    global perhp
    global poophp
    global used
    global enemy
    global bus
    global current
    global hpcarrier
    global move1t
    global move2t
    global move2d
    global move1d
    global ptype
    enemy = name
    poophp = hp
    perhp = hp

    print('')
    print('You sent out ' + current)
    print('')
    print('HP: ')
    print (pokemonhp)
    print('')
    pokemonfunc = possibles.get(current.lower())
    pokemonfunc()
    
    print('')
    print('')
    battling = True
    while battling:
        s = input("What do you wanna do: Attack/Catch/Run ")
        print('')
        if s == "run":
            print("------YOU FLED------")
            print('')
            attacking = False
            battling = False
            bushing = False
            running = True

        elif s == "catch":
            catching = True
            while catching:
                print("Balls in Bag-")
                print('')
                pokeballv = str(pokeball)
                print('1. Pokeballs: ' + pokeballv)
                print('')
                greatballv = str(greatball)
                print('2. Greatballs: ' + greatballv)
                print('')
                ultraballv = str(ultraball)
                print('3. Ultraballs: ' + ultraballv)
                print('')
                masterballv = str(masterball)
                print('4. Masterball: ' + masterballv)
                print('')
                
                #------ BALLING --------
                balling = True
                while balling:
                    c = input("Which Pokeball would you like to use: ")
                    print('')

                    if c == "1" or c == "Pokeball" or c == "pokeball":
                        if pokeball >= 1:
                            pokeball = (pokeball - 1)
                            print("You used a Pokeball")
                            print('')
                            used = "pokeball"
                            catch()
                            if bus == "yes":
                                pokemonhp = pokemonhpn
                                bus = "mnopel"
                                balling = False
                                catching = False
                                battling = False
                                break
                            else:
                                balling = False
                                break
                        else:
                            print("You have no pokeballs left")
                                
                        
                    elif c == "2" or c == "Greatball" or c == "greatball":
                        print("You used a Greatball")
                        print('')
                        used = "greatball"
                        catch()
                        if bus == "yes":
                            pokemonhp = pokemonhpn
                            bus = "mnopel"
                            balling = False
                            catching = False
                            battling = False
                            break
                        else:
                            balling = False
                            break
                
                    elif c == "3" or c == "Ultraball" or c == 'ultraball':
                        print("You used a Ultraball")
                        print('')
                        used = "ultraball"
                        catch()
                        if bus == "yes":
                            pokemonhp = pokemonhpn
                            bus = "mnopel"
                            balling = False
                            catching = False
                            battling = False
                            break
                        else:
                            balling = False
                            break
                       
                    elif c == "4" or c == "Masterball" or c == "masterball":
                        print("You used a Masterball")
                        print('')
                        print ("Congratulations, you caught a " + bush_item)
                        level = (level + 1)
                        pokemonhpn = (pokemonhpn + 1)
                        print('')
                        pc_list.append(bush_item)
                        status = "none"
                        if bush_item not in pokedex_list:
                            print(bush_item + " has been registered to the Pokedex")
                            print('')
                        pokedex_list.append(bush_item)
                        pokemonhp = pokemonhpn
                        balling = False
                        catching = False
                        battling = False
                        break
                       

                    if c == "back":
                        balling = False
                        catching = False
        


        elif s == "attack":
            attacking = True
            while attacking:
                print("Moves: ")
                print('')
                print("1. "+ move1)
                print('')
                print("2. "+ move2)
                print('')
                x = input("So which move: ")
                print('')

                #ATTACKING
                if x == "1" or x == "move1":
                    print(current + " used " + move1)
                    print('')

                    effect(move1t, type, hp, move1d)
                    hp = hpcarrier

                elif x == move2 or x == "2":
                     print(current + " used " + move2)
                     print('')

                     effect(move2t, type, hp, move2d) 
                     hp = hpcarrier
                        
                else:
                    print("The attack missed")
                poophp = hp

                if hp < 1:
                    print( name + " fainted")
                    print('')
                    print("------YOU WON------")
                    level += 1
                    #print(level)
                    #leevs = "yep"
                    #leveling = True
                    #le = (le + 1)
                    pokemonhpn = (pokemonhpn + 1)
                    print('')
                    attacking = False
                    battling = False
                    bushing = False
                    pokemonhp = pokemonhpn
                    break

                else:
                    print ( name + " HP:")
                    print(hp)
                    print('')

                item = random.choice(table)
                if item == attack1:
                    pokemonhp = (pokemonhp - num1)
                    print(name + " used " + attack1)
                    print('')
                elif item == attack2:
                    pokemonhp = (pokemonhp - num2)
                    print(name + " used " + attack2)
                    print('')
                if pokemonhp < 1:
                    print(current + " fainted")
                    print('')
                    print("------YOU LOST------")
                    print('')
                    attacking = False
                    battling = False
                    bushing = False
                    running = True
                    pokemonhp = pokemonhpn
                    continue
                    #break


                 
                
                else:
                    print(current + " HP:")
                    print(pokemonhp)
                    print('')
                    break
    bushing = False  
    return ("")



def trainer():
    print("Challunge")

#------ EVOLUTION FUNCTION -----

def evolve(pokemon, npokemon):
    print (f'Look your {pokemon} is evolving...')
    print('')
    print(f'----- {pokemon} evolved into {npokemon} ------')
#---------------------------------------------------------------------------------------------------------------


#-------------------MAIN LOOP--------------------


while running:
   

   #-----------EVOLUTION------------

    if level == 16:
        if evolving == True:
            move1 = "Fire Fang"
            move1d = 10
            starter = "Charmeleon"
            print('')
            print("Look, Charmander is Evolving.....")
            time.sleep(2)
            print('')
            print('-------CHARMANDER EVOLVED INTO CHARMELEON------')
            time.sleep(2)
            print('')
            print(charmander())
            print('')
            print('Charmeleon learned Fire Fang!')
            print('')
            

            evolving = False


    elif level == 36:
        if evolving2 == True:
            move1 = "Wing Attack"
            move1d = 18
            starter = "Charizard"
            print('')
            print("Look, Chharmeleon is Evolving.....")
            time.sleep(2)
            print('')
            print('------CHARMELEON EVOLVED INTO CHARIZARD--------')
            time.sleep(2)
            print('')
            print(charmander())
            print('')
            print('Charizard learned Wing Attack!')
            print('')

            evolving2 = False
            


    #---------------Level Up Moves--------------------

    if level == 8:
        print("Charmander learned Headbutt!!")
        print('')
        move1 = "Headbutt"
        move1d = 5
        
    elif level == 12:
        print("Charmander learned Metal Claw")
        print('')
        move2 = "Metal Claw"
        move2d = 7

    elif level == 20:
        print('Charmeleon learned Slash!!')
        print('')
        move2 = "Slash"
        move2t = 'normal'

    elif level == 24:
        print('Charmeleon learned Fire Punch!!')
        print('')
        move1 = "Fire Punch"
        move1t = "fire"

    elif level == 30:
        print('Charmeleon learned Flamethrower')
        print('')
        move1 = "Flamethrower"
        move1t = "fire"

    elif level == 40:
        print('Charizard learned Air Slash!!')


        
       


              

    #---------------------------------------------------

        
    a = input("What to do: ")
    print('')


    #---SAVE---
    if a == "save" or a == "Save":
        save()


    #-------- SWAPING POKEMON --------

    if a == "swap" or a == "Swap":
        print('Pokemon in PC -')
        print('')
        print(pc_list)
        print('')
        swapping = True
        while swapping:
            swap = input("Which pokemon would you like to use: ")

            if swap == "back" or swap == "exit":
                break
            
            if swap in pc_list:
                print('')
                print('Using', swap)
                
                swapper()
                current = swap
                break
            else:
                print('Pokemon not found')
                print('')
                
        
    
    #Exit protocol
    if a == "exit":
        break
   
    if a == "pokedex" or a == "Pokedex":
        print('----- POKEDEX -----')
        print('')
        pokedexnum = str(len(pokedex_list))
        print('Pokemon Registered: ' + pokedexnum)
        print('')
        print(pokedex_list)
        print('')
        
    if a == "pc" or a == "PC" or a == "Pc":
        print('----- PC -----')
        print('')
        pokedexnum = str(len(pc_list))
        print('Pokemon caught: ' + pokedexnum)
        print('')
        print(pc_list)
        print('')
        
    #Pokemon Info
    elif a == "pokemon":
        levels = str(level)
        
        print("\nHP: " + str(pokemonhp) + "\nLevel: " + levels)
        pokemonfunc = possibles.get(current.lower())
        pokemonfunc()

        
        #pokemonhps = str(pokemonhp)
        #print("HP: " + pokemonhps)
        print('')
        continue

   #Travel Function    
    elif a == "travel":
        print("Locations")
        print('')
        print('1. Aurora Hills')
        print('')
        print('2. Springfield City')
        print('')
        print('3. Tempest Wilds')
        print('')
        print('4. Crystal Glades')
        print('')
        b = input("Where to go: ")
        print('')
        if b == "1":
            print("Travelling to Aurora Hills")
            print('')
            time.sleep(1)

            print(" ~         ~~          __   ")
            print("       _T      .,,.    ~--~ ^^")
            print(" ^^   // \                    ~")
            print("      ][O]    ^^      ,-~ ~")
            print("   /''-I_I         _II____")
            print("__/_  /   \ ______/ ''   /'\_,__")
            print("  | II--'''' \,--:--..,_/,.-{ },")
            print("; '/__\,.--';|   |[] .-.| O{ _ }")
            print(":' |  | []  -|   ''--:.;[,.'\,/")
            print("'  |[]|,.--'' '',   ''-,.    |")
            print("  ..    ..-''    ;       ''. '")
            print('')


            location = "Aurora Hills"
            continue

        elif b == "2":
            print("Travelling to Springfield City")
            print('')
            time.sleep(2)

            print("                   \  |  /         ___________")
            print("    ____________  \ \_| /         |  ___      |       _________")
            print("   |            |  \  |/          | |   |     |      | = = = = |")
            print("   | |   |   |  |   \\|            | |`v'|     |      |         |")
            print("   |            |    \|  //       |  --- ___  |      | |  || | |")
            print("   | |   |   |  |     |_//        |     |   | |      |         |")
            print("   |            |  \\ |_/_______   |     |   | |      | |  || | |")
            print("   | |   |   |  |   \\| /_____/ \  |      ---  |      |         |")
            print("   |            |    \| |+ ++|  | |  |^^^^^^| |      | |  || | |")
            print("   |            |    \| |+ ++|  | |  |^^^^^^| |      | |  || | |")
            print("^^^|    (^^^^^) |^^^^^|^| H  |_ |^|  | |||| | |^^^^^^|         |")
            print("   |    ( ||| ) |     | ^^^^^^    |  | |||| | |      | ||||||| |")
            print("   ^^^^^^^^^^^^^________/  /_____ |  | |||| | |      | ||||||| |")
            print("                                  ^^^^^^^^^^^^^      | ||||||| |")
            print("                                                     -----------")
            print("")
            location = "Springfield City"
            continue
        elif b == "3":
            print("Travelling to Tempest Wilds")
            print('')
            time.sleep(2)
            print("                         vv")
            print("                     vvv^^^^vvvvv")
            print("                 vvvvvvvvv^^vvvvvv^^vvvvv")
            print("        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv   ")
            print("    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv   ")
            print("  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv")
            print(" vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^")
            print(" vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^")
            print("  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv")
            print("   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv")
            print("     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v")
            print("        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv")
            print(" vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^")
            print("vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^vvvvvv^vvvv^^vvvvv^v")
            print(" ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____vv^^^vvvvvvvv^^^^  ")
            print("    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\ vvvvv^^^  ")
            print("         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\ ^vvvv^v  ")
            print("             ;^^vvvvvvvvvvv/____\@@@@@@\ vvvvvvv  ")
            print("             ;      \_  ^\|[  -:] ||--| | _/^^   ")
            print("             ;        \   |[   :] ||_/| |/")
            print("             ;         \\ ||___:]______/")
            print("             ;          \   ;=; /")
            print("             ;           |  ;=;|")
            print("             ;          ()  ;=;|")
            print("            (()          || ;=;|")
            print("                        / / \;=;\ ")
            print('')
            
            location = "Tempest Wilds"
            continue
        
        elif b == "4":
            print("Travelling to Crystal Glades")
            time.sleep(2)
            print("            ...        *                        *       *")
            print("      ...   *         * ..   ...                        *")
            print(" *      ...        *           *            *")
            print("          ...               ...                          *")
            print("            ..                            *")
            print("    *        ..        *                       *")
            print("           ________              *                      *")
            print("  *    *  /      ****                   *")
            print("         /        ****               *         *  X   *")
            print("   *    /        ******     *                    XXX      *")
            print("       /___________*****          *             XXXXX")
            print("        |            ***               *       XXXXXXX   X")
            print("    *   | ___        |                    *   XXXXXXXX  XXX")
            print("  *     | | |   ___  | *       *             XXXXXXXXXXXXXXX")
            print("        | |_|   | |  ****             *           X   XXXXXXX")
            print("    *********** | | *******      *                X      X")
            print("************************************************************")
            print("")            
            location = "Crystal Glades"
            continue
            
        else:
            continue

    #Bush
    elif a == "bush":
        print("Entering a bush")
        print('')
        a = "eliuyfdg"
        bushing = True

    
        
    #While bushing
        while bushing:

            #---------------Aurora Hills-------------------------------------------

            if location == "Aurora Hills":
                bush_item = random.choice(hills_list)

                #Pokemon
                
                    

                if bush_item == "Pidgey":
                    print("A Pidey appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 11')
                    print('')
                    print(pidgey())
                    print(pokemon("Pidgey", 11, pidgey_list, "Gust", 5, "Tackle", 3, 'flying' ))                                    
                    break
                
                elif bush_item == "Caterpie":
                    print("A Caterpie appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 9')
                    print('')
                    print(caterpie())
                    print(pokemon("Caterpie", 9, caterpie_list, "Tackle", 3, "Bug Bite", 4, 'bug' ))
                    break                
                
                elif bush_item == "Ekans":
                    
                    print("An Ekans appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 10')
                    print('')
                    print(ekans())
                    print(pokemon("Ekans", 10, ekans_list, "Bite", 3, "Acid", 5, 'poison'))                                
                    break

                
            #------------------------------------------------------------------------


            #----------------SPRINGFIELD CITY----------------
                
            elif location == "Springfield City":
                bush_item = random.choice(spring_list)

                #Pokemon In spring
                if bush_item == "Metapod":
                    print("A Metapod appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 30')
                    print('')
                    print(metapod())
                    print(pokemon("Metapod", 30, metapod_list, "Tackle", 1, "Tackle", 1, 'bug' ))
                    break

                elif bush_item == "Caterpie":
                    print("A Caterpie appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 9')
                    print('')
                    print(caterpie())
                    print(pokemon("Caterpie", 9, caterpie_list, "Tackle", 3, "Bug Bite", 4, 'bug' ))
                    break

                elif bush_item == "Pidgey":
                    print("A Pidgey appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 11')
                    print('')
                    print(pidgey())
                    print(pokemon("Pidgey", 11, pidgey_list, "Gust", 5, "Tackle", 3, 'flying' ))                                    
                    break

                elif bush_item == "Pidgeotto":
                    print("A Pidgeotto appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 15')
                    print('')
                    print(pidgeotto())
                    print('')
                    print(pokemon("Pidgeotto", 16, pidgeotto_list, "Quick Attack", 5, "Peck", 6, 'flying'))
                    break

                elif bush_item == "Pidgeot":
                    print("A Pidgeot appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 21')
                    print('')
                    print(pidgeot())
                    print (pokemon("Pidgeot", 21, pidgeot_list, "Sky Attack", 9, "Air Slash", 7, 'flying'))
                    break


                #------------------ TEMPEST WILDS ----------------------#


            elif location == "Tempest Wilds":
                bush_item = random.choice(wilds_list)

                    #Pokemon In Wilds

                if bush_item == "Arbok":
                    print("An Arbok appeared")
                    print('')
                    time.sleep(1)
                   
                    arbok()
                    print('HP: 14')
                    print('')
                    print('')
                    print (pokemon("Arbok", 14, arbok_list, "Poison Jab", 6, "Bite", 4, 'poison' ))
                    break

                
                if bush_item == "Gloom":
                    print("A Gloom Appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 30')
                    print('')
                    print(gloom())
                    print(pokemon("Gloom", 30, gloom_list, "Acid", 13, "Razor Leaf", 14, 'grass'))
                    break

                elif bush_item == "Oddish":
                    print("A Wild Oddish Appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 26')
                    print(gloom())
                    print(pokemon("Oddish", 22, oddish_list, "Acid", 9, "Leech Seed", 10, 'grass'))
                    break

                elif bush_item == "Scyther":
                    print("A Wild Scyther Appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 35')
                    print(scyther())
                    print(pokemon("Scyther", 35, scyther_list, "Fury Cutter", 17, "X Scissor", 18, 'bug'))
                    break

                elif bush_item == "Vileplume":
                    print("A Wild Vileplume Appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 33')
                    print('')
                    print(vileplume())
                    print(pokemon("Vileplume", 33, vileplume_list, "Petal Blizzard", 15, "Sludge Wave", 16, 'grass'))
                    break

        #--------------CRYSTAL GLADES---------------

            elif location == "Crystal Glades":
                bush_item = random.choice(crystal_list)

                if bush_item == "Shellder":
                    print("A wild Shellder appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 45')
                    print('')
                    print(shellder())
                    print (pokemon("Shellder", 45, shellder_list, "Ice Shard", 20, "Water Gun", 18, 'water'))
                    break

                elif bush_item == "Lapras":
                    print("A wild Lapras appeared")
                    print('')
                    time.sleep(1)
                    print('HP: 45')
                    print('')
                    print(lapras())
                    print (pokemon("Lapras", 52, lapras_list, "Ice Beam", 25, "Surf", 23, 'water'))
                    break
                


 
