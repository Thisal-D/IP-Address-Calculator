#get inputs 
#ip address
file = open("FLSM\\flsm_input_ipaddress.rapa","r")
ip_address = file.readline()
file.close()

#subnets
file = open("FLSM\\flsm_input_subnets.rapa","r")
subnets = file.readline()
file.close()

#hosts
file = open("FLSM\\flsm_input_hosts.rapa","r")
hosts = file.readline()
file.close()

#subnet mask
file = open("FLSM\\flsm_input_subnetmask.rapa","r")
subnet_mask = file.readline()
file.close()

###################################################
###################################################
###################################################
###################################################
###################################################
def binary_to_decimal(bin_num,v_type) :
    index = len(bin_num)-1
    dec_num = 0
    power = 0
    while index != -1 :
        dec_num += int(bin_num[index]) * (2**power)
        power += 1
        index -= 1  
    return v_type(dec_num)
###################################################
###################################################
def decimal_to_binary(val):
    bin_val = bin(val)[2:]
    bin_val =  "0"* (8-len(bin_val)) + bin_val
    return bin_val

###################################################
###################################################
def calculate_subnetmaks_by(val_type,val,ip_c):
    if val_type == "hosts" :
        host_bits = 0 
        while 1:
            if val <= 2**host_bits :
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

    if val_type == "nets" :
        net_bits = 0 
        while 1:
            if val <= 2**net_bits :
                break
            net_bits += 1

        ###################################################
        if ip_c ==  "class c" :
            default_subnet_mask = "255.255.255"
            if net_bits <= 8 :
                host_bits = 8 - net_bits
                sub4_binary = "1"*net_bits + "0"*host_bits
                sub4 = binary_to_decimal(sub4_binary,str)
            subnet_mask = default_subnet_mask + "." + sub4
       
        ###################################################
        if ip_c == "class b" :
            default_subnet_mask = "255.255"
            if net_bits <= 8 :
                host_bits = 8 - net_bits
                sub3_binary = "1"*net_bits + "0"*host_bits
                sub3 = binary_to_decimal(sub3_binary,str)
                sub4 = "0"
            else:
                host_bits = 16 - net_bits
                net_bits = net_bits - 8
                sub3 = "255" 
                sub4_binary = "1"*net_bits +"0"*host_bits
                sub4 =  binary_to_decimal(sub4_binary,str)
            subnet_mask = default_subnet_mask + "." + sub3 + "." + sub4
        
        ###################################################
        if ip_c == "class a"    :
            default_subnet_mask = "255"
            if net_bits <= 8:
                host_bits =  8-net_bits 
                sub2_binary = "1"*net_bits + "0"*host_bits
                sub2 = binary_to_decimal(sub2_binary,str)
                sub3 = "0"
                sub4 = "0"
            elif net_bits <= 16 :
                host_bits = 16 - net_bits
                net_bits = net_bits - 8
                sub2 = "255"
                sub3_binary = "1"*net_bits + "0"*host_bits
                sub3 = binary_to_decimal(sub3_binary,str)
                sub4 = "0"
            else:
                host_bits = 24 - net_bits
                net_bits = net_bits - 16
                sub2 = "255"
                sub3 = "255"
                sub4_binary = "1"*net_bits + "0"*host_bits
                sub4 = binary_to_decimal(sub4_binary,str)
            subnet_mask = default_subnet_mask + "."+ sub2 + "." + sub3 + "." + sub4 
    return subnet_mask

###################################################
###################################################
def calculate_block_size_by_subnet_mask(subnet_mask):
    sub1,sub2,sub3,sub4 = subnet_mask.split(".")
    subs = [sub1,sub2,sub3,sub4]

    block_size_bit  = 0
    block_get = 0

    for sub  in  subs :
        block_get += 1  
        for  bit in decimal_to_binary(int(sub)) :
            if bit == "0" :
                block_size_bit += 1
        if block_size_bit != 0 :
            break
    value = str(2**block_size_bit) +  ","+ str(block_get)
    return value

###################################################
###################################################
def calculate_hosts_subnets_by_subnet_mask(subnet_mask,ip_c):
    sub1,sub2,sub3,sub4 = subnet_mask.split(".")
    subs = [sub1,sub2,sub3,sub4]

    host_bits  = 0
    for sub in subs :
        for bit in decimal_to_binary(int(sub)) :
            if bit == "0" :
                host_bits += 1
    ###################################################

    net_bits = 0
    if ip_c == "class c":
        index = 3 
    elif ip_c  == "class b": 
        index = 2
    else:
        index = 1

    for sub in subs[index:] :
        for bit in decimal_to_binary(int(sub)) :
            if bit == "1" :
                net_bits += 1

    subnets = 2**net_bits
    hosts = 2** host_bits
    val = str(hosts)+","+str(subnets)
    return val

