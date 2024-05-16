import os
import re

class AmunLogParser:
    
    def __init__(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.filename = filename
                    content = f.read()
                    self.content_list = content.strip().split('\n')
            except IOError:
                self.content_list = None
        else:
            self.content_list = None
				
    # only develop this one, leave others alone
    # def amun_request_handler_log_parser(self):




