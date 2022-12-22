import time

class Packet(object):
    data = None
    creation_time = time.monotonic()
    sent = False
    data_type = None

    def __init__(self, x):
        self.data = x
        self.update_type()


    def update_sent(self):
        self.sent = True

    def update_type(self):
        self.data_type = type(self.data)

    def convert(self):
        # convert bytearray to string
        if self.data is not None:
            data_string = ''.join([chr(b) for b in self.data])
            data_dict = {}

            #turn back into dictionary
            data_string = data_string.strip("'{}'") # get rid of stuff on outside
            for subString in data_string.split(","):
                subString = subString.replace("'", "").strip().split(":") #get rid of stuff on outside

                if subString[0] == 'time':
                    data_dict[subString[0]] = subString[1].strip() + subString[2].strip() + subString[3].strip()
                else:
                    data_dict[subString[0]] = float(subString[1])

            self.data = data_dict
            self.update_type()
            return data_dict
        else:
            return
