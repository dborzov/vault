uname -m # see architecture, like x86_64
#  x64, x86_64 and AMD64 are the same thing
uname # OS name :)

#user management
passwd
adduser joe

cd /usr/local # for use when installing software locally. 

nano /etc/profile # system-wide shell profile file

# upload files with ssh
scp file.txt worker@host:/home/worker/folder

#download files with ssh
scp worker@host:/home/worker/folder file.txt

#run stuff in background shell
screen rtorrent
# ^A+D to detach
screen -r # to list detached ones
screen -r name # to attach


#set up ssh public key
scp .ssh/id_rsa.pub username@hostname.com:~
cat id_rsa.pub >> .ssh/authorized_keys
