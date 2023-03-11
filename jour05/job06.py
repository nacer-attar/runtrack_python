def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40 and note % 5 >= 2.5:
            note_arrondie = 5 * round(note/5)
            notes_arrondies.append(note_arrondie)
        else:
            notes_arrondies.append(note)
    return notes_arrondies
