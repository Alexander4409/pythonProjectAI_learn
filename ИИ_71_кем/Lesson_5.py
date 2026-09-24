def object():
    sim = int(input())
    pas = int(input())
    user = int(input())

    bits_on_sym = 0
    while(1 << bits_on_sym) < sim:
        bits_on_sym += 1

    pass_len = bits_on_sym * pas
    result = pass_len * user

    print(f'bits: {result}')

object()
