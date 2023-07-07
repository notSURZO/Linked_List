class Patient:
  def __init__(self,id,name,age,bg,n,p):
    self.name = name
    self.age = age
    self.id = id
    self.bg = bg
    self.next =n
    self.prev=p
class WRM:
  def __init__(self):
    self.dh = Patient(None,None,None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh
    self.tail = self.dh
  def RegisterPatient(self,id, name, age,bg):

    n= Patient(id,name,age,bg,self.dh,self.tail)
    self.tail.next = n
    self.tail = self.tail.next
    self.dh.prev = self.tail
    print('Success registering patient')

  def ServePatient(self):
    tbr = self.dh.next
    prevNode = tbr.prev
    nextNode = tbr.next
    prevNode.next = nextNode
    nextNode.prev = prevNode
    tbr.next = None
    tbr.prev = None
    print(tbr.name,'is Served')
  def ShowAllPatient(self):
    temp = self.dh.next
    if temp!= self.dh:     
      while temp != self.dh:
        print(temp.name,end=' ')
        temp = temp.next
    else:
      print('No patient to be served')

  def CancelAll(self):
    self.dh.next = self.dh
    self.dh.prev = self.dh
    print('All appointments cancelled')
  def CanDoctorGoHome(self):
    if self.dh.next.name == self.dh.name:
      print('yes')
    else:
      print('No')
x = WRM()
while True:
  print(f'''\n **Welcome to Waiting Room Management System**
  ==Choose an Option==       
  1. RegisterPatient()
  2.ServePatient
  3.CancelAll()
  4.CanDoctorGoHome()
  5.ShowAllPatient()
  6.exit
  ====================''')

  i = input('Enter your choice: ')

  if i == '1':
    print('Executing RegisterPatient()...')
    iid = input('Enter ID: ')
    n = input('Enter Name: ')
   
    iage = input('Enter Age: ')
    ibg = input('Enter Blood group: ')
    x.RegisterPatient(iid,n,iage,ibg)
  elif i == '2':
    print('Executing ServePatient()...')
    print()
    x.ServePatient()
  elif i == '3':
    print('Executing CancelAll()...')
    print()
    x.CancelAll()

  elif i == '4':
    print('Executing CanDoctorGoHome()...')
    print()
    x.CanDoctorGoHome()
  elif i == '5':
    print('Executing ShowAllPatient()...')
    print()
    x.ShowAllPatient()
  elif i == '6':
    print('''Thank You For Using Waiting Room Management System
EXITING...''')
    break
  else:
    print('No Such Option')
