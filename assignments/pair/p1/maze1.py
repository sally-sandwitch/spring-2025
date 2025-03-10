import assignments.pair.p2.graphics as g

def read_specific_line(file_path,line_number):
      with open(file_path,'r')as file:
         for i, line in enumerate(file):
            if i + 1 == line_number:

               return line#.rstrip('n')
            
            
         
def main():
   l = -1
   with open('p1/maze.txt') as f:
      while True:
         line = f.readline()
         if line == "":
            break
         l += 1
   print(l)

   width=400
   height=400
   win=g.GraphWin('maze', width, height)

   i=(l/2)
   x=50
   y=50
   dx=300/(l/2)
   radius=3
   #c=g.Circle(g.Point(x,y), radius)
   #c.setFill("#FF5733")
   #c.draw(win)

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
   str_store=[]
   while (vc<i):
 
      hc=0
      while (hc<i):
         if str_store[hc]=='#' and str_store[hc+1]=='#':
            x1=(300/i)*hc
            x2=(300/i)*vc
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