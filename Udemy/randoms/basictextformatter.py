def capitalized(phrase):
    return phrase.capitalize()

def phrase_check(phrase):
    interogatives = ('how', 'when', 'where', 'why', 'what')
    if phrase.startswith(interogatives):
        return phrase + '?'
    else:
        return phrase + '.'

stuff = []

while True:
    ui = input('say something: ')
    if ui == "/end":
        break
    else:
        stuff.append(capitalized(phrase_check(ui)))

print(' '.join(stuff))