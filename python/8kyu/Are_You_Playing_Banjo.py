def are_you_playing_banjo(name):
    cond = "plays" if name.lower().startswith("r") else "does not play"
    return "%s %s banjo" % (name, cond)
