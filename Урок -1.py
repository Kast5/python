Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



while True:
    try:
        time_s = int(input("\nВведите количество секунд: "))

        if time_s < 1:
            break
        days = time_s // 86400
        hours = (time_s % 86400) // 3600
        mins = ((time_s % 86400) % 3600) // 60
        sec_s = (((time_s % 86400) % 3600) % 60)

        if days > 0:
            if days == 1:
                print("Day:", days, end=" ")
            else:
                print("Days:", days, end=" ")
        if hours > 0:
            if hours ==1:
                print("Hour:", hours, end=" ")
            else:
                print("Hours:", hours, end=" ")
        if mins > 0:
            if mins == 1:
                print("Minute:", mins, end=" ")
            else:
                print("Minutes:", mins, end=" ")
        if sec_s > 0:
            if sec_s ==1:
                print("Second:", sec_s, end=" ")
            else:
                print("Seconds:", sec_s, end=" ")

    except ValueError:
        print("Задание выполнено")


# Задание 2
a = []
for i in range(1000):
    if i % 2 != 0:
        a.append(i ** 3)
print(a)

b = []
sum1 = 0
for num in a: #[5,7,3,4] num = 1, num = 2, num = 3, num = 4
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        b.append(i)
    sum1 = 0
print(sum(b))


sum_num_plus = 0
for num in a:
   summ = 0
   i = num
   num += 17
   while num != 0:
       summ += num % 10
       num = num //10
   if summ % 7 == 0:
       sum_num_plus += i

print(sum_num_plus)


# задание 3
for n in range(1, 101):
    if (10 < n < 20) or (n % 10 in [ 0, 5, 6, 7, 8, 9]):
        print(n, "процентов")
    elif n % 10 == 1:
        print(n, "процент")
    else:
        print(n, "процента")