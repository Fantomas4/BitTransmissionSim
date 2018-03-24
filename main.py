def transmit_msg(msg):

    for bit in range(len(msg)):

        import random

        if random.randint(1,1000) == 355:
            msg[bit] = not msg[bit]

    return msg

def calculate_CRC_code(p,msg):


def generate_final_message_with_CRC_code(p,msg):

    CRC_code = calculate_CRC_code(p,msg)

def generate_random_message(k):

    msg = []

    for i in range(k):
        import random
        msg.append(random.randint(0,1))

    return msg


def main():

    p_number = input("> Enter the P number (bits) you want to use: ")
    k_number = input("> Enter the k number (the length (amount of bits) of the messages to be transmitted: ")
    msg_amount = input("> Enter the amount of messages that should be transmitted during the simulation: ")

    for i in range(msg_amount):

        generated_msg = generate_random_message()
        received_msg = transmit_msg(generated_msg)


if __name__ == "__main__":
    main()










