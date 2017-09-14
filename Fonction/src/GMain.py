#================================================
def function1():
    print("Function1 : Hello World !")
#================================================
def function2(data):
    print("Function2 : " + data)
#================================================
def function3():
    m_data = "Function3 : Hello World !"
    return m_data 
#================================================
def function4(data):
    m_data = "Function4 : " + data
    return m_data 
#================================================
def function5(id, data="Hello World !"):
    m_data = "Function5 : " + data + " : " + str(id)
    return m_data 
#================================================
function1()
function2("Hello World !")
print(function3())
print(function4("Hello World !"))
print(function5(5))
#================================================
