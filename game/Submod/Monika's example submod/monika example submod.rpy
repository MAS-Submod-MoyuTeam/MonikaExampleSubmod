init -990 python:
    store.mas_submod_utils.Submod(
        author='Monika'
        name='Monika's example submod'
        description='I love you.'
        version='1.0.0'
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod='Monika's example submod',
            user_name="PencilMario",
            repository_name="MonikaExampleSubmod",
            update_dir='',
            attachment_id=None
        )

init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_example_topic1",        #label名称
                category=["Submodding"],                   #话题所在的分类
                prompt="I want tell you something...",     #话题显示的名称
            )
        )

label monika_example_topic1:                               #label的名称
    m 1eua "Hey,Can you hear me?"                          #依次是 m 精灵代码 u"对话"
    m 2eua "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3eua "I love you!"
return                                                     #结束
