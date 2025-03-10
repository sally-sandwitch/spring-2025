import assignments.pair.p2.graphics as g
def main():
  m = 10
  l = -1
  y=1
  lines=[]
  with open('p1/maze10x10.txt') as f:
    while True:
         line = f.readline()
         if line == "":
            break
         l += 1
    print(l)
    text_file = open('p1/maze10x10.txt', "r")
    lines = text_file.readlines()
    print (lines)
    text_file.close()
 

  print("### DBG")
  for l in lines:
    print(l)


  height =len(lines)
  width = len(lines[0])
  print('maze', width, height)


  # This part is theoretical. I couldn't test because I cannot import graphics 
  win=g.GraphWin('maze', width * m, height * m)
  for hi in range(height):
    for wi in range(width):
      rect = g.Rectangle((wi * m, hi * 10),((wi + 1) * m, (hi + 1) * 10))
      rect.setFill('#FF5733')
      rect.draw(win)


  win.getMouse()
  win.close()

if __name__=="__main__":
    main()
