import socket,threading,time
dest_IP=""


def find_other(IP,udp_socket_scanf):
    global dest_IP
    HIP = IP
    IPList = IP.split(".")
    count = 1
    while True:
        IP = IPList[0] + "." + IPList[1] + "." +IPList[2] +"." + str(count)
        if IP == HIP:
            count+=1
            continue
        udp_socket_scanf.sendto(b"E4J7P0V9J_5U32",(IP,7777))
        time.sleep(0.04)
        if dest_IP != "":
            break
        count+=1
        if count==255:
            count=0
    udp_socket_scanf.sendto(b"E4J7P0V9J_5U32",(dest_IP,7777))




def send_msg(udp_socket,IP,udp_socket_scanf):
    find_other(IP,udp_socket_scanf)
    print("IP:"+dest_IP+"connect!")
    while True:
        msg = input()
        udp_socket.sendto(msg.encode("utf-8"),(dest_IP,7777))



def recv_msg(udp_socket):
    global dest_IP
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if (recv_data[0]).decode("utf-8") == "E4J7P0V9J_5U32":
            dest_IP = recv_data[1][0]
        else:
            print((recv_data[0]).decode("utf-8"))
        

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket_scanf = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7777))
    udp_socket_scanf.bind(("",8888))
    IP = input("IP > ")
    print("Search Other APP")
    Send = threading.Thread(target=send_msg,args=(udp_socket,IP,udp_socket_scanf))
    Recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    Recv.start()
    Send.start()
    

if __name__ == '__main__':
    main()