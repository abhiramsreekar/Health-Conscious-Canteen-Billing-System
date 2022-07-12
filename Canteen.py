import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image  
win=tk.Tk()  
win.title("Canteen")
win.geometry("900x900")
win.configure(bg='white')
canvas=Canvas(win,width=900,height=900)
canvas.configure(bg='white')
img1=ImageTk.PhotoImage(Image.open('C:/Users/sasid/Downloads/canteen.jpg'))  
canvas.create_image(310, 20, anchor=NW, image=img1)
img2=ImageTk.PhotoImage(Image.open('C:/Users/sasid/Downloads/chef.jpg'))  
canvas.create_image(20,200, anchor=NW, image=img2)
menu=canvas.create_text(150,500, text="",fill="black", font=('Helvetica 10 bold'))
solution=canvas.create_text(500,700,text="",fill="black",font=('Comicsans 10'))
profit=canvas.create_text(450,800,text="",fill="black",font=('Comicsans 15 bold'))
def nextPermutation(nums: list) -> None:
        if sorted(nums,reverse=True)==nums:
            return None
        n=len(nums)
        brk_point=-1
        for pos in range(n-1,0,-1):
            if nums[pos]>nums[pos-1]:
                brk_point=pos
                break
        else:
            nums.sort()
            return
        replace_with=-1
        for j in range(brk_point,n):
            if nums[j]>nums[brk_point-1]:
                replace_with=j
            else:
                break
        nums[replace_with],nums[brk_point-1]=nums[brk_point-1],nums[replace_with]
        nums[brk_point:]=sorted(nums[brk_point:])
        return nums
def knapSack(W, wt, val, names,n,check):
    umap=dict()
    res1=[]
    set_sol=set()
    for i in range(n) :
        umap[wt[i]]=val[i]
     
 
    result = -2147483648
    remaining_weight=0
    sum = 0
    while True:
        sum = 0
        remaining_weight = W
        possible=[]
        for i in range(n) :
            if (wt[i] <= remaining_weight) :
 
                remaining_weight -= wt[i]
                sum += (umap[wt[i]])
                possible.append((wt[i],
                     umap[wt[i]])
                )
             
         
        possible.sort()
        if (sum > result) :
            result = sum
        st=""
        res=""
        l=[]
        if (tuple(possible) not in set_sol):
            for sol in possible:
                if check==1:
                        if sol[0]==25:st='Vada'
                        if sol[0]==20:st='Idli'
                        if sol[0]==35:st='Masala Dosa'
                        if sol[0]==30:st='Mysore Bajji'
                        
                elif check==2:
                        if sol[0]==35:st='Veg.Fried Rice'
                        if sol[0]==34:st='Veg.Noodles'
                        if sol[0]==25:st='Parota'
                        if sol[0]==26:st='Puri'

                elif check==3:
                        if sol[0]==20:st='Samosa'
                        if sol[0]==30:st='Gulab Jamun'
                        if sol[0]==25:st='Egg Pakoda'
                        if sol[0]==40:st='Frankie'
                res=st+": "+str(sol[1])+", "
                l.append(res)
            res1.append(" ".join(l))
            
                
            print()
            set_sol.add(tuple(possible))
         
        canvas.itemconfig(solution,text="\n".join(res1))
        if not nextPermutation(wt):
            break
    canvas.itemconfig(profit,text="Maximum Profit="+str(result))
    return result
def breakfast():
    canvas.itemconfig(menu,text="---MENU FOR TODAY---"+"\n"+
              "1. Vada          25/-"+"\n"+
              "2. Idli          20/-"+"\n"+
              "3. Masala Dosa   35/-"+"\n"+
              "4. Mysore Bajji  30/-"+"\n"+
              "----------------------")
    canvas.update
    item_names=['Vada','Idli','Masala Dosa','Mysore Bajji']
    item_health_factors=[20,40,15,10]
    item_cost=[25,20,35,30]
    canvas.create_text(750,310, text="Enter your budget",fill="black", font=('Helvetica 10 bold'))
    entry1 = tk.Entry(win)
    canvas.create_window(750,360, window=entry1)
    def Enter():
        n=int(entry1.get())
        m=knapSack(n,item_cost,item_health_factors,item_names,4,1)
    btn4=Button(win,text='Enter',width=15,height=2,font="Times 12",command=Enter)
    btn4.place(x=645,y=400)
def lunch():
    canvas.itemconfig(menu,text="---MENU FOR TODAY---"+"\n"+
             "1. Veg.Fried Rice    35/-"+"\n"+
             "2. Veg.Noodles       34/-"+"\n"+
             "3. Parota            25/-"+"\n"+
             "4. Puri              26/-"+"\n"+
             "----------------------")
    canvas.update
    item_names=['Veg.Fried Rice','Veg.Noodles','Parota','Puri']
    item_health_factors=[35,40,30,20]
    item_cost=[35,34,25,26]

    canvas.create_text(750,310, text="Enter your budget",fill="black", font=('Helvetica 10 bold'))
    entry1 = tk.Entry(win)
    canvas.create_window(750,360, window=entry1)
    def Enter():
        n=int(entry1.get())
        m=knapSack(n,item_cost,item_health_factors,item_names,4,2)
    btn4=Button(win,text='Enter',width=15,height=2,font="Times 12",command=Enter)
    btn4.place(x=645,y=400)
def snacks():
    canvas.itemconfig(menu,text="---MENU FOR TODAY---"+"\n"+
             "1. Samosa           20/-"+"\n"+
             "2. Gulab Jamun      30/-"+"\n"+
             "3. Egg Pakoda       25/-"+"\n"+
             "4. Frankie          40/-"+"\n"+
             "----------------------")
    canvas.update
    item_names=['Samosa','Gulab Jamun','Egg Pakoda','Frankie']
    item_health_factors=[25,35,20,30]
    item_cost=[20,30,25,40]
    canvas.create_text(750,310, text="Enter your budget",fill="black", font=('Helvetica 10 bold'))
    entry1 = tk.Entry(win)
    canvas.create_window(750,360, window=entry1)
    def Enter():
        n=int(entry1.get())
        m=knapSack(n,item_cost,item_health_factors,item_names,4,3)
    btn4=Button(win,text='Enter',width=15,height=2,font="Times 12",command=Enter)
    btn4.place(x=645,y=400)
canvas.pack()
btn1=Button(win,text='Breakfast',width=15,height=2,font="Times 12",command=breakfast)
btn1.place(x=370,y=300)
btn2=Button(win,text='Lunch',width=15,height=2,font="Times 12",command=lunch)
btn2.place(x=370,y=400)
btn3=Button(win,text='Snacks',width=15,height=2,font="Times 12",command=snacks)
btn3.place(x=370,y=500)
win.mainloop() 
