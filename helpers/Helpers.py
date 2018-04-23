import re


class Helpers():

    def checkCorrectionMail(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False