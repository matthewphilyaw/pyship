class SystemUnit:
    def __init__(self, unit_type):
        if unit_type == None:
            raise Exception("Must declare the unit type")

        self.unit_type = unit_type
        self.value = 0

    def applied(self, success, message):
        return True #print 'unit type: ' + str(self.unit_type) + '\nunit status: ' + str(success) + '\nmessage: ' + str(message)