import string

admin = "admin"
user = "user"
klient = "klient"


allowed_numbers = string.digits
allowed_characters_for_username = string.digits + string.ascii_letters
allowed_characters_for_password = string.digits + string.ascii_letters + '!@#$%&*?^'

min_len_username = 3
min_len_password = 4
max_len_username = 20
max_len_password = 20


my_mail = ''
my_password = ''
