class myRouter(object):
    'This is a class that describes the characteristic of a router'
    def __init__(self, routername, model, serial, ios):
        self.routername = routername
        self.model = model
        self.serial = serial
        self.ios = ios

    def print_router(self, manuf_date):
        print('The router name is: ', self.routername)
        print('The model is: ', self.model)
        print('The serial number of: ', self.serial)
        print('The IOS version is: ', self.ios)
        print('The model and manuf_date combine is: ' , self.model + '-' + manuf_date)


router1 = myRouter('Cisco', '2600', '12345', '12.4')
print(router1)
print(router1.model)
router1.print_router('20241010')
router2 = myRouter('R1', '2700', '98765', '13.1')
print(router2.model)

class MyNewRouter(myRouter):
    def __init__(self, routername, model, serial, ios, ports):
        myRouter.__init__(self, routername, model, serial, ios)
        self.ports = ports 

    def print_new_router(self, string):
        print(string + '-' + self.model)


new_router1 = MyNewRouter('R1', '3000', '55555', '10.1', '48')

print(new_router1.ports)
new_router1.print_new_router('Hola')