import assignments.pair.p1.graphics as g
         
def main():
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

   for y in range (len(lines)):
      if lines[y]=='\n':
         lines.append([])
      y+=1

   width=400
   height=400
   win=g.GraphWin('maze', width, height)

   i=(l/2)
   x=50
   y=50
   dx=300/(l/2)
   radius=3

   while (i<=l):
      while(x<=(width-50)):
         c=g.Circle(g.Point(x,y), radius)
         c.setFill("#FF5733")
         c.draw(win)
         x+=dx
      y+=dx
      x=50
      print(i)
      i+=1
   win.getMouse()
   
   i=l/2
   vc=0
   while (vc<l):
      print('meep')
      hc=0
      while (hc<l):
         print('hc')
         # issue with if statement
         if lines[hc]=='#' and lines[hc+1]=='#':
            x1=(300/i)*hc
            x2=(300/i)*vc
            print('draw?')
            y=300/i
            l = g.Line(g.Point(x1,y), g.Point(x2,y))
            l.setWidth(3)
            c.setFill("#FF5733")
            l.draw(win)
         hc+=2
      vc+=2


   win.getMouse()
   win.close()

if __name__=="__main__":
    main()