###################################################
###################################################
def  binary_subnet_mask(subnet_mask):
    sub1,sub2,sub3,sub4 = subnet_mask.split(".")
    sub1,sub2,sub3,sub4 = int(sub1),int(sub2),int(sub3),int(sub4)

    sub1_bin = decimal_to_binary(sub1)
    sub2_bin = decimal_to_binary(sub2)
    sub3_bin = decimal_to_binary(sub3)
    sub4_bin = decimal_to_binary(sub4)

    binary_subnetmask = sub1_bin + "." + sub2_bin + "." + sub3_bin + "." + sub4_bin
    return binary_subnetmask

###################################################
###################################################
def seperated_number(val):
    val = str(val)
    val_t = ""
    #reverse number
    for i in range(len(val)-1,-1,-1):
        val_t += val[i]
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
    l_val = ""

    #reberse back
    for i in range(len(val_t1)-1,-1,-1):
        l_val += val_t1[i]
    
    return l_val

###################################################
###################################################
#ip class get

ipd1 ,ipd2 ,ipd3 ,ipd4 = ip_address.split(".")
ipd1 ,ipd2 ,ipd3 ,ipd4 = int(ipd1) ,int(ipd2) ,int(ipd3) ,int(ipd4)

if ipd1 > 191:
    ip_class = "class c"
    default_subnet_mask ="255.255.255.0"
elif ipd1 >127 :
    ip_class = "class b"
    default_subnet_mask ="255.255.0.0"
else:
    ip_class = "class a"
    default_subnet_mask ="255.0.0.0"

file = open("FLSM\\ip_address_class.rapa","w")
if ip_class == "class c"  :
    file.write("Class C")
elif ip_class == "class b" :
    file.write("Class B")
else:
    file.write("Class A")
file.close()    

f = open("FLSM\\ip_address.rapa","w")
ip_address = str(ipd1) + "." + str(ipd2) + "." + str(ipd3) + "." + str(ipd4)
f.write(ip_address)
f.close()

###################################################
###################################################
###################################################
###################################################
#calculate subnet mask
if hosts != "" :
    hosts = str(int(hosts) + 2 )
    subnet_mask = calculate_subnetmaks_by("hosts",int(hosts),ip_class)
elif subnets != "" :
    subnet_mask = calculate_subnetmaks_by("nets",int(subnets),ip_class)

#after subnetting
f=open("FLSM\\subnet_mask.rapa","w")
f.write(subnet_mask)
f.close()
#binary
binary_subnetmask = binary_subnet_mask(subnet_mask)
f=open("FLSM\\binary_subnet_mask.rapa","w")
f.write(binary_subnetmask)
f.close()

#before subnetting (default)
f = open("FLSM\\default_subnet_mask.rapa" ,"w")
f.write(default_subnet_mask)
f.close()
#binary 
binary_default_subnetmask = binary_subnet_mask(default_subnet_mask)
f=open("FLSM\\binary_default_subnet_mask.rapa","w")
f.write(binary_default_subnetmask)
f.close()

###################################################
###################################################
###################################################
###################################################
#calculate ip addresses , hosts and subnets 
hosts , subnets = calculate_hosts_subnets_by_subnet_mask(subnet_mask,ip_class).split(",")
f = open("FLSM\\ip_addresses.rapa","w")
f.write(seperated_number(hosts))
f.close()
f = open("FLSM\\sub_nets.rapa","w")
f.write(seperated_number(subnets))
f.close()
f = open("FLSM\\hosts.rapa","w")
f.write(seperated_number(str(int(hosts)-2)))
f.close()

###################################################
###################################################
###################################################
###################################################
#calculate block size
block_size,block_get = calculate_block_size_by_subnet_mask(subnet_mask).split(",")
f = open("FLSM\\increment_value.rapa" ,"w")
f.write(block_size)
f.close()

f=open("FLSM\\process_status.rapa","w")
f.close()


###################################################
###################################################
###################################################
###################################################
#calculate ranges 
def class_c_range(ip1,ip2,ip3,ip4,block_size):
    ip_ranges = []
    ip_usable_ranges = []
    all_range = []

    loop_run = 1

    if block_size != 1 :
        for ip4 in range(0,256,block_size):
            ip_add = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
            ip_add2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-1)
            ip_range =  ip_add + "     -     "  + ip_add2
            ip_ranges.append(ip_range)

            if block_size > 2 : 
                ip_add_us = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+1)
                ip_add_us2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-2)
                ip_range_us = ip_add_us + "     -     "  + ip_add_us2
                ip_usable_ranges.append(ip_range_us)

                if loop_run == 6 :
                    break
                loop_run += 1
    
    all_range.append(ip_ranges)
    all_range.append(ip_usable_ranges)

    return all_range
