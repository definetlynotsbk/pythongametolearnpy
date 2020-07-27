def phrase_check(oof):
    questions = ("What", "When", "Why", "Where", "How")
    if oof.startswith(questions):
        return "".join([oof, "?"])
    else:
        return oof

ui = ""
mylist = []
while 1 == 1:
    ui = (input("say something:"))
    if ui == "\end":
        break
    else:
        mylist.append(phrase_check(ui.capitalize()))

print (", ".join(mylist))