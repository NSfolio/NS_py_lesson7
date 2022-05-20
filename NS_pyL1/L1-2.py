time_second = int(input('Введите время в секундах:'))
period = 60
time_minut = time_second / period
time_minut_m = time_second // period
time_minut_s = time_second % period
time_hour = time_minut_m / period
time_hour_h = time_minut_m // period
time_hour_m = time_minut_m % period
print("Время:", time_hour_h, "hh:", time_hour_m, "mm:", time_minut_s, "ss")
