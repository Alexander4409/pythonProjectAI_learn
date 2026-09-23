password = input("Enter user password")
password_bytes = password.encode("utf-8")

size_in_bytes = len(password_bytes)
size_in_bits = size_in_bytes * 8
size_in_kilobytes  = size_in_bytes / 1024

print(f"results :\n"
      f"User passcode - {password}\n"
      f"symbol count - {len(password)} \n"
      f"kilobytes - {size_in_kilobytes}")