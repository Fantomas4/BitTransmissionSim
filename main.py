class TransmissionInfoLog:

    def __init__(self, total_msg_transferred):
        self.incorrect_msg_transferred_count = 0
        self.incorrect_msg_detected_count = 0
        self.total_msg_transferred = total_msg_transferred

    def inc_detected_count(self):
        # increase the counter for the messages that were detected to have been transmitted with errors.
        self.incorrect_msg_detected_count += 1

    def inc_actual_count(self):
        # increase the counter of the messages that were truly transmitted with errors
        self.incorrect_msg_transferred_count += 1


def check_received_msg_integrity(msg, p, log):

    remainder = perform_modulo2_operation(msg, p)

    if 1 in remainder:
        log.inc_detected_count()
    else:
        pass


def transmit_msg(msg, log):

    error_in_msg = False

    for bit in range(len(msg)):

        import random

        #if random.randint(1, 10) == 5:
        if random.randint(1, 1000) == 355:
            msg[bit] = not msg[bit]
            error_in_msg = True

    if error_in_msg is True:
        log.inc_actual_count()

    return msg


def bit_num_xor_operation(a, p):

    result_bit_num = []

    from operator import xor

    for bit in range(len(a)):

        result_bit_num.append(int(xor(bool(a[bit]), bool(p[bit]))))

    return result_bit_num


def perform_modulo2_operation(msg, p):

    # a copy of the msg (list) is created, since changing the original msg list will also change the original msg.
    msg_copy = list(msg)

    temp_bit_num = []

    pos = 0

    while pos < len(msg_copy):
        # when the last digit of the msg is used, the loop must exit

        # remove any 0's from the front of the number ex. 00010101 --> 10101

        for k in range(len(temp_bit_num)):

            if temp_bit_num[0] == 0:
                del temp_bit_num[0]
            else:
                break

        # copy as many digits from the original message as are needed to match the length of the p_number

        while len(temp_bit_num) < len(p) and pos < len(msg_copy):

            temp_bit_num.append(msg_copy[pos])

            pos += 1

        if len(temp_bit_num) == len(p):
            temp_bit_num = bit_num_xor_operation(temp_bit_num, p)

    # remove any 0's from the front of the number ex. 00010101 --> 10101

    for k in range(len(temp_bit_num)):

        if temp_bit_num[0] == 0:
            del temp_bit_num[0]
        else:
            break

    # if the final fcs number result has less than the amount of digits of the
    # original p number - 1, we add as many digits as is needed to the front of the final fcs
    # number, to match the size of the original p_number - 1
    while len(temp_bit_num) < len(p) - 1:
        temp_bit_num.insert(0, 0)

    return temp_bit_num


def generate_final_message_with_crc_code(msg, p):

    # a copy of the msg (list) is created, since changing the original msg list will also change the original msg.
    msg_copy = list(msg)

    # p number is n+1 bits, so we add n bits to the end of the msg
    # add n 0's to the end of the msg
    for i in range(len(p) - 1):
        msg_copy.append(0)

    crc_code = perform_modulo2_operation(msg_copy, p)

    return msg + crc_code


def generate_random_message(k):

    msg = []

    for i in range(k):
        import random
        msg.append(random.randint(0, 1))

    return msg


def main():

    print(""" 
  ____  _ _ _______                            _         _              _____ _           
 |  _ \(_) |__   __|                          (_)       (_)            / ____(_)          
 | |_) |_| |_ | |_ __ __ _ _ __  ___ _ __ ___  _ ___ ___ _  ___  _ __ | (___  _ _ __ ___  
 |  _ <| | __|| | '__/ _` | '_ \/ __| '_ ` _ \| / __/ __| |/ _ \| '_ \ \___ \| | '_ ` _ \ 
 | |_) | | |_ | | | | (_| | | | \__ \ | | | | | \__ \__ \ | (_) | | | |____) | | | | | | |
 |____/|_|\__||_|_|  \__,_|_| |_|___/_| |_| |_|_|___/___/_|\___/|_| |_|_____/|_|_| |_| |_|
                                                                                                                                                                                   
 """)
    print("===========================================================================================\n")

    print("> Welcome to the BitTransmissionSim.\n")

    p_number = int(input("> Enter the P number (bits) you want to use: "))
    k_number = int(input("> Enter the k number (the length (amount of bits) of the messages to be transmitted: "))
    msg_amount = int(input("> Enter the amount of messages that should be transmitted during the simulation: "))

    # convert the user int input for the p_number to a list containing int digits
    temp_list = list(map(int, str(p_number)))

    # the p_number is now a list of int digits
    p_number = temp_list

    transmission_log = TransmissionInfoLog(msg_amount)

    print("\n> Initializing Simulation...\n")

    import sys

    for i in range(msg_amount):

        generated_msg = generate_random_message(k_number)
        # print("generated_msg is: ", generated_msg)
        final_msg_with_crc_code = generate_final_message_with_crc_code(generated_msg, p_number)
        received_msg = transmit_msg(final_msg_with_crc_code, transmission_log)

        check_received_msg_integrity(received_msg, p_number, transmission_log)

        sys.stdout.write("\r> Generated, transmitted and checked %d out of %d total messages..." % (i+1, msg_amount))
        sys.stdout.flush()

    print("\n\n\n=============== Transmission Log Results ===============")
    print("* Total amount of messages transmitted: ", msg_amount)
    print("* Total amount of messages that were transmitted actually containing bit errors: ", transmission_log.incorrect_msg_transferred_count, " (", transmission_log.incorrect_msg_transferred_count/msg_amount * 100, "%)")
    print("* Total amount of messages that were correctly detected by the CRC as corrupted: ", transmission_log.incorrect_msg_detected_count, " (", transmission_log.incorrect_msg_detected_count/msg_amount * 100, "%)")


if __name__ == "__main__":
    main()










