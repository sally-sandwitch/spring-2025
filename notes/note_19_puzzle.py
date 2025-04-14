def move(n:int, src:str, dst:str, helper:str):
    if n==1:
        print('move disk from peg{} to peg{}'.format(src,dst))
    else:
        move(n-1,src,helper,dst)
        move(1,src,dst,helper)
        move(n-1,helper,dst,src)

def hanoi(n:int):
    move(n,'A','C','B')

def main():
    hanoi(64)

if __name__=="__main__":
    main()