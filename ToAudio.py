def ToAudio(mail_from, mail_subject, mail_content):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(f"Mail from {mail_from}         Subject {mail_subject}        {mail_content}")
    engine.runAndWait()

def Confirm():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say("Mail sent")
    engine.runAndWait()