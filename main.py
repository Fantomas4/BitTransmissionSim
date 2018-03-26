
def transmit_msg(msg):

    for bit in range(len(msg)):

        import random

        if random.randint(1,1000) == 355:
            msg[bit] = not msg[bit]

    return msg


def modulo2_operation(a, b):

    result_bit_num = []

    from operator import xor

    for bit in range(len(a)):
        result_bit_num.append(xor(bool(a[bit]), bool(b[bit])))

    return result_bit_num


def calculate_crc_code(p,msg):

    # p number is n+1
    n = p - 1

    # add n 0's to the end of the msg
    for i in range(n):
        msg.append(0)

    # calculate the FCS number

    pos = n-1
    temp_bit_num = msg

    # for bit in range(0, n-1):
    #     temp_bit_num.append(msg[bit])

    while pos != len(msg):

        temp_bit_num = modulo2_operation(temp_bit_num, p)

        for bit in range(len(temp_bit_num)):
            # remove any 0's from the front of the number ex. 00010101 --> 10101
            if temp_bit_num[bit] == 0:
                del temp_bit_num[bit]

        pos += 1

        # append the next bit of the original message to the end of the temp bit number used for the modulo 2
        temp_bit_num.append(msg[pos])


def generate_final_message_with_crc_code(p,msg):

    CRC_code = calculate_crc_code(p,msg)


def generate_random_message(k):

    msg = []

    for i in range(k):
        import random
        msg.append(random.randint(0,1))

    return msg


def main():

    p_number = int(input("> Enter the P number (bits) you want to use: "))
    k_number = int(input("> Enter the k number (the length (amount of bits) of the messages to be transmitted: "))
    msg_amount = int(input("> Enter the amount of messages that should be transmitted during the simulation: "))

    for i in range(msg_amount):

        generated_msg = generate_random_message(k_number)
        received_msg = transmit_msg(generated_msg)


if __name__ == "__main__":
    main()










