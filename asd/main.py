import math
print("=== Задача 4.1: Колесо обозрения ===")


R = 20
T = 40
h_os = 22
t_half = 20


omega = 2 * math.pi / T

V = omega * R

a_centripetal = V**2 / R

S_half = V * t_half
displacement_half = 2 * R

times = [0, T/4, T/2, 3*T/4, T]
heights = [h_os + R * math.sin(omega * t - math.pi/2) for t in times]

print(f"1. Угловая скорость ω = {omega:.3f} рад/с")
print(f"2. Линейная скорость V = {V:.3f} м/с")
print(f"3. Центростремительное ускорение a_цс = {a_centripetal:.3f} м/с²")
print(f"4. Путь за 20 с (пол-оборота) S = {S_half:.1f} м; Перемещение |r| = {displacement_half} м")
print("5. Высота кабинки h(t):")
for t, h in zip(times, heights):
    print(f"   t = {t:>5.1f} с: h = {h:>6.1f} м")

S_full_check = 2 * math.pi * R
print(f"Проверка: За полный оборот (40 с) путь ≈ {S_full_check:.1f} м")
print()