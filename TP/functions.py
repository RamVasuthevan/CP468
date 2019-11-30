
#normalization
def num_in_interval(lo, hi, mult, steps):
    step_size = (hi - lo) / steps
    return lo + mult * step_size


def general_decoder(string, var_length, domain_start, domain_end):
    # Split string into variables
    bin_list = [string[i:i + var_length] for i in range(0, len(string), var_length)]

    # Convert each variable from binary to decimal
    dec_list = [(int(num, 2)) for num in bin_list]

    # Map each decimal to a floating point number in the range (domain_start, domain_end)
    xs = [(num_in_interval(domain_start, domain_end, dec_list[i], 2 ** len(bin_list[i]))) for i in range(len(dec_list))]
    return xs
