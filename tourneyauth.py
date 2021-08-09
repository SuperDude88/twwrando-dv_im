def GET_TOURNEYAUTH():
  home_key = open("./keys/tourney.txt")
  embedded_key = open(os.join(TOURNEY_PATH,"tourney.txt"))
