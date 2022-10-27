# get inputs 
#ip address
file = open("VLSM\\vlsm_input_ipaddress.rapa","r")
ip_address = file.readline()
file.close()

#subnets
file = open("VLSM\\vlsm_input_subnets.rapa","r")
subnets = file.readline()
file.close()

#hosts
hosts_list = []
file = open("VLSM\\vlsm_input_hosts.rapa","r")
for i in range(int(subnets)):
    hosts_list.append(int(file.readline()))
file.close()

###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
def seperated_number(val):
    val = str(val)
    val_t = ""
    #reverse number
    for i in range(len(val)-1,-1,-1):
        val_t += val[i]
    
    print(val_t)
    index = 0
    need = 3

    #add , 
    val_t1 = ""
    for i in val_t:
        if need ==  index :
            val_t1 += "," 
            need += 3 
        val_t1 += i 
        index += 1
    print(val_t1)
    l_val = ""

    #reberse back
    for i in range(len(val_t1)-1,-1,-1):
        l_val += val_t1[i]
    
    return l_val
###################################################
###################################################

def round_two_s_power(num):
    power = 0
    num+=2
    while 1 :
        if num <= 2**power :
            break
        power += 1
    value = 2**power
    return value

ip_addresses_list = []

#write ip addresses
#write hosts
f = open("VLSM\\ip_addresses.rapa","w")
f1 = open("VLSM\\ip_hosts.rapa","w")
for host in hosts_list :
    ip_addresses = round_two_s_power(host)
    ip_addresses_list.append(ip_addresses)
    f.write(seperated_number(str(ip_addresses))+"\n")
    f1.write(seperated_number(str(ip_addresses-2))+"\n")
f.close()
f1.close()
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################

ip1,ip2,ip3,ip4 = ip_address.split(".")

if int(ip1) > 191:
    ip_address_class = "class c"
    default_ip_address = ip1 + "." + ip2 + "." +ip3 
elif int(ip1) > 127:
    ip_address_class = "class b"
    default_ip_address = ip1 + "." + ip2 + "."    
else:
    ip_address_class = "class a"
    default_ip_address = ip1 + "."

###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################

#binary_to_decimal
def binary_to_decimal(bin_num,vtype) :
    index = len(bin_num)-1
    dec_num = 0
    power = 0
    while index != -1 :
        dec_num += int(bin_num[index]) * (2**power)
        power += 1
        index -= 1  
    return vtype(dec_num)
   
###################################################
###################################################
#subnet_mask maker
def subnet_mask_by_host(hosts,ip_c):
    host_bits = 0
    while 1:
        if hosts == 2**host_bits :
            break
        host_bits += 1

    ###################################################
    if ip_c == "class c" :
        net_bits = 8 - host_bits
        default_subnet_mask = "255.255.255"
        sub4_binary =  "1"*net_bits + "0"*host_bits
        sub4 = binary_to_decimal(sub4_binary,str)
        subnet_mask = default_subnet_mask + "." + sub4
    
    ###################################################
    elif ip_c == "class b" :
        default_subnet_mask = "255.255"
        if host_bits <= 8 :
            net_bits = 8-host_bits
            sub3 = "255"
            sub4_binary = "1"*net_bits + "0"*host_bits
            sub4 =  binary_to_decimal(sub4_binary,str)
        else:
            net_bits = 16 - host_bits
            host_bits = host_bits - 8
            sub3_binary = "1"*net_bits + "0"*(host_bits)
            sub3 = binary_to_decimal(sub3_binary,str)
            sub4 = "0"
        subnet_mask = default_subnet_mask + "." + sub3 + "." + sub4  
    
    ###################################################
    else :
        default_subnet_mask = "255"
        if host_bits <= 8 :
            net_bits = 8-host_bits
            sub2 = "255"
            sub3 = "255"
            sub4_binary = "1"*net_bits + "0"*host_bits
            sub4 = binary_to_decimal(sub4_binary,str)
        elif host_bits <= 16 :
            net_bits = 16-host_bits
            host_bits = host_bits-8
            sub2 = "255"
            sub3_binary = "1"*net_bits + "0"*host_bits 
            sub3 = binary_to_decimal(sub3_binary,str)
            sub4 = "0"
        else:
            net_bits = 24-host_bits
            host_bits = host_bits - 16
            sub2_binary = "1"*net_bits + "0"*host_bits
            sub2 = binary_to_decimal(sub2_binary,str)
            sub3 = "0"
            sub4 = "0"
        subnet_mask = default_subnet_mask + "." + sub2 + "." + sub3 + "." + sub4
    return subnet_mask

#write subnet masks
f = open("VLSM\\subnet_mask.rapa","w")
subnet_mask_list = []
for hosts in ip_addresses_list :
    vlsm_subnet_mask = subnet_mask_by_host(hosts,ip_address_class) 
    subnet_mask_list.append(vlsm_subnet_mask)
    f.write(vlsm_subnet_mask+ "\n")
