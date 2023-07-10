from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x600+0+0")
        self.root.title("My Inventory | Developed By Pankaj and Gaurav")
        self.root.config(bg="white")
        

        #-----title----#
        self.icon_title=PhotoImage(file="icon.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#312318",anchor="w",padx=20,fg="white").place(x=0,y=0,relwidth=1,height=70)


        #-----btn_logout----#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#B55912",padx=20,cursor="hand2").place(x=1100,y=20,height=40,width=150)

        #-----clock----#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#010c48",fg="white").place(x=0,y=70,relwidth=1,height=30)
        #self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #------Left Menu-----#
        self.MenuLogo=Image.open("logo1.png")
        self.MenuLogo=self.MenuLogo.resize((80,80),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=100,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#B55912").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2").pack(side=TOP,fill=X)

        #---content---#
        self.lbl_employee=Label(self.root,text="Total Emloyee\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=620,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=940,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=620,y=300,height=150,width=300)
        

        #-----footer----#
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By GP Team\nFor any technical issue contact us",font=("times new roman",15),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
#==================================================================================================================

    def employee(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=employeeClass(self.new_win)

    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win)

    def category(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=categoryClass(self.new_win)

    def product(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productClass(self.new_win)

    def sales(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=salesclass(self.new_win)


if __name__=="__main__":
  root=Tk()
  obj=IMS(root)   
  root.mainloop()    