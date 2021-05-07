import bcrypt
import base64

password = # https://www.youtube.com/watch?v=-tJYN-eG1zk&ab_channel=QueenOfficial
bpass = password.encode('ascii')
passed= str(base64.b64encode(bpass))
hashAndSalt = bcrypt.hashpw(passed.encode(), bcrypt.gensalt())
print(hashAndSalt)

salt = b'$2b$12$SVInH5XmuS3C7eQkmqa6UOM6sDIuumJPrvuiTr.Lbz3GCcUqdf.z6'
# I wrote this code last year and i didnt save password verify line... I need to find my password