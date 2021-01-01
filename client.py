from class_code import DataStore
import sys
import os

def main():
	f = './my_json.json'
	try:
		os.rename(f,f)
	except:
		print("[-] File already in use")
		sys.exit(0)

	clientObj = DataStore()
	var = """
	Select Function:
	1. Create Key-Value Pair
	2. Read Key-Value Pair
	3. Delete Key-Value Pair
	4. Exit
	"""
	while(True):
		print(var)
		try:
			sw = input("Enter Client Function:")
			if int(sw) == 1:
				key, value = input("Enter Key-Value Pair (seperated by spaces):").split(" ")
				clientObj.create(key, int(value))
			elif int(sw) == 2:
				key = input("Enter key value to read: ")
				clientObj.read(key)
			elif int(sw) == 3:
				key = input("Enter key value to delete: ")
				clientObj.delete(key)
			elif int(sw) == 4:
				print("[-] Exiting...")
				sys.exit(0)	
			else:
				print("[!] Invalid Input")
		except KeyboardInterrupt:
			print("[-] Exiting...")
			sys.exit(0)

if __name__ == "__main__":
	main()