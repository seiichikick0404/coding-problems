def calculate_max_lit_leds(H, W):
    if H == 1 or W == 1:
        return H * W
    else:
        return ((H + 1) // 2) * ((W + 1) // 2)


H, W = map(int, input().split())
print(calculate_max_lit_leds(H, W))