f.close()
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################

def decimal_to_binary(dec_num):
    dec_num = int(dec_num)
    bin_num = bin(dec_num)[2:]
    bin_num = "0"*(8-len(bin_num)) + bin_num
    return bin_num

def block_size_get_by_subnet_mask(subnet_mask):
    sub1,sub2,sub3,sub4 = subnet_mask.split(".")
    
    sub_lists = [sub2,sub3,sub4]
    block_size_bits = 0
    block_get = 1

    for sub_decimal in sub_lists:
        block_get += 1 
        sub_decimal_binary = decimal_to_binary(sub_decimal)
        for sub_binary in sub_decimal_binary:
            if sub_binary == "0" :
                block_size_bits += 1 
        if block_size_bits != 0 :
            break

    block_size_get = str(2**block_size_bits) + ">" + str(block_get)
    return block_size_get
    

#calculate block size and block get
block_size_get_list = []
for subnet_mask in subnet_mask_list:
    block_size = block_size_get_by_subnet_mask(subnet_mask)
    block_size_get_list.append(block_size)

###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################


ipd1,ipd2,ipd3,ipd4 = ip_address.split(".")

if ip_address_class == "class a" :
    ipd1 = int(ipd1)
    ipd2 = 0
    ipd3 = 0
    ipd4 = 0
elif ip_address_class == "class b" :
    ipd1 = int(ipd1)
    ipd2 = int(ipd2)
    ipd3 = 0
    ipd4 = 0
else:
    ipd1 = int(ipd1)
    ipd2 = int(ipd2)
    ipd3 = int(ipd3)
    ipd4 = 0


#openning files 
file_001 = open("VLSM\\ip_start_range.rapa","w")
file_001_end = open("VLSM\\ip_end_range.rapa","w")
file_002 = open("VLSM\\ip_start_usable_range.rapa","w")
file_002_end = open("VLSM\\ip_end_usable_range.rapa","w")

#write first start (usable)ip 
first_start_ip_range =  "{0}.{1}.{2}.{3}".format(ipd1,ipd2,ipd3,ipd4)
first_start_ip_usable_range =  "{0}.{1}.{2}.{3}".format(ipd1,ipd2,ipd3,ipd4+1)
file_001.write(first_start_ip_range+"\n")
file_002.write(first_start_ip_usable_range+"\n")


def ip_address_start_range(block_size,block_get):
    global ipd1
    global ipd2
    global ipd3
    global ipd4
    ###################################################
    ###################################################
    if block_get == 2:
        if ipd2 + block_size >= 256 :
            ipd1 += 1
            ipd2 = (block_size+ipd2)-256
        else:
            ipd2 +=  block_size

    if block_get == 3:
        if ipd3 + block_size >= 256 :
            ipd2 += 1
            ipd3 = (block_size+ipd3)-256
        else:
            ipd3 += block_size

    if block_get == 4:
        if ipd4 + block_size >= 256 :
            ipd3 += 1
            ipd4 = (block_size+ipd4)-256
        else:
            ipd4 += block_size
    ip_address_range = "{0}.{1}.{2}.{3}".format(ipd1,ipd2,ipd3,ipd4)
    file_001.write(ip_address_range+"\n")
    ip_address_usable_range = "{0}.{1}.{2}.{3}".format(ipd1,ipd2,ipd3,ipd4+1)
    file_002.write(ip_address_usable_range+"\n")

def get_before_ip_address(ip1,ip2,ip3,ip4,file):
    global ipdt1
    global ipdt2
    global ipdt3
    global ipdt4
    ipdt1 = ip1
    ipdt2 = ip2
    ipdt3 = ip3
    ipdt4 = ip4

    if ipdt4 !=  0 :
        ipdt4 = ipdt4-1
    else:
        ipdt4 = 255
        if ipdt3 != 0 :
            ipdt3 = ipdt3-1
        else:
            ipdt3 = 255 
            if ipdt2 != 0 :
                ipdt2 =  ipdt2 - 1
            else:
                ipdt2 = 255
                ipdt1 = ipdt1-1

    before_ip_address = "{0}.{1}.{2}.{3}".format(ipdt1,ipdt2,ipdt3,ipdt4)
    file.write(before_ip_address+"\n")


for block_size_get in block_size_get_list[:]  :
    block_size,block_get = block_size_get.split(">")
    #ip address range start and ip address usable range start
    ip_address_start_range(int(block_size),int(block_get))
    #ip address range end 
    get_before_ip_address(ipd1,ipd2,ipd3,ipd4,file_001_end)
    #ip address usable range end 
    get_before_ip_address(ipdt1,ipdt2,ipdt3,ipdt4,file_002_end)

file_001.close()
file_001_end.close()
file_002.close()
file_002_end.close()

# set process status - completed
f = open("VLSM\\process_status.rapa","w")
f.write("")
f.close()
