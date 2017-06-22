from appJar import gui

app = gui("Mad Lib Generator", "600x600")
app.setBg("lightblue")
app.setFont(18)

app.addEntry("Country")
app.addEntry("Song")
app.addEntry("Type of Dog")
app.addEntry("Thing")
app.addEntry("Color")

app.setEntryDefault("Country", "Country")
app.setEntryDefault("Song", "Song")
app.setEntryDefault("Type of Dog", "Type of Dog")
app.setEntryDefault("Thing", "Thing")
app.setEntryDefault("Color", "Color")

string_one = "Once upon a time in "
string_two = "Heather was listening to her favorite song "
string_three = "Suddenly, a viscous "
string_four = "He told her tales of magic milk bones and the dangers of beggin strip wands and how they might effect the "
string_five = " Despite the melodrama of his claim this did not stop Heather from enjoying the beautiful "

def press(GenerateMadlib):
    app.setTextArea("MadLibEntry", string_five + app.getEntry("Color") + " sunset.")
    app.setTextArea("MadLibEntry", string_four + app.getEntry("Thing") + ".")
    app.setTextArea("MadLibEntry", string_three + app.getEntry("Type of Dog") + " appeared out of nowhere to share with her his darkest secrets. ")
    app.setTextArea("MadLibEntry", string_two + app.getEntry("Song") + "." + " ")
    app.setTextArea("MadLibEntry", string_one + app.getEntry("Country") + " ")


app.addButton("Generate MadLib", press)

app.addTextArea("MadLibEntry")

app.go()