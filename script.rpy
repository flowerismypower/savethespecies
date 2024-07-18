define transition =(Dissolve(4.0, alpha=False, time_warp=None, mipmap=None))
define newtrans =(Dissolve(1.0, alpha=False, time_warp=None, mipmap=None))
define s = Character('Shark', color="#2862c5")
define t = Character('Thomas', color="#fa9727")
label start:
    scene starting black  
    with Dissolve(0.1) 
    show door opening
    with Dissolve(5.0)
    scene bar starting 
    with transition
    scene bar second
    with transition
    scene bar third meeting
    with transition

    s "hey how are you today"
    t "SHARKEY! I haven't seen you in ages"
    t "How are you?"
    s "Things are ok"
    t "You seem so tired"
    "..."
    s "Yeah I've been going through some things"

    scene bar fourth
    with newtrans

    t "Oh Dude! Like What???"

    scene recollection sixth
    with newtrans

    s "Humans are honestly horrible creatures"
    s "They have been destroying my house and throwing rubbish onto my property"
    
    scene shark scared
    with newtrans

    s "Now I'm scared to even walk alone at night"
    t "Why?"
    s "I'm too worried that i will be attacked for my fins, or get caught in nets"

    scene sharks are bad
    with newtrans

    s "On top of all of that, humans think taht i am the bad guy."
    s "They are calling me a danger and they won't let me live in peace any more"

    menu: 
        "I couldn't bear to hear such bad news, so i decided that i would"

        "Help Sharkey.":

            jump help

        "Do nothing":

            jump nothing

label help:
    scene starting black
    with newtrans

    t "I knew that this wasn't right, so I started making some changes"

    scene help fix it
    with newtrans

    t "I decide to start cleaning up his habitat, made him safe spaces and started speaking up on his behalf"
    t "And the best part is, others started joining me too!"

    scene the end
    with newtrans

    t "And evrything worked out well"
    "{b}Good Ending{/b}."
    return

label nothing:

    scene starting black
    with transition

    s "I wish people would start helping me out"
    "Sharkey's home was still being destroyed and he was still in danger of poachers"

    t "This is unacceptable"
    "{b}Bad Ending{/b}."
    return

        
        




