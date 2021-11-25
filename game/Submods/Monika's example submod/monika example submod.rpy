init -990 python:
    store.mas_submod_utils.Submod(
        author="Monika",
        name="Monika's example submod",
        description="I love you.",
        version='1.0.1'
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Monika's example submod",
            user_name="PencilMario",
            repository_name="MonikaExampleSubmod",
            update_dir="",
            attachment_id=None
        )

init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_example_topic1",       
                category=["Submodding"],                   
                prompt="I want tell you something...",     
            )
        )

label monika_example_topic1:                               
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 4ekb "Hey,Can you hear me?"
    m 1eka "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3hubsb "I love you!"
    $_history_list.pop()
    menu:
        "I love you!{fast}"
        "I love you too!":
            if mas_isMoniEnamored(higher=True):
                m 1eua "I~~~~~~~~ Love~~~~~~~ You~~~~~~~!"
            elif mas_isMoniNormal(higher=true):
                m 1eua "Full of expectation~"
            else:
                m 1eua "..."
        "...":
            m 1eua "..."
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
return                                                     
