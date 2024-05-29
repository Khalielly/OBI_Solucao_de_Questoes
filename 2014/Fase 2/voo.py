def fuction_day(p_A, c_B, p_B, c_A):
    day = 24 * 60

    for fuso in range(-11, 13):
        partida = (p_A + fuso * 60) % day
        fim = c_B

        x = (fim - partida) % day

        partida = (p_B - fuso * 60) % day
        fim = c_A

        y = (fim - partida) % day

        if x == y and x < day // 2:
            duracao = x
            break

    return duracao, fuso

def tempo_para_minutos(tempo):
    h, m = map(int, tempo.split(":"))
    return h * 60 + m

if __name__ == "__main__":
    entrada = input().split()

    p_A, c_B, p_B, c_A = map(tempo_para_minutos, entrada)

    duracao, fuso = fuction_day(p_A, c_B, p_B, c_A)

    print(duracao,fuso)









