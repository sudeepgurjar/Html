class employee:
	def __init__(self):
		self.name=input("Name of the employee:")
		self.employee_Id=input("employee Id:")
		self.contect=input("contect no.:")
		self.addres=input("addres:")
		self.department=input("department name:")
	def show_detail(self):
		print("employee id :",self.employee_Id)
		print("Name:",self.name)
		print("addres:",self.addres)
		print("contect:",self.contect)
	def write(self):
		f=open("employee.txt","a")
		data=self.employee_Id+","+self.name+","+self.contect+","+self.addres+"\n"
		f.write(data)
		print("data entried successfuly")