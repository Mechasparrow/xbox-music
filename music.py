from inputs import get_gamepad
from sound import Soundgenerator
from note import Note

exit = False
notes = Note()

while (not exit):
    events = get_gamepad()

    for event in events:
        print (event.code)
        if (event.state == 1):
            if (event.code == "BTN_SELECT"):
                exit = True
            elif (event.code == "BTN_SOUTH"):
                print ("sound button")
                snd = Soundgenerator(notes.note("A"))
                snd.playsound()
            elif (event.code == "BTN_EAST"):
                snd = Soundgenerator(notes.note("C"))
                snd.playsound()
            elif (event.code == "BTN_NORTH"):
                snd = Soundgenerator(notes.note("D"))
                snd.playsound()
            elif (event.code == "BTN_WEST"):
                snd = Soundgenerator(notes.note("F"))
                snd.playsound()
            elif (event.code == "BTN_TR"):
                snd = Soundgenerator(notes.note("G"))
                snd.playsound()