###################################################
###################################################
def class_b_range(ip1,ip2,ip3,ip4,block_size,block_get):
    all_range = []
    ip_ranges = []
    ip_usable_ranges = []

    loop_run = 1

    if block_get == 4 :
        if block_size != 1 : 
            for ip3 in range(0,256,1):
                for ip4 in range(0,256,block_size):
                    ip_add = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
                    ip_add2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-1)
                    ip_range =  ip_add + "     -     "  + ip_add2
                    ip_ranges.append(ip_range)

                    if block_size > 2 :
                        ip_add_us = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+1)
                        ip_add_us2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-2)
                        ip_range_us = ip_add_us + "     -     "  + ip_add_us2
                        ip_usable_ranges.append(ip_range_us)

                    if loop_run == 6 :
                        break
                    loop_run += 1
                if loop_run == 6 :
                    break
    
    if block_get == 3 :
        for ip3 in range(0,256,block_size):
            ip_add = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(0)
            ip_add2 = str(ip1) + "." + str(ip2) + "." + str(ip3+block_size-1) + "." + str(255)
            ip_range =  ip_add + "     -     "  + ip_add2
            ip_ranges.append(ip_range)

            ip_add_us = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(1)
            ip_add_us2 = str(ip1) + "." + str(ip2) + "." + str(ip3+block_size-1) + "." + str(254)
            ip_range_us = ip_add_us + "     -     "  + ip_add_us2
            ip_usable_ranges.append(ip_range_us)
            if loop_run == 6 :
                break
            loop_run += 1 

    all_range.append(ip_ranges)
    all_range.append(ip_usable_ranges)

    return all_range

###################################################
###################################################
def class_a_range(ip1,ip2,ip3,ip4,block_size,block_get):
    ip_ranges = []
    ip_usable_ranges = [] 
    all_range = []

    loop_run = 1

    if block_get == 4 :
        if block_size != 1: 
            for ip2 in range(0,256,1) :
                for ip3 in range(0,256,1) :
                    for ip4 in range(0,256,block_size):
                        ip_add = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
                        ip_add2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-1)
                        ip_range =  ip_add + "     -     "  + ip_add2
                        ip_ranges.append(ip_range)

                        if block_size >2 :
                            ip_add_us = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+1)
                            ip_add_us2 = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4+block_size-2)
                            ip_range_us = ip_add_us + "     -     "  + ip_add_us2
                            ip_usable_ranges.append(ip_range_us)
                        if loop_run == 6 :
                            break
                        loop_run += 1
                    if loop_run == 6 :
                        break    
                if loop_run == 6 :
                    break

    if block_get == 3 :
        for ip2 in range(0,256,1):
            for ip3 in range(0,256,block_size):
                ip_add = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(0)
                ip_add2 = str(ip1) + "." + str(ip2) + "." + str(ip3+block_size-1) + "." + str(255)
                ip_range =  ip_add + "     -     "  + ip_add2
                ip_ranges.append(ip_range)

                ip_add_us = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(1)
                ip_add_us2 = str(ip1) + "." + str(ip2) + "." + str(ip3+block_size-1) + "." + str(254)
                ip_range_us = ip_add_us + "     -     "  + ip_add_us2
                ip_usable_ranges.append(ip_range_us)
                if loop_run == 6 :
                     break
                loop_run +=1
            if loop_run == 6 :
                break
    
    if block_get == 2 :
        for ip2 in range(0,256,block_size):
            ip_add = str(ip1) + "." + str(ip2) + "." + str(255) + "." + str(0)
            ip_add2 = str(ip1) + "." + str(ip2+block_size-1) + "." + str(255) + "." + str(255)
            ip_range =  ip_add + "     -     "  + ip_add2
            ip_ranges.append(ip_range)

            ip_add_us = str(ip1) + "." + str(ip2) + "." + str(255) + "." + str(1)
            ip_add_us2 = str(ip1) + "." + str(ip2+block_size-1) + "." + str(255) + "." + str(254)
            ip_range_us = ip_add_us + "     -     "  + ip_add_us2
            ip_usable_ranges.append(ip_range_us)
            if loop_run == 6 :
                break
            loop_run +=1
    
    all_range.append(ip_ranges)
    all_range.append(ip_usable_ranges)

    return all_range

    

if ip_class == "class a" :
    ip_ranges_all = class_a_range(ipd1,ipd2,ipd3,ipd4,int(block_size),int(block_get))
elif ip_class == "class b":
    ip_ranges_all = class_b_range(ipd1,ipd2,ipd3,ipd4,int(block_size),int(block_get))
else:
    ip_ranges_all = class_c_range(ipd1,ipd2,ipd3,ipd4,int(block_size))


files = ["FLSM\\ip_ranges.rapa","FLSM\\ip_usable_ranges.rapa"]

index = 0
while len(files) > index :
    f = open(files[index],"w")
    for i in ip_ranges_all[index] :
        f.write(i+"\n")
    index += 1 

f = open("FLSM\\process_status.rapa","w")
f.close()
