from collections import deque

def count_threats_and_misdirections(s):
    steps = 0
    results = []

    while True:
        queue = deque()
        i = 0
        threats = 0
        misdirections = 0
        n = len(s)

        while i < n:
            if s[i:i+5] == "kalan":  # اگر "kalan" پیدا شد
                j = i + 5  # بررسی بعد از "kalan"
                while j < n and s[j] == ' ':  # شمارش فاصله‌ها
                    j += 1
                if j < n and s[j:j+3] == "tar":  # اگر "tar" بعدش بود
                    if j == i + 5:  # بدون فاصله → تهدید
                        threats += 1
                    else:  # با فاصله → گمراهی
                        misdirections += 1
                    i = j + 3  # پرش به بعد از "tar"
                    continue  # حذف این بخش
            queue.append(s[i])  # کاراکتر را در `deque` قرار بده
            i += 1

        if threats == 0 and misdirections == 0:
            break  # اگر دیگر "kalan tar" نبود، خروج

        s = "".join(queue)  # تبدیل `deque` به رشته برای مرحله بعد
        results.append((threats, misdirections))
        steps += 1

    # چاپ خروجی
    print(steps)
    for t, m in results:
        print(t, m)

# دریافت ورودی و اجرا
s = input().strip()
count_threats_and_misdirections(s)
