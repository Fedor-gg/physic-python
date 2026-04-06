import math
print("=== Задача 4.2: Спутник Земли ===")


R_z = 6370
h = 200
T_min = 88

R_orb_km = R_z + h
R_orb_m = R_orb_km * 1000

T_sec = T_min * 60
omega_sat = 2 * math.pi / T_sec

V_m_s = omega_sat * R_orb_m
V_km_s = V_m_s / 1000

a_centripetal_sat = V_m_s**2 / R_orb_m

L_km = 2 * math.pi * R_orb_km

N = (24 * 60) / T_min

print(f"1. Радиус орбиты R_орб = {R_orb_km} км ({R_orb_m/1000:.1f} км)")
print(f"2. Угловая скорость ω = {omega_sat:.5f} рад/с")
print(f"3. Линейная скорость V = {V_m_s:.1f} м/с ({V_km_s:.2f} км/с)")
print(f"4. Центростремительное ускорение a_цс = {a_centripetal_sat:.2f} м/с²")
print(f"5. Длина орбиты L ≈ {L_km:.1f} км")
print(f"6. Количество оборотов за сутки N ≈ {N:.2f}")