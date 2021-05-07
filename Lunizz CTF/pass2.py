import bcrypt
import base64

hashpassword = b'$2b$12$SVInH5XmuS3C7eQkmqa6UOM6sDIuumJPrvuiTr.Lbz3GCcUqdf.z6'

salt= b'$2b$12$SVInH5XmuS3C7eQkmqa6UO'
file = open("rockyou.txt","r")
for p in file:
	#print(p)
	password = p.strip()
	try:
		bpass = password.encode('ascii')
		passed= str(base64.b64encode(bpass))
		hashAndSalt = bcrypt.hashpw(passed.encode(), salt)
		#print(p, hashAndSalt)
		if hashAndSalt == hashpassword:
			print("GOTIT........>>",p, hashAndSalt)
			break
	except:continue