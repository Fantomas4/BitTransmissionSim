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

    if remainder is 0:
        pass
    else:
        log.inc_detected_count()


def transmit_msg(msg, log):

    error_in_msg = False

    for bit in range(len(msg)):

        import random

        if random.randint(1, 1000) == 355:
            msg[bit] = not msg[bit]
            error_in_msg = True

    if error_in_msg is True:
        log.inc_actual_count()

    return msg


def bit_num_xor_operation(a, p):

    result_bit_num = []

    print("DIAG - bit_num_xor_operation func: a is : ", a)
    print("DIAG - bit_num_xor_operation func: p is : ", p)
    print("DIAG - bit_num_xor_operation func: result_bit_num is : ", result_bit_num)

    from operator import xor

    # LATHOS LATHOS
    for bit in range(len(a)):
        # LATHOS LATHOS
        print("Loop counter: ", bit)
        print("DIAG - bit_num_xor_operation func: result_bit_num (in loop) is : ", result_bit_num)
        print("DIAG - bit_num_xor_operation func: a[bit] is : ", a[bit])
        print("DIAG - bit_num_xor_operation func: p[bit] is : ", p[bit])

        result_bit_num.append(int(xor(bool(a[bit]), bool(p[bit]))))

    return result_bit_num


def perform_modulo2_operation(msg, p):

    print("DIAG - perform_modulo2_operation func: msg is: ", msg)

    # p number is n+1 bits
    n = len(p) - 1

    # add n 0's to the end of the msg
    for i in range(n):
        msg.append(0)

    print("DIAG - perform_modulo2_operation func: msg after adding 0's is: ", msg)

    # calculate the FCS number

    pos = n-1
    temp_bit_num = []

    # start the modulo2 operation using the first n+1 bit digits of the message
    for bit in range(n+1):
        temp_bit_num.append(msg[bit])

    print("DIAG - perform_modulo2_operation func: temp_bit_num is : ", temp_bit_num)

    while pos != len(msg):

        temp_bit_num = bit_num_xor_operation(temp_bit_num, p)

        # remove any 0's from the front of the number ex. 00010101 --> 10101
        i = 0
        found_1 = False

        while found_1 is False and i < len(temp_bit_num):

            if temp_bit_num[i] == 0:
                del temp_bit_num[i]
            else:
                found_1 = True

            i += 1

        # append the next bit of the original message to the end of the temp bit number used for the modulo 2

        pos += 1

        temp_bit_num.append(msg[pos])

    print("Diag - calculate_crc_code func: The FCS bit number is: ", temp_bit_num)

    return temp_bit_num


def generate_final_message_with_crc_code(msg, p):

    crc_code = perform_modulo2_operation(msg, p)

    return msg + crc_code


def generate_random_message(k):

    msg = []

    for i in range(k):
        import random
        msg.append(random.randint(0, 1))

    print("DIAG - generate_random_message func: msg is: ", msg)

    return msg


def main():

    p_number = int(input("> Enter the P number (bits) you want to use: "))
    k_number = int(input("> Enter the k number (the length (amount of bits) of the messages to be transmitted: "))
    msg_amount = int(input("> Enter the amount of messages that should be transmitted during the simulation: "))

    # convert the user int input for the p_number to a list containing int digits
    temp_list = list(map(int, str(p_number)))

    # the p_number is now a list of int digits
    p_number = temp_list

    print("$$$$$$$$$ p_number list is: ", temp_list)

    transmission_log = TransmissionInfoLog(msg_amount)

    for i in range(msg_amount):

        generated_msg = generate_random_message(k_number)
        final_msg_with_crc_code = generate_final_message_with_crc_code(generated_msg, p_number)
        received_msg = transmit_msg(final_msg_with_crc_code, transmission_log)

        check_received_msg_integrity(received_msg, p_number, transmission_log)

    print("\n\n\n=============== Transmission Log Results ===============")
    print("* Total amount of messages transmitted: ", msg_amount)
    print("* Total amount of messages that were actually transmitted containing bit errors: ", transmission_log.incorrect_msg_transferred_count)
    print("* Total amount of messages that were correctly detected by the CRC as corrupted: ", transmission_log.incorrect_msg_detected_count)


if __name__ == "__main__":
    main()










