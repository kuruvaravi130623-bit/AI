print("hello i am python")
print("today we will build a cleaning robot together")
print(2+3,"is the answerto 2+3")
# this is our room: 5 sports. D=dirty,c=clean
room=["D","C","D","D","C"]

# A helper that draws the room with nice symbols
def show_room(room):
  picture=""
  for spot in room:
    if spot=="D":
        picture +="" #dirty spot
    else:
        picture +="" #clean spot
  print(picture)

print("our room right now")
show_room(room)

# the robot looks at one spot and decides what to do.
def clean_spot(spot):
    if spot=="D": # the room is dirty
      # your turn: make it clean. type "c" on the next line,next line replacing the word here
      return "C"

    else: #the room is cleaned already
      return "c"
result=clean_spot("D")
print(" The robot looked at a dirty spot and made it: ",result," (C means clean)")
print("BEFORE - the dirty room:")
def show_room(room):
  print(room)

for i in range(len(room)):
  room[i]=clean_spot(room[i])
  print("after cleaning spot number",i+1,":")
  show_room(room)

  print()
  print("after - all done!")
  show_room(room)
